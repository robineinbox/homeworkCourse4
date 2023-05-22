from src.item import Item

if __name__ == 'main':
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    try:
        item.name = 'СуперСмартфон'
    except Exception as e:
        assert str(e) == 'Длина наименования товара превышает 10 символов.'

    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all_items) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all_items[0]
    assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5.5
