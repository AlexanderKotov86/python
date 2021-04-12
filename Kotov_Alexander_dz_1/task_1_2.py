min_list = 1
max_list = 1000
list = [min_list]

while min_list < max_list:
    if (min_list + 1) % 2 != 0:
        min_list = min_list + 1
        list.append(min_list ** 3)
    else:
        min_list = min_list + 1
print(list)
idx = 0
ch_7 = 0
total_7 = 0

while idx < len(list) and list[idx] != 0:
    ch_7 += list[idx] % 10
    list[idx] //= 10
    if ch_7 % 7 == 0:
      total_7 += list[idx]
      idx += 1
    else:
      idx += 1

print("Сумма /7 ", total_7)

min_list = 1
start_list = 17
max_list = 1000
list = [start_list]

while min_list < max_list:
    if (min_list + 1) % 2 != 0:
        min_list = min_list + 1
        list.append(17 + min_list ** 3)
    else:
        min_list = min_list + 1
print(list)
idx = 0
ch_7 = 0
total_7 = 0

while idx < len(list) and list[idx] != 0:
    ch_7 += (list[idx]) % 10
    list[idx] //= 10
    if ch_7 % 7 == 0:
      total_7 += list[idx]
      idx += 1
    else:
      idx += 1

print("Сумма +17 /7 ", total_7)
