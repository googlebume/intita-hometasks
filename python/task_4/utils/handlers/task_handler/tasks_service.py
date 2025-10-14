class TaskService:
    def __init__(self, crypto, file_handler):
        self.crypto = crypto
        self.file_handler = file_handler
        self.tasks = []

    def add(self, text: str):
        if any(t["task"].lower() == text.lower() for t in self.tasks):
            raise ValueError(f"Таска '{text}' вже існує")
        task = {"id": self.crypto.gen_id(text), "task": text}
        self.tasks.append(task)
        self.file_handler.write_file(str(self.tasks))
        return task

    def edit(self, index: int, new_text: str):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Таска не існує")
        if any(i != index and t["task"].lower() == new_text.lower() for i, t in enumerate(self.tasks)):
            raise ValueError(f"Таска '{new_text}' вже існує")
        old = self.tasks[index]["task"]
        self.tasks[index].update({"task": new_text, "id": self.crypto.gen_id(new_text)})
        return old, new_text

    def remove(self, index: int):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Таска не існує")
        return self.tasks.pop(index)

    def list_all(self):
        return self.tasks
