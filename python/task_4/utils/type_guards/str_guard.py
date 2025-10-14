def safe_input_str(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            print("Введіть текст, а не число!")
        elif value == "":
            print("Поле не може бути порожнім!")
        else:
            return value
        
def validate_task_text(text: str):
    if not text.strip():
        raise ValueError("Текст таски не може бути порожнім")
    if len(text) > 500:
        raise ValueError("Текст таски занадто довгий (максимум 500 символів)")