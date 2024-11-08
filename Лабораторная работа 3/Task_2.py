def find_common_participants(first_group, second_group, sign = ','):
    first = set(first_group.split(sign))
    second = set(second_group.split(sign))
    common_participants = first.intersection(second)
    return sorted(list(common_participants))


first_group = "Иванов|Петров|Сидоров"
second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(first_group, second_group, sign = '|')
print(common_participants)
