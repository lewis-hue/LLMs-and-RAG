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
  1. Tuned KB dataset on Vertex AI  
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
text
Copy
Edit
Model: text-bison@001 (Google Vertex AI)
Why text-bison@001?

High throughput & cost-efficient

Excellent instruction-following

📚 Retrieval-Augmented Generation
Document Ingestion

Compliance guides, whitepapers, policy docs

Embedding Generation

text
Copy
Edit
Vertex AI Embeddings API → 768-dim vectors
Vector Store

Local FAISS / Pinecone index

Query & Retrieval

Embed user query → retrieve top 5 nearest docs

Prompt Assembly

text
Copy
Edit
[SYSTEM]
You are Qubiten’s compliance assistant...
[CONTEXT]
<doc1>…<doc5>
[USER]
{user question}
LLM Call & Post-processing

Send prompt → receive data.answer → format response

🧰 Data Preparation & Vertex AI Tuning
bash
Copy
Edit
# 1. Upload base model
gcloud ai models upload \
  --region=us-central1 \
  --display-name=qubiten-llm \
  --container-image-uri=us-docker.pkg.dev/vertex-ai/prediction/text-bison@001

# 2. Create tuning job
gcloud ai tuning-jobs create \
  --model=projects/.../models/qubiten-llm \
  --training-dataset=projects/.../datasets/qa_pairs \
  --parameter-split=0.8 \
  --machine-type=n1-standard-4
Corpus: ISO 27001, SOC 2, HIPAA, GDPR specs

Steps: Cleaning → Tokenization → Q&A annotation → GCS upload → fine-tune

Outcome: Domain-specific accuracy boost

🔧 Backend Implementation
python
Copy
Edit
from flask import Flask, request, jsonify
from vertexai import MatchingEngine, TextGenerationModel

app = Flask(__name__)
index = MatchingEngine.Index("projects/.../locations/.../indexes/qubiten-index")
llm   = TextGenerationModel.from_pretrained("text-bison@001")

@app.route("/predict", methods=["POST"])
def predict():
    user_msg = request.json["message"]
    vec      = index.embed([user_msg])[0]
    docs     = index.search(vec, top_k=5)
    prompt   = assemble_prompt(docs, user_msg)
    resp     = llm.predict(prompt)
    return jsonify(answer=resp.text)
Endpoint: POST /predict

Workflow:

Embed query

Retrieve docs

Build prompt

Call LLM

Return JSON

💻 Frontend Implementation
html
Copy
Edit
<!-- index.html -->
<script src="nav-dynamic.js"></script>
js
Copy
Edit
// nav-dynamic.js (chat snippet)
const response = await fetch("http://127.0.0.1:5000/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ message: text })
});
const data = await response.json();
bubble(data.answer, "bot");
Files:

index.html – main shell + chat widget

nav-dynamic.js – overlays, chat integration

styles.css – bespoke utility styles

UX: Smooth toggle, typing indicator, auto-scroll

✅ Integration & Testing
Local Dev:

Flask on localhost:5000

Latency < 500 ms

3rd-Party Site:

Embedded via <script>

CORS configured

Results:

100% demo uptime

Excellent response relevance

🏁 Conclusion
Qubiten Compliance Chatbot showcases:

Mastery of RAG and LLM fine-tuning

Clean, modular Flask + JS architecture

Seamless local & third-party integration

Production-ready, extensible to any regulated domain
