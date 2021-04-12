price_list = [57.8, 46.51, 97, 43, 67.02, 90, 12.7, 19, 43.8, 76.04]

for price in range(len(price_list)):
    rub = int(price_list[price])
    kk = int(round((price_list[price] - rub) * 100))      # без округления выдает некорректное значение копеек
    price_list[price] = str(rub) + " руб. " + f'{kk:02d}' + ' коп.'

print(id(price_list))
print('A:', ', '.join(price_list))
price_list.sort()
print('B:', id(price_list), ', '.join(price_list))

price_list_max_min = sorted(price_list, reverse=True)
print('C:' , id(price_list_max_min), ', '.join(price_list_max_min))

print('D: ', ', '.join(price_list_max_min[:5]))