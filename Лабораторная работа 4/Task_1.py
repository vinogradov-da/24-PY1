import json


def task(file) -> float:
    with open('input.json') as file:
        data = json.load(file)
    total = sum(item["score"] * item["weight"] for item in data)

    return round(total, 3)


json_file = 'input.json'

print(task(input))
