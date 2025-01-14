"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import csv
from src.item import Item, InstantiateCSVError

@pytest.fixture
def items_csv(tmp_path):
    data = [("apple", 0.5, 10), ("banana", 0.4, 15), ("pear", 0.6, 7)]
    filepath = tmp_path / "items.csv"
    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    return filepath

def test_instantiate_from_csv(items_csv):
    Item.instantiate_from_csv(items_csv)
    assert len(Item.all) == 3
    assert Item.all[0].name == "apple"
    assert Item.all[0].price == 0.5
    assert Item.all[0].quantity == 10
    assert Item.all[1].name == "banana"
    assert Item.all[1].price == 0.4
    assert Item.all[1].quantity == 15
    assert Item.all[2].name == "pear"
    assert Item.all[2].price == 0.6
    assert Item.all[2].quantity == 7

def test_instantiate_from_csv_file_not_found(tmp_path):
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(tmp_path / "nonexistent.csv")
































# """Здесь надо написать тесты с использованием pytest для модуля item."""    # Дз_5
# from src.item import Item
#
# def test_item_creation():
#     item = Item('Book', 10.99, 5)
#     assert item.name == 'Book'
#     assert item.price == 10.99
#     assert item.quantity == 5
#
# def test_item_total_price():
#     item = Item('Book', 10.99, 5)
#     assert item.calculate_total_price() == 54.95
#
# def test_item_discount():
#     Item.pay_rate = 0.9
#     item = Item('Book', 10.99, 5)
#     item.apply_discount()
#     assert item.price == 9.891





# """Здесь надо написать тесты с использованием pytest для модуля item."""   Дз_4
# from src.item import Item
#
#
# def test_item_init():
#     item = Item("Телефон", 10_000, 20)
#     assert item.name == "Телефон"
#     assert item.price == 10_000
#     assert item.quantity == 20
#
#
# def test_item_add():
#     item1 = Item("Телефон", 10_000, 20)
#     item2 = Item("Наушники", 5_000, 30)
#     result = item1.add(item2)
#     assert result.quantity == item1.quantity + item2.quantity
#
#
# def test_item_str():
#     item = Item("Телефон", 10_000, 20)
#     assert str(item) == "Телефон"
#
#
# def test_item_repr():
#     item = Item("Телефон", 10_000, 20)
#     assert repr(item) == "Item('Телефон', 10000, 20)"






# """Здесь надо написать тесты с использованием pytest для модуля item.""" Дз_3
# from src.item import Item
#
# def test_item_repr():
#     item1 = Item("Смартфон", 10000, 20)
#     assert repr(item1) == "Item('Смартфон', 10000, 20)"
#
# def test_item_str():
#     item1 = Item("Смартфон", 10000, 20)
#     assert str(item1) == 'Смартфон'
#
#
#
#
#  """Здесь надо написать тесты с использованием pytest для модуля item.""" Дз_2
#  from src.item import Item
#
# def test_name_length():
#     item = Item('Телефон', 10000, 5)
#     item.name = 'Смартфон'
#     assert item.name == 'Смартфон'
#
#     try:
#         item.name = 'СуперСмартфон'
#     except Exception as e:
#         assert str(e) == 'Длина наименования товара превышает 10 символов.'
#
# def test_instantiate_from_csv():
#     Item.instantiate_from_csv()
#     assert len(Item.all_items) == 6
#
# def test_string_to_number():
#     assert Item.string_to_number('5') == 5.0
#     assert Item.string_to_number('5.0') == 5.0
#     assert Item.string_to_number('5.5') == 5.5









# """Здесь надо написать тесты с использованием pytest для модуля item.""" ДЗ_1
# from src.item import Item
#
#
# def test_item():
#     item1 = Item("Смартфон", 10000, 20)
#     item2 = Item("Ноутбук", 20000, 5)
#
#     assert item1.calculate_total_price() == 200000
#     assert item2.calculate_total_price() == 100000
#
#     Item.set_pay_rate(0.8)
#     item1.apply_discount()
#
#     assert item1.price == 8000.0
#     assert item2.price == 20000
#
#     assert Item.get_all_items() == [item1, item2]