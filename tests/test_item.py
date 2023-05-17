"""Здесь надо написать тесты с использованием pytest для модуля item."""
def test_item():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

    Item.set_pay_rate(0.8)
    item1.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 20000

    assert Item.get_all_items() == [item1, item2]


class Item:
    pay_rate = 1
    all_items = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all_items.append(self)

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate

    @classmethod
    def set_pay_rate(cls, pay_rate):
        cls.pay_rate = pay_rate

    @classmethod
    def get_all_items(cls):
        return cls.all_items
