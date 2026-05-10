import os
import datetime
import shutil
from core.config import MEMORY_DIR, BACKUPS_DIR
from core.cleanup import check_and_compact_memory

def backup_memory(file_path: str):
    """
    Creates a backup of the specified memory file with a timestamp.
    """
    if not os.path.exists(file_path):
        return
    
    filename = os.path.basename(file_path)
    name, ext = os.path.splitext(filename)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"{name}_{timestamp}{ext}"
    backup_path = os.path.join(BACKUPS_DIR, backup_filename)
    
    shutil.copy2(file_path, backup_path)
    # print(f"Backed up {filename} to {backup_filename}")

def absorb_knowledge(topic: str, content: str):
    """
    Parses expert feedback and updates the relevant .md file in /memory.
    Automatically triggers a backup and checks for compaction.
    """
    # Sanitize topic to create a valid filename
    filename = f"{topic.lower().replace(' ', '_')}.md"
    file_path = os.path.join(MEMORY_DIR, filename)
    
    # Backup existing memory before writing
    backup_memory(file_path)
    
    # Append the new knowledge
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    knowledge_entry = f"\n\n## Update: {timestamp}\n{content}\n"
    
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(knowledge_entry)
        
    # Check if the memory file needs compaction
    check_and_compact_memory(file_path)

def read_knowledge(topic: str) -> str:
    """
    Reads knowledge from the corresponding .md file in /memory.
    """
    filename = f"{topic.lower().replace(' ', '_')}.md"
    file_path = os.path.join(MEMORY_DIR, filename)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    return "No prior knowledge on this topic."
