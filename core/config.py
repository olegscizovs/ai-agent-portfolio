import os

# Model Configuration
MODEL_NAME = 'qwen3.5-big'
CONTEXT_WINDOW = 32768  # 32k context

# Directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMORY_DIR = os.path.join(BASE_DIR, 'memory')
BACKUPS_DIR = os.path.join(MEMORY_DIR, 'backups')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
PROJECT_SPECS_DIR = os.path.join(BASE_DIR, 'project_specs')

# Create necessary directories
os.makedirs(MEMORY_DIR, exist_ok=True)
os.makedirs(BACKUPS_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(PROJECT_SPECS_DIR, exist_ok=True)

# Compaction Configuration
MAX_MEMORY_FILE_SIZE_KB = 50
MAX_MEMORY_FILE_SIZE_BYTES = MAX_MEMORY_FILE_SIZE_KB * 1024
