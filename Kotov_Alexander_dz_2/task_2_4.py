position_name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for item_list in range(len(position_name)):
    name_raw = position_name[item_list].split(' ')
    name = name_raw[-1].capitalize()
    print('Привет,', name + '!')
