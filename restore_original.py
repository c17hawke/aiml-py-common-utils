from pathlib import Path
import os
import logging
import shutil

logging.basicConfig(
    level=logging.INFO,
    format= "[%(asctime)s: %(levelname)s]: %(message)s"
    )

ROOT = Path("./")

backup_directory_name = ".template_backup"
backup_directory = ROOT / backup_directory_name

def reset_backup():
    for path in backup_directory.rglob("**/*"):
        src = path
        dest = src.relative_to(backup_directory_name)
        dest = ROOT / dest
        dest.parent.mkdir(exist_ok=True, parents=True)
        shutil.copy2(src=src, dst=dest)
        logging.info(f"restoring backup of file: {src.name} at path: {dest}")

if backup_directory.exists():
    logging.info(f"`{backup_directory_name}` directory is present")
    reset_backup()
else:
    logging.info(f"`{backup_directory_name}` directory is NOT present, hence aborting!")
