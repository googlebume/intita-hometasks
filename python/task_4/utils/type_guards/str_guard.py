def safe_input_str(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            print("Введіть текст, а не число!")
        elif value == "":
            print("Поле не може бути порожнім!")
        else:
            return value