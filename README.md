# 📚 StudyRAG – AI Powered Study Assistant

StudyRAG is a Retrieval-Augmented Generation (RAG) based AI assistant that allows users to upload study materials and ask natural language questions. The assistant retrieves relevant information from the uploaded documents using hybrid search and generates context-aware answers with Google Gemini.

---

## 🚀 Features

- 📄 Upload multiple PDF, DOCX, and PPT/PPTX files
- 🌐 Upload Website URLs
- 🎥 Upload YouTube videos (using transcripts)
- 🔍 Hybrid Retrieval (Semantic Search + BM25)
- 📊 Cross-Encoder Reranking for improved retrieval quality
- 🤖 AI-powered answers using Google Gemini
- 📌 Source citations for every generated answer
- 💬 Modern React-based chat interface
- ⚡ FastAPI backend with REST APIs

---

## 🏗️ Project Architecture

```
                React Frontend
                       │
                       ▼
                 FastAPI Backend
                       │
       ┌───────────────┼───────────────┐
       │               │               │
   PDF/DOCX/PPT     Website URL     YouTube URL
       │               │               │
       └───────────────┼───────────────┘
                       ▼
               Loader Factory Pattern
                       ▼
                Text Extraction
                       ▼
                   Chunking
                       ▼
          Sentence Transformer Embeddings
                       ▼
                  ChromaDB Vector Store
                       ▼
              Hybrid Retrieval Pipeline
      (Semantic + BM25 + RRF + Reranker)
                       ▼
                Google Gemini LLM
                       ▼
                 Final AI Response
```

---

# 🛠️ Tech Stack

## Frontend

- React.js
- Vite
- Axios
- CSS

## Backend

- FastAPI
- Pydantic
- Python

## AI / RAG

- Google Gemini
- Sentence Transformers
- ChromaDB
- BM25
- Reciprocal Rank Fusion (RRF)
- Cross Encoder Reranker

## Document Processing

- PyPDF
- python-docx
- python-pptx
- BeautifulSoup
- youtube-transcript-api

---

# 📂 Supported Input Sources

- PDF
- DOCX
- PPT / PPTX
- Website URLs
- YouTube Videos

---

# ⚙️ How It Works

### 1. Upload Documents

Users upload one or more study materials.

↓

### 2. Text Extraction

The system extracts text using the appropriate loader.

↓

### 3. Chunking

Documents are divided into overlapping chunks.

↓

### 4. Embedding Generation

Sentence Transformers convert chunks into vector embeddings.

↓

### 5. Vector Storage

Embeddings and metadata are stored in ChromaDB.

↓

### 6. User Question

A question is sent from the frontend.

↓

### 7. Hybrid Retrieval

The system retrieves relevant chunks using:

- Semantic Search
- BM25 Keyword Search
- Reciprocal Rank Fusion
- Cross-Encoder Reranking

↓

### 8. Answer Generation

Retrieved context is sent to Google Gemini to generate an accurate answer.

↓

### 9. Response

The frontend displays:

- AI-generated answer
- Source documents
- Warnings (if applicable)

---

# 📡 API Endpoints

## Health Check

```
GET /
```

---

## Upload Files

```
POST /upload/files
```

Supports:

- PDF
- DOCX
- PPT/PPTX

---

## Upload Website / YouTube

```
POST /upload/source
```

Example:

```json
{
    "source":"https://en.wikipedia.org/wiki/Graph_theory"
}
```

---

## Chat

```
POST /chat
```

Example:

```json
{
    "question":"Explain Graph Coloring."
}
```

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/sanchi1406/study-rag.git
```

Go to backend

```bash
cd backend
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY

MODEL_NAME=YOUR_MODEL

EMBEDDING_MODEL=BAAI/bge-small-en-v1.5

CHROMA_DB_PATH=vector_db

CHROMA_COLLECTION=study_notes

UPLOAD_DIR=uploads

CHUNK_SIZE=800

CHUNK_OVERLAP=200
```

Run backend

```bash
uvicorn app.main:app --reload
```

Go to frontend

```bash
cd frontend
```

Install packages

```bash
npm install
```

Run frontend

```bash
npm run dev
```

---

# 📈 Future Improvements

- Authentication & User Accounts
- Conversation Memory
- OCR Support for Scanned PDFs
- Streaming Responses
- Metadata Filtering
- Multi-user Workspaces
- Deployment with Docker
- Cloud Vector Database

---

# 📸 Screenshots
<img width="1037" height="746" alt="image" src="https://github.com/user-attachments/assets/c5cf6571-0fdc-4b1e-a71b-9245645936c3" />

(Add screenshots of your application here.)

---

# 👩‍💻 Author

**Sanchi**

GitHub: https://github.com/sanchi1406
