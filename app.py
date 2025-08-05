# app.py

from flask import Flask, request, jsonify, render_template
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever  # from qubiten_vector_index.py

from flask_cors import CORS

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app, resources={r"/predict": {"origins": "*"}})  # Allow any site to access this route

# Initialize your Ollama model + prompt chain
model = OllamaLLM(model="deepseek-r1:1.5b")

template = """
You are Qubiten’s AI compliance expert, guiding website visitors on our industry-specific compliance offerings, pricing, and related legal/regulatory questions.

Here is context from Qubiten’s knowledge base: {services_info}

User question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json(force=True)
    question = payload.get("message", "").strip()
    if not question:
        return jsonify({"error": "Please provide a non-empty question."}), 400

    # Retrieve relevant service docs and run the LLM chain
    services_info = retriever.invoke(question)
    answer = chain.invoke({
        "services_info": services_info,
        "question": question
    })

    return jsonify({"answer": answer})


if __name__ == "__main__":
    # In production, switch debug=False and use a WSGI server
    app.run(host="0.0.0.0", port=5000, debug=True)
