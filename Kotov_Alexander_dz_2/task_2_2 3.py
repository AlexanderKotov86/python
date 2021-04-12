list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

print(id(list_1))

for item_list in range(len(list_1)):
    if list_1[item_list].isdigit():
        list_1[item_list] = '"' + f'{int(list_1[item_list]):02d}' + '"'
    elif (list_1[item_list][:1] == '+' or list_1[item_list][:1] == '-') and list_1[item_list][1:].isdigit():
        list_1[item_list] = '"' + list_1[item_list][:1] + f'{int(list_1[item_list][1:]):02d}' + '"'

print(id(list_1))
print(' '.join(list_1))
