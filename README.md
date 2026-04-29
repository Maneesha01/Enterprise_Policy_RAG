# 📊 Enterprise Policy RAG  
AI-Powered Retrieval-Augmented Generation (RAG) System for HR Policy Q&A  

---

## 🚀 Overview  

Enterprise Policy RAG is a Retrieval-Augmented Generation (RAG) system designed to answer employee queries related to company HR policies.  

It combines:
- Vector database (ChromaDB)  
- Embeddings (HuggingFace)  
- LLM (Llama 3 via Ollama)  
- LangChain framework  

The system retrieves relevant policy documents and generates accurate, context-aware responses.

---

## 🧠 Architecture  

```
User Query
    ↓
Retriever (Chroma Vector DB)
    ↓
Relevant Policy Documents
    ↓
LLM (Llama3 via Ollama)
    ↓
Final Answer
```

---

## 📂 Project Structure  

```
Enterprise_Policy_RAG/
│
├── implementation/
│   ├── ingest.py              # Data ingestion & vector DB creation
│   └── answer.py              # RAG pipeline (retrieval + generation)
│
├── knowledge-base/
│   └── HR-policies/
│       ├── employee_benefits.md
│       ├── leave_policy.md
│       ├── travel_expense_policy.md
│       ├── wellness_policy.md
│       └── wfh_policy.md
│
├── vector_db/                 # Persisted embeddings (ChromaDB)
│
├── app.py                     # (Optional UI / entry point)
├── test.ipynb                 # Testing notebook
└── README.md
```

---

## ⚙️ Tech Stack  

- Python  
- LangChain  
- ChromaDB (Vector Database)  
- HuggingFace Embeddings (`all-MiniLM-L6-v2`)  
- Ollama (Llama 3.2)  
- Gradio (UI - optional)  

---

## 🔄 Workflow  

### 1. Data Ingestion  
- Load HR policy documents (.md files)  
- Split content using Markdown headers  
- Generate embeddings  
- Store in Chroma vector database  

### 2. Query Processing  
- User asks a question  
- Retrieve top-k relevant documents  
- Pass context + query to LLM  
- Generate final answer  

---

## 🧾 Key Components  

### 📥 Ingestion (`ingest.py`)  
- Loads documents from `knowledge-base/HR-policies`  
- Splits into structured chunks  
- Stores embeddings in `vector_db`  

---

### 🤖 RAG Pipeline (`answer.py`)  
- Retrieves relevant documents  
- Combines chat history with query  
- Generates response using LLM  

---

## ▶️ Setup & Installation  

### 1. Clone Repository  
```
git clone https://github.com/your-username/Enterprise_Policy_RAG.git
cd Enterprise_Policy_RAG
```

### 2. Create Virtual Environment  
```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install Dependencies  
```
pip install -r requirements.txt
```

---

## 🔑 Environment Variables  

Create a `.env` file:  

```
OPENAI_API_KEY=your_key   # (used as placeholder for local Ollama)
```

---

## 🧠 Run Ollama Model  

Make sure Ollama is running locally:  

```
ollama run llama3.2:1b
```

---

## 📥 Run Data Ingestion  

```
python implementation/ingest.py
```

This will:
- Process documents  
- Create embeddings  
- Store them in `vector_db/`  

---

## 💬 Run Query 

You can call the function from `answer.py`:

```python
from implementation.answer import answer_question

response, docs = answer_question("What is the leave policy?")
print(response)
```

---

## 📊 Example Query  

```
What is the work from home policy?
```

### Example Output  

```
Employees are allowed to work remotely based on manager approval...
```

---

## 🔍 Features  

- ✅ Retrieval-Augmented Generation (RAG)  
- ✅ Context-aware responses  
- ✅ Markdown-based document ingestion  
- ✅ Vector search using ChromaDB  
- ✅ Local LLM inference using Ollama  
- ✅ Modular and scalable design  

---



---

