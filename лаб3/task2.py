def find_common_participants(str1, str2, split=','):
    str1_ = set(str1.split(split))
    str2_ = set(str2.split(split))
    common = str1_.intersection(str2_)
    return sorted(common)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))

