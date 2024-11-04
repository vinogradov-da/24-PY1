def find_common_participants(first, second, argument=','):
    first = set(first.split(argument))
    second = set(second.split(argument))
    common_participants = first.intersection(second)
    return sorted(list(common_participants))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, argument='|')
print(common_participants)
