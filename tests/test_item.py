"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item_init():
    item = Item("Телефон", 10_000, 20)
    assert item.name == "Телефон"
    assert item.price == 10_000
    assert item.quantity == 20


def test_item_add():
    item1 = Item("Телефон", 10_000, 20)
    item2 = Item("Наушники", 5_000, 30)
    result = item1.add(item2)
    assert result.quantity == item1.quantity + item2.quantity


def test_item_str():
    item = Item("Телефон", 10_000, 20)
    assert str(item) == "Телефон"


def test_item_repr():
    item = Item("Телефон", 10_000, 20)
    assert repr(item) == "Item('Телефон', 10000, 20)"


















# from src.item import Item, Phone
#
#
# def test_create_item():
#     item = Item("Смартфон", 10000, 20)
#     assert item.name == "Смартфон"
#     assert item.price == 10000
#     assert item.quantity == 20
#
#
# def test_repr():
#     item = Item("Смартфон", 10000, 20)
#     assert repr(item) == "Item('Смартфон', 10000, 20) "
#
#
# def test_add_item_and_phone():
#     item = Item("Смартфон", 10000, 20)
#     phone = Phone("iPhone 14", 120000, 5, 2)
#
#     assert item + phone == 25
#     assert phone + item == 25
#
#
# def test_add_item_and_item():
#     item1 = Item("Смартфон", 10000, 20)
#     item2 = Item("Ноутбук", 50000, 5)
#
#     assert item1 + item2 == 25































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
# def test_name_length():
#     item = Item('Телефон', 10000, 5)
#     item.name = 'Смартфон'
#     assert item.name == 'Смартфон'
#     try:
#         item.name = 'СуперСмартфон'
#     except Exception as e:
#         assert str(e) == 'Длина наименования товара превышает 10 символов.'
#
# def test_instantiate_from_csv():
#     Item.instantiate_from_csv("items.csv")
#     assert len(Item.all_items) == 6
#
# def test_string_to_number():
#     assert Item.string_to_number('5') == 5.0
#     assert Item.string_to_number('5.0') == 5.0
#     assert Item.string_to_number('5.5') == 5.5
#
# def test_item():
#     item1 = Item("Смартфон", 10000, 20)
#     item2 = Item("Ноутбук", 20000, 5)
#     assert item1.calculate_total_price() == 200000
#     assert item2.calculate_total_price() == 100000
#     Item.set_pay_rate(0.8)
#     item1.apply_discount()
#     assert item1.price == 8000.0
#     assert item2.price == 20000
#     assert Item.get_all_items() == [item1, item2]






















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