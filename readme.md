# Project Title: MemoriaVerse

## 🧠 Project Overview

**MemoriaVerse** is a dual-purpose application designed to demonstrate the power and versatility of **memory-based search and retrieval** algorithms. It features two distinct modules:

1.  **Oraculum:** A memory-assisted **Fake News Detection** tool.
2.  **CipherQuest:** An adaptive, memory-based **Password Guessing Game**.

The core of MemoriaVerse lies in its efficient, memory-centric data architecture, which allows for rapid, context-aware lookups and pattern matching across both structured and unstructured data.

---

## 🚀 Key Features

### 1. Oraculum: Fake News Detection

* **Associative Search:** Quickly checks incoming news snippets against a curated, in-memory **knowledge base** of known facts and debunked claims.
* **Contextual Scoring:** Uses similarity metrics (e.g., semantic or vector-based) to score the likelihood of a claim being fabricated, even if the exact wording is new.
* **Rapid Verification:** Designed for near-instantaneous search and comparison, highlighting the speed advantages of in-memory data structures (e.g., specialized hash maps, trie structures, or vector databases).

### 2. CipherQuest: Password Guessing Game

* **Adaptive Memory:** The "opponent" (the game's AI) learns and remembers previous valid and invalid guess patterns (e.g., length, character sets, common sequences) from the player.
* **Strategic Guessing:** The AI uses its learned memory to *intelligently* narrow down its next guess, showcasing how pattern analysis and memory recall can be used in a security context.
* **Difficulty Scaling:** The game's difficulty increases as the AI's memory of the player's past choices grows, making it a true test of randomness and security best practices.

---

## 🛠 Technology Stack

| Component | Technology/Tool | Purpose |
| :--- | :--- | :--- |
| **Backend Language** | Python (or your language) | Core logic and algorithm implementation. |
| **Memory Store** | Redis, Memcached, or Custom In-Memory DB | For rapid data storage and retrieval. |
| **Semantic Search** | Hugging Face Transformers, Sentence-BERT (optional) | To generate vector embeddings for news data (Oraculum). |
| **Frontend/UI** | Streamlit, Flask/React, or CLI | User interface for interacting with the two modules. |

---

## ⚙ Installation and Setup

### Prerequisites

* [List any required software, e.g., Python 3.9+]
* [List any required external services, e.g., A running Redis instance]

### Steps

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourUsername/MemoriaVerse.git](https://github.com/YourUsername/MemoriaVerse.git)
    cd MemoriaVerse
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Memory Store:**
    * If using **Redis**, ensure your server is running and update the connection details in `config.py`.
    * If using a **custom in-memory store**, no further steps are required.

4.  **Initialize Knowledge Base (Oraculum):**
    * The fake news module requires pre-loaded data. Run the setup script:
    ```bash
    python setup_oraculum.py
    ```

---

## ▶ Usage

### 1. Launch the Application

Run the main application script:

```bash
python run_app.py
