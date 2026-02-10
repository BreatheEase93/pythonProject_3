from unittest.mock import patch

from srs.utils import read_json


def test_read_json():
    """Тест read_json, для файла по умолчанию"""
    result = read_json()
    assert len(result) == 2
    assert result[0][0].name == "Смартфоны"
    assert result[0][0].product_count == 7


def test_read_json_fail():
    """Тест read_json, ошибки файла"""
    assert read_json("sadasfaf") == ([], [])


def test_general_io_error():
    """Мок для общей ошибки ввода-вывода"""
    with patch('builtins.open', side_effect=IOError("Диск не доступен")):
        categories, products = read_json("file.json")

        assert categories == []
        assert products == []
