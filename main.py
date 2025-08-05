# qubiten_agent.py

from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# Initialize the local Ollama model
model = OllamaLLM(model="deepseek-r1:1.5b")

# Prompt template tailored for Qubiten’s compliance-services AI assistant
template = """
You are Qubiten’s AI compliance expert, guiding website visitors on our industry-specific compliance offerings, pricing, and related legal/regulatory questions.

Here are some relevant details from Qubiten’s knowledge base: {services_info}

User question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

if __name__ == "__main__":
    while True:
        print("\n\n-------------------------------")
        question = input("Ask about Qubiten’s services (or ‘q’ to quit): ")
        print("\n\n")
        if question.strip().lower() == "q":
            break

        # Retrieve the top-k relevant compliance documents
        services_info = retriever.invoke(question)
        # Run the chain with the retrieved context
        result = chain.invoke({
            "services_info": services_info,
            "question": question
        })
        print(result)
