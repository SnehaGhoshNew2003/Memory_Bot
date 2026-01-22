'''from neo4j import GraphDatabase
import time

class MemoryStore:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def store(self, user_id, text, embedding, confidence):
        with self.driver.session() as session:
            session.run(
                """
                CREATE (m:Memory {
                    user_id: $user_id,
                    text: $text,
                    embedding: $embedding,
                    confidence: $confidence,
                    created_at: $ts
                })
                """,
                user_id=user_id,
                text=text,
                embedding=embedding,
                confidence=confidence,
                ts=time.time()
            )

    def recall(self, user_id, min_conf=0.4, limit=8):
        with self.driver.session() as session:
            res = session.run(
                """
                MATCH (m:Memory {user_id: $user_id})
                WHERE m.confidence >= $min_conf
                RETURN m.text AS text
                ORDER BY m.created_at DESC
                LIMIT $limit
                """,
                user_id=user_id,
                min_conf=min_conf,
                limit=limit
            )
            return [r["text"] for r in res]

    def decay(self, factor=0.95):
        with self.driver.session() as session:
            session.run(
                "MATCH (m:Memory) SET m.confidence = m.confidence * $f",
                f=factor
            )
            '''

# backend/memory_store.py

from neo4j import GraphDatabase
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv() 

class MemoryStore:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            os.getenv("NEO4J_URI"),
            auth=(
                os.getenv("NEO4J_USERNAME"),
                os.getenv("NEO4J_PASSWORD")
            )
        )

    def store(self, user_id: str, text: str, confidence: float):
        query = """
        CREATE (m:Memory {
            user_id: $user_id,
            text: $text,
            confidence: $confidence,
            created_at: datetime($created_at)
        })
        """
        with self.driver.session() as session:
            session.run(
                query,
                user_id=user_id,
                text=text,
                confidence=confidence,
                created_at=datetime.utcnow().isoformat()
            )

    def recall(self, user_id: str, min_conf: float = 0.6, limit: int = 5):
        query = """
        MATCH (m:Memory)
        WHERE m.user_id = $user_id AND m.confidence >= $min_conf
        RETURN m.text AS text
        ORDER BY m.created_at DESC
        LIMIT $limit
        """
        with self.driver.session() as session:
            records = session.run(
                query,
                user_id=user_id,
                min_conf=min_conf,
                limit=limit
            ).data()

        return [r["text"] for r in records if r.get("text")]
