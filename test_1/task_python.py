# Задание 1
# Создайте отдельный список с мужчинами и отдельный список с женщинами.

list_of_man = ["Eddard Stark",
               "Robb Stark",
               "Jaime Lannister",
               "Tyrion Lannister",
               "Joffrey Baratheon",
               "Robert Baratheon",
               "Viserys Targaryen",
               "Jon Snow"]

list_of_woman = ["Catelyn Stark",
                 "Sansa Stark",
                 "Cersei Lannister",
                 "Daenerys Targaryen"]
                
# Задание 2
# Допустим, что все мужчины и женщины выстроились в линию в алфавитном порядке и
# рассчитались на первый-второй. Нужно получить список людей, которые оказались вторыми.
# Для этого напишите функцию, которая принимает в качестве аргументов два списка с
# мужчинами и женщинами и возвращает список людей, оказавшихся вторыми.
# Примечание: для нахождения алфавитного порядка НЕ нужно менять местами имя и фамилию.

def task_2(list1, list2):
    new_list = list1 + list2
    new_list.sort()
    result = new_list[1::2]
    return result
task_2(list_of_man,list_of_woman)

# Задание 3
# Для каждой пары людей узнайте, являются ли они однофамильцами. Для этого создайте 
# словарь, где ключом является пара людей. Значением словаря будет 1, если пара является 
# однофамильцами, и 0, если их фамилии отличаются.

# Примечание 1: в паре могут быть люди любого пола.
# Примечание 2: порядок людей в паре значения не имеет.
# Примечание 3: тип данных и значение ключа может быть любым, с которым вам удобно 
# работать. Главное, чтобы по ключу было понятно, кто именно входит в пару.

import itertools

def get_same_surname(men, women):
    line = list(itertools.combinations([elem.split(' ') for elem in women+men], 2))
    return {(' '.join(elem[0]), ' '.join(elem[1])): 1 if elem[0][1] == elem[1][1] else 0 for elem in line}

x   

# Задание 4
# Узнайте состав каждой семьи, которая встречается в предоставленных списках. 
# Для этого создайте словарь, где ключом является фамилия. Значением словаря будет список
# всех однофамильцев (и мужчин, и женщин).

list_of_names = list_of_man + list_of_woman
from collections import defaultdict
result = defaultdict(list)
for elem in list_of_names:
    result[elem.split()[1]].append(elem.split()[0]) 

dict_task4 = dict(result)

# Задание 5
# Узнайте размер каждой семьи, используя словарь из задания 4. В качестве ответа выведите
# на экран несколько строчек: в каждой строчке должна быть указана семья и ее размер. 
# Для вывода на экран используйте команду print().


for key, value in dict_task4.items():
    print(key, len([item for item in value]))