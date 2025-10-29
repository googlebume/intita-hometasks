import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        func()
        time_end = time.time()
        return time_end-time_start
    return wrapper

@execution_time
def cycle():
    i = 0
    while(i != 10):
        if i == 10:
            break
        print(i)
        i += 1 


print(f"Виконання зайняло {cycle()} секунд")