geo_logs = [
     {'visit1': ['Москва', 'Россия']},
     {'visit2': ['Дели', 'Индия']},
     {'visit3': ['Владимир', 'Россия']},
     {'visit4': ['Лиссабон', 'Португалия']},
     {'visit5': ['Париж', 'Франция']},
     {'visit6': ['Лиссабон', 'Португалия']},
     {'visit7': ['Тула', 'Россия']},
     {'visit8': ['Тула', 'Россия']},
     {'visit9': ['Курск', 'Россия']},
     {'visit10': ['Архангельск', 'Россия']}
]


def filter_the_list(object: list) -> list:
    geo_logs_new = []
    for visits in geo_logs:
        for places in visits.values():
            if "Россия" in places:
                geo_logs_new.append(visits)
    return geo_logs_new


if __name__ == '__main__':

    for visits in filter_the_list(geo_logs):
        print(visits)