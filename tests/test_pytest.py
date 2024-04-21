import pytest
import requests

from main import discriminant, solution, get_name, get_directory, add


@pytest.mark.parametrize(
    'a, b, c, expected',
    (
            [0, 5, 5, 25],
            [5, 7, 12, -191],
            [-5, 7, 2, 89],
            [5, -7, -2, 89],
    )
)
def test_discriminant(a, b, c, expected):
    actual = discriminant(a, b, c)
    assert actual == expected


@pytest.mark.parametrize(
    'a, b, c, expected',
    (
            [1, 8, 15, [-3.0, -5.0]],
            [1, -13, 12, [12.0, 1.0]],
            [-4, 28, -49, 3.5],
            [1, 1, 1, "корней нет"],
    )
)
def test_solution(a, b, c, expected):
    actual = solution(a, b, c)
    assert actual == expected


@pytest.mark.parametrize(
    'doc_number, expected',
    (
            ["10006", "Аристарх Павлов"],
            ["101", "Документ не найден"],
    )
)
def test_get_name(doc_number, expected):
    actual = get_name(doc_number)
    assert actual == expected


@pytest.mark.parametrize(
    'doc_number, expected',
    (
            ["11-2", "1"],
            ["311 020203", "3"],
            ["1544", "Полки с таким документом не найдено"],
    )
)
def test_get_directory(doc_number, expected):
    actual = get_directory(doc_number)
    assert actual == expected


@pytest.mark.parametrize(
    'document_type, number, name, shelf_number, expected',
    (
            ["international passport", "311 020203", "Александр Пушкин", 3, True],

    )
)
def test_add(document_type, number, name, shelf_number, expected):
    actual = add(document_type, number, name, shelf_number)
    assert actual == expected


class TestYandexDisk:
    def setup_method(self):
        self.headers = {'Authorization': 'your_token'}

    def test_creat_folder(self):
        params = {'path': 'Image101'}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)

        assert response.status_code == 201

    def test_creat_folder_again(self):
        params = {'path': 'Image101'}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)

        assert response.status_code == 409
