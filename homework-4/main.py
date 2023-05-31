from src.item import Item
from src.phone import Phone

if __name__ == '__main__':

    # смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2

    item1 = Item("Смартфон", 10_000, 20)
    assert (item1 + phone1).quantity == 25
    assert (phone1 + phone1).quantity == 10

    phone1.number_of_sim = 1
    try:
        Phone("iPhone 14", 120_000, 5, 0)
    except ValueError as e:
        assert str(e) == "Количество физических SIM-карт должно быть целым числом больше нуля."

