# TODO решите задачу
import json

def task() -> float:
    with open("input.json", "r") as f:
        data = json.load(f)
    total = sum(elem["score"]*elem["weight"] for elem in data)
    return round(total, 3)


print(task())
