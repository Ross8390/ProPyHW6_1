import pytest
from task_1 import filter_the_list


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

@pytest.mark.parametrize('geo_logs', geo_logs)
def test_len(geo_logs):
    result = filter_the_list(geo_logs)
    assert len(result) == 6, f'Длина {len(result)} не верна'

@pytest.mark.parametrize('geo_logs', geo_logs)
def test_find_Russia(geo_logs):
    result = filter_the_list(geo_logs)
    for visits in result:
         for places in visits.values():
            assert 'Россия' in places, 'Не найдено слово Россия'



if __name__ == '__main__':
    pytest.main()