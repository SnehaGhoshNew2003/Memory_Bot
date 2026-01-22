# Memory_Bot

Long-Term Personal AI with Persistent Memory using Neo4j + LangChain + Gemini
MemoryAI is a personal AI system that remembers conversations across sessions, stores long-term memories in a graph database (Neo4j), and recalls relevant context intelligently using LangChain + Gemini.

## Features

- **Long-term memory** across chats and restarts
- **Graph-based memory storage** using Neo4j
- **Context-aware memory recall**
- **Memory confidence & decay support** (extensible)
- **Gemini LLM integration** via LangChain
- **FastAPI backend** 
- **Streamlit frontend** for intuitive UI
- **Fully Dockerized** (Backend + Frontend + Neo4j)
- **Response is sent back to user.**

## Project Structure
```
MemoryAI/
│
├── backend/
│ ├── init.py
│ ├── chain.py # LangChain execution logic
│ ├── config.py # Environment config loader
│ ├── gemini.py # Gemini LLM + embeddings
│ ├── main.py # FastAPI app entry
│ ├── memory_store.py # Neo4j memory layer
│ ├── Dockerfile # Backend Dockerfile
│ └── test.py # Backend tests
│
├── frontend/
│ ├── app.py # Streamlit UI
│ └── Dockerfile # Frontend Dockerfile
│
├── .env # Environment variables
├── docker-compose.yml # Full system orchestration
├── requirements.txt # Python dependencies
├── LICENSE # MIT License
└── README.md # This file
```


## 🔧 Tech Stack

- **LLM**: Google Gemini (via LangChain)
- **Memory DB**: Neo4j (Graph Database)
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Orchestration**: Docker & Docker Compose

## Environment Variables

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_gemini_api_key
NEO4J_URI=bolt://neo4j:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
```
## Docker Setup
Build & Run Everything
```
docker compose up --build
```

**This starts:**
- Neo4j → http://localhost:7474
- Backend → http://localhost:8000
- Frontend → http://localhost:8501

## Data Flow
1. **User Input **→ User sends message via Streamlit frontend with their user_id
2.** API Receipt** → FastAPI backend receives POST /chat request with message and user ID
3. **Memory Check **→ System checks if message contains memory recall triggers (keywords, questions, or contextual cues)
4.** Recall Path** → If recalling memories:
    - Queries Neo4j for relevant user memories.
    - Retrieves top N contextually relevant memories.
    - Passes memories + current message to LLM.
5. **Storage Path** → If not recalling:
    - Routes message through memory importance filter.
    - Extracts important personal facts using LLM.
    - Stores significant facts in Neo4j as structured memory nodes.
6. **Response Generation** → LLM generates response using:
    - Current conversation context.
    - Retrieved memories (if any).
    - System instructions for memory management.
7. **Response Delivery** → Generated response sent back through API → displayed in frontend.
8. **Memory Update** → Memory access counters and timestamps updated in Neo4j.
