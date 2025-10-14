import os.path
import json
from pathlib import Path


class BaseFileHandler():
    def __init__(self, paths = None, exists = None):
        current_file = Path(__file__).resolve()
        self.project_root = str(current_file.parents[3]) + "\database\database.json"
        # print(self.project_root)
        exists = os.path.exists(self.project_root)
        if not exists:
            # print("Не створено")
            file = open(self.project_root, 'w')
            file.write('')
            file.close()


    def is_exists(self):
        return os.path.exists(self.project_root)
    
    def delete_file(self):
        exists = self.is_exists()
        if exists: 
            os.remove(self.project_root)

    def write_file(self, data):
        with open(self.project_root, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def read_file(self):
        if not self.is_exists():
            return []
        with open(self.project_root, 'r', encoding='utf-8') as file:
            return json.load(file)