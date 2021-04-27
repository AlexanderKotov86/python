names_list = ['Илья', 'Петр', 'Мария', 'Иван']


def thesaurus(names_list):
    dict_names = {}
    names_list = sorted(names_list)
    for name in names_list:
        dict_names.setdefault(name[0], [])
        dict_names[name[0]].append(name)
    print(dict_names)


thesaurus(names_list)

names_surnames_list = ['Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева']


def thesaurus_ad(names_surnames_list):
    dict_names_surnames = {}
    names_surnames_list = sorted(names_surnames_list)
    for name_surname in names_surnames_list:
        name, surname = name_surname.split()
        dict_names_surnames.setdefault(surname[0], [])
        dict_names_surnames[surname[0]].append(name_surname)
    sorted_dict_tuple = sorted(dict_names_surnames.items(), key=lambda x: x[0])
    dict_names_surnames_sorted = dict(sorted_dict_tuple)
    print(dict_names_surnames_sorted)


thesaurus_ad(names_surnames_list)
