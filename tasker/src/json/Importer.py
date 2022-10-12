import json


class Importer:

    def __init__(self):
        pass

    def read_tasks(self):
        with open(r"taski.json", encoding='utf-8') as f:
            data = json.load(f)
            
        return data

    def get_tasks(self):
        return self.read_tasks()
        