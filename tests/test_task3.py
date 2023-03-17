import pytest
from task_3 import quantity_search


queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]


@pytest.mark.parametrize('queries', queries)
def test_on_dict(queries):
    result = quantity_search(queries)
    assert type(result) == dict, 'Результат не является словарем'
    assert  type(result) not in (int, float, tuple, list, set, str, bool)

@pytest.mark.parametrize('queries', queries)
def test_is_instance(queries):
    result = quantity_search(queries)
    for element in result.values():
        assert isinstance(element, int), f'Значения {element} не являются int'



if __name__ == '__main__':
    pytest.main()