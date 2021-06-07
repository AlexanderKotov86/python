import random

objects = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

num = int(input('Кол-во шуток: '))
repeats_1 = input('Можно с повторами? Y/N: ')

if str.lower(repeats_1) == 'y':
    repeats = True
elif str.lower(repeats_1) == "n":
    repeats = False
else:
    print('Неправильный ответ')
    quit()


def get_jokes_adv(num, repeats):
    """Function to return jokes. num (int) - count of jokes, repeats (bool) - repeating of words """

    joke_list = []

    if not repeats:
        if num > min(len(objects), len(adverbs), len(adjectives)):
            print('Так не получится')
        else:
            random.shuffle(objects)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            for idx in range(num):
                joke_list.append(f'{objects[idx]} {adverbs[idx]} {adjectives[idx]}')

    else:
        for idx in range(num):
            cur_objects = random.choice(objects)
            cur_adverbs = random.choice(adverbs)
            cur_adjectives = random.choice(adjectives)
            joke_list.append(f'{cur_objects} {cur_adverbs} {cur_adjectives}')
    return joke_list


print(get_jokes_adv(num, repeats))
