def find_common_participants(first, second, sign=","):
    first = set(first.split(sign))
    second = set(second.split(sign))
    
    common_participants = first.intersection(second)
    return sorted(list(common_participants))


first_group = "Иванов|Петров|Сидоров"
second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(first_group, second_group, sign="|")
print(common_participants)
