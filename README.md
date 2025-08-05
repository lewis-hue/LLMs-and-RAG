# Qubiten Compliance Chatbot: An LLM-Powered RAG System

<p align="center">
  <img src="https://img.shields.io/badge/Tech%20Stack-LLM%20%7C%20RAG%20%7C%20Vertex%20AI-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Tech Stack Badge" />
  <img src="https://img.shields.io/badge/Backend-Python%20%7C%20Flask-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Backend Badge" />
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="Frontend Badge" />
</p>

## **Project Overview**

An intelligent RAG-powered assistant for Qubiten that delivers expert guidance on compliance services using a fine-tuned LLM and a custom knowledge base.


### **Key Features**

* **Intelligent RAG System:** Seamlessly integrates a Google Vertex AI LLM with a vector store for contextual, accurate responses.
* **Domain-Specific Expertise:** Fine-tuned LLM on compliance guides, whitepapers, and legal documents for enhanced precision.
* **Scalable Architecture:** Designed with a modular Python/Flask backend and a clean, responsive JavaScript frontend for easy deployment and maintenance.
* **Interactive UI:** Features a dynamic chat widget with smooth animations, typing indicators, and a clean user experience.


---

## **Technical Stack**

### **Backend & AI/ML**
* **LLM & RAG:** Google Vertex AI (`text-bison@001`), Vertex AI Embeddings API
* **Framework:** Flask
* **Language:** Python
* **Vector Store:** In-memory FAISS or cloud-based Pinecone (configurable)

### **Frontend**
* **Technologies:** HTML5, CSS3, JavaScript (ES6+)
* **Key Components:** Dynamic navigation overlays (`nav-dynamic.js`), interactive chat widget (`chat.js`), RESTful API communication (`fetch`)

---

## **Architecture & Implementation**

### **1. RAG Workflow**

**flowchart TD**

    A[👤 User Query] -->|1. POST /predict| B(🌐 Flask Backend)
    B -->|2. Embed Query| C{🔍 Vector Store}
    C -->|3. Top-k Retrieval| B
    B -->|4. Construct Prompt| D[🤖 Vertex AI LLM<br/>(text-bison@001)]
    D -->|5. Generate Answer| B
    B -->|6. Return JSON| A

  ### 2. Backend Code (app.py)

A clean, well-documented Flask application that handles API requests, orchestrates the RAG pipeline, and serves the frontend. The chat endpoint is the core of the system.

```{python}
# app.py
from flask import Flask, render_template, request, jsonify
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever  # Placeholder for vector store logic
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

try:
    model = OllamaLLM(model="deepseek-r1:1.5b")
    template = """
    You are a helpful and professional Qubiten sales and support assistant...
    Context from relevant services: {services}
    User's Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    logging.getLogger(__name__).info("LangChain model initialized.")
except Exception as e:
    logging.getLogger(__name__).error(f"Failed to init LLM: {e}")
    chain = None

@app.route('/api/chat', methods=['POST'])
def chat():
    if not chain:
        return jsonify({'error': 'AI model unavailable.'}), 503
    try:
        user_message = request.get_json().get('message')
        services_context = retriever.invoke(user_message)
        result = chain.invoke({"services": services_context, "question": user_message})
        return jsonify({'answer': result})
    except Exception as e:
        logging.getLogger(__name__).error(f"Chat error: {e}")
        return jsonify({'error': 'An internal error occurred.'}), 500


### 3. Frontend Code (chat.js)

The frontend is built for a responsive and engaging user experience. The chat.js file manages all chat-specific logic, cleanly separating it from the rest of the site's functionality.

```{javascript}
// /static/js/chat.js
(() => {
  const form = document.getElementById("chat-form");
  const input = document.getElementById("user-input");
  const pane = document.getElementById("chat-window");
  const API_URL = "http://127.0.0.1:5000/api/chat";

  // UI rendering and helpers (toggle, bubble creation, autoresize)

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const text = input.value.trim();
    if (!text) return;

    bubble(text, "user");
    input.value = "";
    const wait = bubble('<span class="typing"><span></span><span></span><span></span></span>', "bot", true);
    
    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text }),
      });
      const result = await response.json();
      const reply = result.answer || "I'm sorry, I didn't get a valid response.";
      wait.remove();
      bubble(reply, "bot");
    } catch (err) {
      console.error("API Error:", err);
      wait.remove();
      bubble("I'm having trouble connecting to the server.", "bot");
    }
  });

  // Initialization and event listeners
})();


### Tuning Dataset (used as knowledge base)

![Tuning dataset for knowledge base](https://github.com/lewis-hue/LLMs-and-RAG/blob/main/Tuned%20Model%20Success.png)




### Local AI Agent


![Local AI Agent Response 1](https://github.com/lewis-hue/LLMs-and-RAG/blob/main/Local%20Agent%20success%201.png)




![Local AI Agent Response 2](https://github.com/lewis-hue/LLMs-and-RAG/blob/main/Local%20Agent%20success%202.png)



### Local AI Agent integrated into a third-party website

![Integrated AI Agent](https://github.com/lewis-hue/LLMs-and-RAG/blob/main/Website%20AI%20Agent%20Success.png)



### Project Outcome

This project successfully demonstrates the end-to-end development of a powerful, domain-specific chatbot. The modular design facilitates future scaling and integration into other platforms, while the RAG architecture ensures responses are both accurate and relevant to the provided context, minimizing hallucination. This solution provides a strong foundation for building enterprise-grade LLM applications.
