<p align="center">
  <img src="https://img.shields.io/badge/LLM–RAG–Google%20Vertex%20AI-blue" alt="Tech Stack Badge" />
  <img src="https://img.shields.io/badge/Flask–Python-green" alt="Backend Badge" />
  <img src="https://img.shields.io/badge/HTML–CSS–JS-yellow" alt="Frontend Badge" />
</p>

# <code>🎯 Qubiten Compliance Chatbot</code>

> **An intelligent, Retrieval-Augmented LLM assistant** powering compliance guidance for ISO 27001, SOC 2, HIPAA & GDPR.

---

## 📑 Table of Contents

1. [Project Summary](#project-summary)  
2. [Architecture Diagram](#architecture-diagram)  
3. [LLM & RAG Components](#llm--rag-components)  
   - [LLM Model](#llm-model)  
   - [Retrieval-Augmented Generation](#retrieval-augmented-generation)  
4. [Data Preparation & Vertex AI Tuning](#data-preparation--vertex-ai-tuning)  
5. [Backend Implementation](#backend-implementation)  
6. [Frontend Implementation](#frontend-implementation)  
7. [Integration & Testing](#integration--testing)  
8. [Conclusion](#conclusion)

---

## 🔍 Project Summary

- **Company Simulation:** Qubiten – Compliance services provider  
- **Technologies:**  
  - **LLM & RAG:** Google Vertex AI LLM (`text-bison@001`)  
  - **Backend:** Python, Flask, Vertex AI REST API  
  - **Frontend:** HTML, CSS, JavaScript  
  - **Deployment:** Local & third-party site integration  
- **Key Features:**  
  1. Tuned knowledge-base dataset on Vertex AI  
  2. Document embeddings & similarity search  
  3. Interactive chat widget overlay  
  4. End-to-end flow: user → retrieval → LLM → response  

**Skills & Keywords:**  
LLM · RAG · Google Vertex AI · Embeddings · Flask · Python · JavaScript · HTML · CSS · REST API · Chatbot · Architecture · Documentation

---

## 🏗️ Architecture Diagram

```mermaid
flowchart TD
  A[👤 User] -->|sends query| B[🌐 Web UI]
  B -->|POST /predict| C[🐍 Flask Backend]
  C -->|embed query| D{🔍 Vector Store}
  C -->|similarity search| D
  D -->|top-k docs| C
  C -->|construct prompt| E[🤖 Vertex AI LLM<br/>text-bison@001]
  E -->|generates answer| C
  C -->|return JSON| B
  B -->|render| A
Figure 1: High-level flow from user request to response.
🤖 LLM & RAG Components
▶️ LLM Model
Model: text-bison@001 (Google Vertex AI)
Model: text-bison@001 (Google Vertex AI)
Why text-bison@001?

High throughput & cost-efficient

Excellent instruction-following

📚 Retrieval-Augmented Generation
**1. Document Ingestion**

Compliance guides, whitepapers, policy docs

**2. Embedding Generation**
**
Vertex AI Embeddings API → 768-dim vectors**

**3. Vector Store**

Local FAISS / Pinecone index

**4. Query & Retrieval
**
Embed user query → retrieve top 5 nearest docs

**5. Prompt Assembly**
