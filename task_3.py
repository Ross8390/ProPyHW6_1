queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

def quantity_search(object: list) -> dict:
    dict = {}

    for query in queries:
        words = query.split()

        if len(words) in dict.keys():
            dict[len(words)] += 1
        else:
            dict.update({len(words): 1})

    return dict

def count_percentage():
    object = quantity_search(queries)
    for key, value in object.items():
        percentage = round((value / len(queries)) * 100)
        print(f'Запросов из {key} слова: {percentage}% ')
    return


if __name__ == '__main__':
    count_percentage()

