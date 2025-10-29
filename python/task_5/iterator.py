tasks = [
    {
        "name": "Погладити котика <3",
        "executeBy": '19.10.2025'
    },
    {
        "name": "Вийти погуляти з другом о 13:00",
        "executeBy": '19.10.2025'
    },
    {
        "name": "Потяг",
        "executeBy": '20.10.2025'
    },
]

def iterator(tasks):
    i = 0
    while i < len(tasks):
        if len(tasks[i]['name']) >= 10:
            print(tasks[i]['name'])
            yield tasks[i]
        i += 1
    yield 'end'


gen = iterator(tasks)
for item in gen:
    pass
