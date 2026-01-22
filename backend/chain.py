from backend.gemini import llm
from backend.memory_store import MemoryStore
from langchain_core.prompts import ChatPromptTemplate

store = MemoryStore()

prompt = ChatPromptTemplate.from_template(
    """
You are a personal AI with long-term memory.

Relevant memories:
{memories}

User says:
{input}

Respond intelligently using recalled memory.
"""
)

def run_chain(user_id: str, user_input: str):
    # Recall memory
    recalled = store.recall(user_id)
    formatted = "\n".join(recalled) if recalled else "None"

    # Run LLM
    chain = prompt | llm
    response = chain.invoke({
        "memories": formatted,
        "input": user_input
    }).content

    # Store memory
    store.store(
        user_id=user_id,
        text=user_input,
        confidence=0.9
    )

    return response
