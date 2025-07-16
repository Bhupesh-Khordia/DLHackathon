# 🤖 MATLAB Troubleshooting Chatbot

Hackathon Project – **CS-671 (Deep Learning)**

This project aims to build a chatbot that helps users troubleshoot MATLAB-related queries using deep learning. Users interact through a Streamlit-based web interface where they can ask MATLAB questions. Our system uses LangChain, Hugging Face models, and several deep learning libraries to provide relevant responses.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: LangChain,Langgraph, Python, Flask
- **LLMs**: Hugging Face Transformers, Gemini
- **Vector Store**: FAISS
- **Database**: MongoDB
---

## 🚀 Features

- Chat-based troubleshooting for MATLAB errors and syntax
- Chat-based multi-turn troubleshooting with memory.
- Image based trouleshooting for MATLAB errors.
- Citation of sources or documentation sections in responses.
- Analytics dashboard for admin users.
- Contextual query understanding via document retrieval.
- LLM-powered answers based on MATLAB full documentation.
- User-friendly UI interface.
- Multi Chat Sessions maintainenece to access previous chats
- Authentication for user and admin accounts.
- Modular, extensible backend pipeline.

---

## Project Structure 
```
├── backend
│   ├── agents
│   │   ├── answerQnaAgent.py
│   │   ├── answerRagAgent.py
│   │   ├── autocompleteAgent.py
│   │   ├── decisionAgents.py
│   │   ├── imageQueryAgent.py
│   │   ├── intialAnsweringAgent.py
│   │   ├── qnaDbAgents.py
│   │   ├── queryAnnotatorAgent.py
│   │   └── scrapingAgent.py
│   ├── database.py
│   ├── faiss_vector_store
│   │   ├── index.faiss
│   │   └── index.pkl
│   ├── main.py
│   ├── __pycache__
│   │   └── main.cpython-310.pyc
│   ├── qnaDB
│   │   ├── index.faiss
│   │   └── index.pkl
│   └── requirements.txt
├── Backend.jpg
├── frontend
│   ├── app.py
│   └── libs
├── Frontend_UI.jpg
├── README.md
├── results
└── visited.txt
```

## 🧩 Frontend User Flow

![Frontend User Flow 1](Frontend_UI.jpg)


---

## 🔧 Backend Flow

![Backend Flowchart](Backend.jpg)

---

## ⚙️ Setup Instructions

.env file example (in backend directory) - 

```bask
GEMINI_API_KEY=your_gemini_api
MONGODB_URI=your_database_uri
HUGGINGFACEHUB_API_TOKEN="your_huggingface_api_token"
```


1. Clone the repository:

```bash
git clone https://github.com/your-username/matlab-chatbot.git
cd matlab-chatbot
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python backend/database.py
```

```bash
streamlit run frontend/app.py
```

## 📄 Example Queries
[Examples queries](results/)

## 👥 Team

Developed as part of **CS-671 Deep Learning Hackathon**.

- Bhupesh Yadav - B23200
- Piyush Kumar - B23167
- Asif Hoda - B23253
- Manjeet Rai - B23152
- Tarun Singh - B23103
- Yashodeep - B23040

## Admin username and pass
- username: abc
- pass: pqr
