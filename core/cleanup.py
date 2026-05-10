import os
from core.config import MAX_MEMORY_FILE_SIZE_BYTES, MODEL_NAME
from rich.console import Console

try:
    from langchain_community.llms import Ollama
except ImportError:
    Ollama = None

console = Console()

def check_and_compact_memory(file_path: str):
    """
    Checks if a memory file exceeds the size limit and triggers compaction if necessary.
    """
    if not os.path.exists(file_path):
        return
        
    size_bytes = os.path.getsize(file_path)
    
    if size_bytes > MAX_MEMORY_FILE_SIZE_BYTES:
        console.print(f"\n[bold yellow]⚠️  Memory file {os.path.basename(file_path)} exceeds limit ({size_bytes/1024:.2f} KB). Compacting...[/bold yellow]")
        compact_memory(file_path)

def compact_memory(file_path: str):
    """
    Summarizes the contents of the memory file using a local LLM call to reduce size
    while preserving key architectural decisions and learning points.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        console.print(f"[dim]Initiating LLM summarization for {os.path.basename(file_path)}...[/dim]")
        
        if Ollama is None:
            console.print("[yellow]Langchain Ollama not available. Performing simple truncation...[/yellow]")
            compacted_content = content[-10000:] # Keep last 10k chars roughly
        else:
            llm = Ollama(model=MODEL_NAME)
            prompt = (
                "You are an expert AI architect. Please summarize the following accumulated "
                "learnings and best practices into a concise, highly dense knowledge document. "
                "Preserve all specific rules, code standards, and critical decisions, but remove "
                "redundancies and conversational filler.\n\n"
                f"ORIGINAL CONTENT:\n{content}\n\n"
                "COMPACTED KNOWLEDGE:"
            )
            compacted_content = llm.invoke(prompt)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("# Compacted Knowledge\n\n" + compacted_content)
            
        console.print(f"[bold green]✅ Compaction complete for {os.path.basename(file_path)}.[/bold green]")
    except Exception as e:
        console.print(f"[bold red]❌ Error compacting {os.path.basename(file_path)}: {e}[/bold red]")
