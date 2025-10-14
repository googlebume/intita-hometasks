def safe_input_int(prompt: str, min_value: int = None) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Значення має бути не менше {min_value}.")
                continue
            return value
        except ValueError:
            print("Введіть ціле число!")

def validate_task_number(number: int):
    if not isinstance(number, int) or number < 1:
        raise ValueError("Номер таски має бути більше 0")
