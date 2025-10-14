def format_task_list(tasks):
    if not tasks:
        return "Список тасок порожній"
    return "Всі таски:\n\n" + "\n".join(
        f"{i+1}. {t['task']}" for i, t in enumerate(tasks)
    )
