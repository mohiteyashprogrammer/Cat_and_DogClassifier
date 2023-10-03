import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,format="[%(asctime)s]: %(message)s)"
)

package_name = "CNN_Classifier"


list_of_files=[
   ".github/workflows/.gitkeep",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/components/__init__.py", 
   f"src/{package_name}/utils/__init__.py", 
   f"src/{package_name}/config/__init__.py", 
   f"src/{package_name}/pipeline/__init__.py", 
   f"src/{package_name}/entity/__init__.py", 
   f"src/{package_name}/constants/__init__.py",
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   "configs/config.yaml",
   "params.yaml",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "research/trials.ipynb", 
    ]

for filepath in list_of_files:
    file_path = Path(filepath)
    filedir,filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Direcotry: {filedir} for the file {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file: {file_path}")

    else:
        logging.info(f"{file_path} is already exists")
