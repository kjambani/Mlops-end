import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "mlopsProject"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "dvc.yaml",
    "requirements.txt",
    "setup.py",
    "app.py",
    "Dockerfile",
    "main.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    file_path = Path(filepath)
    file_dir = file_path.parent
    if not file_dir.exists():
        file_dir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {file_dir}")
    if not file_path.exists():
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Created empty file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")
    