def safe_input_float(prompt: str, min_value: float = None) -> float:
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Значення має бути не менше {min_value}.")
                continue
            return value
        except ValueError:
            print("Введіть число (можна з крапкою або комою).")