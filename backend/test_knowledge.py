from app.modules.knowledge.engine import (
    KnowledgeEngine
)

engine = KnowledgeEngine()

knowledge = engine.build_knowledge(
    "app/storage/uploads/sales.csv"
)

print(knowledge)