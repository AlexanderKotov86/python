value_start = 0
value_stop = 20
list_values = [value_start]

while value_start < value_stop:
       value_start = value_start + 1
       list_values.append(value_start)
idx = 0
while idx < len(list_values):
    percent_value = list_values[idx]
    symbols_long = len(str(percent_value))
    if symbols_long >= 3:
        percent_value_unified = int(percent_value) % (10 ** (symbols_long - 1))
    else:
        percent_value_unified = int(percent_value)

    percent_count = percent_value_unified % 10
    base_text = "процент"
    list_endings = ["", "ов", "а"]

    if percent_value_unified > 10 and percent_value_unified < 20:
        base_text_end = base_text + list_endings[1]
    elif percent_count == 0 or percent_count > 4:
        base_text_end = base_text + list_endings[1]
    elif percent_count == 1:
        base_text_end = base_text + list_endings[0]
    else:
        base_text_end = base_text + list_endings[2]
    list_values[idx] = str(percent_value) + " " + base_text_end
    idx += 1

print(list_values)



percent_value = input("Значение % ",)
symbols_long = len(percent_value)
if symbols_long >= 3:
    percent_value_unified = int(percent_value) % (10 ** (symbols_long -1))
else:
    percent_value_unified = int(percent_value)

percent_count = percent_value_unified % 10
base_text = "процент"
list_endings = ["", "ов","а"]

if percent_value_unified > 10 and percent_value_unified < 20:
    base_text_end = base_text + list_endings[1]
elif percent_count == 0 or percent_count > 4:
    base_text_end = base_text + list_endings[1]
elif percent_count == 1:
    base_text_end = base_text + list_endings[0]
else:
    base_text_end = base_text + list_endings[2]

print(percent_value, base_text_end)



