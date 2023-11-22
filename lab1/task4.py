users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
new_txt = {'Общее количество': 0, 'Уникальные посещения': 0}

new_txt['Общее количество'] = len(users)
new_txt['Уникальные посещения'] = ("user1" in users) + ("user2" in users) + ("user3" in users) + ("user4" in users)

#Уникальные посещения можно так же посчитать через множества
#new_txt['Уникальные посещения'] = len(set(users))



print(new_txt)