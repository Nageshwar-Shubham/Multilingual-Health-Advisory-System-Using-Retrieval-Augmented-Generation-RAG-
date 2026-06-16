# Multilingual Health Advisory System Using RAG 🏥🌐

AI-powered healthcare advisory system that utilizes Retrieval-Augmented Generation (RAG) to deliver accurate, context-aware, and multiple language response for medical guidance grounded in trusted health documents.

---

## ✨ Features

* **Grounded Generation (RAG)**: Eliminates AI hallucinations by cross-referencing external medical documents before drafting responses.
* **Multilingual Translation Layer**: Translates user health queries in real time to process and return medical advice across multiple languages.
* **Optimized Vector Storage**: Features semantic search indexing managed by **ChromaDB** for fast context retrieval.
* **Modular Pipeline**: Clean separation between backend processing (`app.py`), database ingestion (`store.py`), and business logic (`src`).
* **Interactive Dashboard**: A clean web-based UI backed by standard templates for seamless user interaction.

---

## 📂 Project Structure

```text
├── chroma_db/          # Main vector database collection storage
├── data/               # Raw medical references, PDFs, or guidelines text
├── notebook/           # Experimental Jupyter Notebooks for testing RAG logic
├── src/                # Core source code (embeddings processing, RAG prompt engine)
├── static/             # Frontend assets (CSS stylesheets, UI images, JavaScript)
├── templates/          # HTML templates for the web app UI
├── .gitignore          # Environment and dependency exclusion rules
├── LICENSE             # Open-source MIT license agreement
├── app.py              # Main application web server gateway
├── requirements.txt    # Production package dependencies
├── setup.py            # Local environment layout installation configuration
├── store.py            # Script to ingest and embed text data into ChromaDB
└── test.py             # Sandbox execution script for basic sanity checks
```

---

## 🛠️ Tech Stack

* **Core Framework**: Python 3.8+
* **Web Architecture**: Flask / FastAPI
* **RAG Orchestration**: LangChain 
* **Vector Engine**: ChromaDB
* **Embeddings & LLM**: Groq_cloud / HuggingFace Transformers

---

## 🚀 Getting Started

Follow these instructions to configure and run the full web application locally.

### 📋 Prerequisites

Ensure you have Python 3.8+ installed along with pip. 

### ⚙️ Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd Multilingual-Health-Advisory-System-Using-Retrieval-Augmented-Generation-RAG-
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install the source package locally:**
   ```bash
   pip install -e .
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   LLM_API_KEY=your_secret_api_key_here
   ```

---

## 💻 Running the Application

### 1. Ingest Data into the Vector Database
Before booting the server, run the storage script to chunk, embed, and store your reference texts into `chroma_db`:
```bash
python store.py
```

### 2. Launch the Web Application Server
Start the development server to activate the web user interface:
```bash
python app.py
```
Open your web browser and navigate to `http://127.0.0.1:5000` (or the terminal-assigned port).

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
