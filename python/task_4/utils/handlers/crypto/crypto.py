import uuid

class Crypto():
    def gen_id(self, task_text: str) -> str:
        return str(uuid.uuid5(uuid.NAMESPACE_DNS, task_text))