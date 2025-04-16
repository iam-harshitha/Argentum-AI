# 💼 Argentum-AI: Your Regulated Financial Chat Assistant

**Argentum-AI** is a smart, locally hosted financial chatbot that leverages Retrieval-Augmented Generation (RAG) and cutting-edge LLMs (like Meta LLaMA-3 via Groq) to answer investment-related questions from PDF documents.  
It's built for financial compliance, concise answers, and an intuitive chat-like user interface — all without relying on cloud storage or third-party PDFs.

---

## 🚀 How It Works 

### 📄 Step 1: Upload a PDF
Users start by uploading a financial document (such as a mutual fund brochure or prospectus) through a simple drag-and-drop interface.

### 📁 Step 2: Parsing & Chunking
The uploaded PDF is read and split into smaller, semantically meaningful text chunks using **PyMuPDF** and custom logic — ensuring high-quality retrieval.

### 🧠 Step 3: Vectorization & FAISS Indexing
Each chunk is embedded using **SentenceTransformers** (`all-MiniLM-L6-v2`) and stored in a local **FAISS** vector index. This makes real-time semantic search blazing fast.

### 🔍 Step 4: Retrieval Based on User Query
When a user types a question, the top relevant document chunks are retrieved from the FAISS index based on vector similarity.

### 📾 Step 5: Prompting the LLM
These chunks are combined with a carefully structured prompt and sent to the **Meta LLaMA-3 8B model** hosted via **Groq API**, ensuring responses are grounded in the retrieved context.

### 💬 Step 6: Response Display (Chat Interface)
The response is shown in a sleek, conversational interface built using **Streamlit**, where previous questions and answers are retained — allowing ongoing Q&A in a natural chat flow.

---

## 🛠️ Tech Stack & Purpose

| Technology | Role |
|------------|------|
| **Streamlit** | 🎋 Frontend UI for chat and PDF upload |
| **PyMuPDF** | 📄 Extract text from PDF files |
| **SentenceTransformers** | 📌 Generate dense vector embeddings for document chunks |
| **FAISS** | ⚡ Build and search a fast local vector store |
| **Groq API** | 🧠 Call Meta LLaMA-3 for concise, contextual answer generation |
| **Transformers** | 🔀 Handles tokenizer and language model structure |
| **Requests** | 📡 Manage external HTTP API communication |
| **Python** | 🐍 Core programming language for backend logic |


---

## 🧰 Source Files 

| File | Description |
|------|-------------|
| `app.py` | 🎯 Main Streamlit app: Handles UI, session, prompt construction, and full orchestration |
| `loader.py` | 📄 Extracts and chunks PDF text |
| `rag.py` | 🧠 Builds FAISS index, handles vector search |
| `llm.py` | 🤖 Sends prompts to Groq-hosted Meta LLaMA-3 and returns clean answers |
| `.env` | 🔐 Stores your Groq API key (`GROQ_API_KEY`) securely |
| `requirements.txt` | 📆 Lists Python dependencies |

---

## 🖼️ Screenshots
![Screenshot 2025-04-16 122504](https://github.com/user-attachments/assets/737cc6b9-7286-4f5f-a18d-ac9ae48ac231)
![Screenshot 2025-04-16 122520](https://github.com/user-attachments/assets/1ac86e91-9ce6-4dfb-b4df-103b42e71990)


## 🔮 Future Improvements

- Support uploading and processing multiple PDFs
- Add logging and history tracking of user queries
- Include optional references to source chunks in responses
- Allow download/export of chat history
- Potential cloud deployment for wider access

---

