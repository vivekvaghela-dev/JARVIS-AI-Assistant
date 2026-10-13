from livekit.agents import function_tool
import json
import os
from datetime import datetime

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "memory_data.json")

@function_tool
def load_memory() -> list:
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

@function_tool
def save_memory(data: list) -> None:
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

@function_tool
def add_memory_entry(speaker: str, text: str) -> None:
    data = load_memory()
    data.append({
        "speaker": speaker,
        "text": text,
        "timestamp": datetime.now().isoformat()
    })
    save_memory(data)

@function_tool
def get_recent_conversations(limit: int = 10) -> list:
    data = load_memory()
    return data[-limit:]