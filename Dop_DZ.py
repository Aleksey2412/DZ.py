class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def добавить_товар(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен по цене {price}.")

    def удалить_товар(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def обновить_цену(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена на {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def получить_цену(self, item_name):
        return self.items.get(item_name, None)

    def список_товаров(self):
        if self.items:
            print("Список товаров:")
            for item_name, price in self.items.items():
                print(f"{item_name}: {price}")
        else:
            print("Список товаров пуст.")


store1 = Store("Магазин 1", "Адрес 1")
store2 = Store("Магазин 2", "Адрес 2")
store3 = Store("Магазин 3", "Адрес 3")

store1.добавить_товар("яблоко", 15.0)
store1.добавить_товар("банан", 10.0)
store2.добавить_товар("мир", 15.0)
store3.добавить_товар("книга '1984'", 10.0)

stores = [store1, store2, store3]

def выбрать_магазин():
    print("Выберите магазин:")
    for i, store in enumerate(stores, 1):
        print(f"{i}. {store.name} (Адрес: {store.address})")
    choice = int(input("Введите номер магазина: ")) - 1
    return stores[choice] if 0 <= choice < len(stores) else None

while True:
    выбранный_магазин = выбрать_магазин()
    if not выбранный_магазин:
        print("Некорректный выбор. Попробуйте снова.")
        continue

    print(f"Выбран магазин: {выбранный_магазин.name}")
    действие = input("Выберите действие (добавить, удалить, обновить, получить, список, выйти): ").strip().lower()

    if действие == "добавить":
        item_name = input("Введите название товара: ")
        price = float(input("Введите цену товара: "))
        выбранный_магазин.добавить_товар(item_name, price)
    elif действие == "удалить":
        item_name = input("Введите название товара для удаления: ")
        выбранный_магазин.удалить_товар(item_name)
    elif действие == "обновить":
        item_name = input("Введите название товара для обновления цены: ")
        new_price = float(input("Введите новую цену: "))
        выбранный_магазин.обновить_цену(item_name, new_price)
    elif действие == "получить":
        item_name = input("Введите название товара для получения цены: ")
        price = выбранный_магазин.получить_цену(item_name)
        if price is not None:
            print(f"Цена товара '{item_name}': {price}")
        else:
            print(f"Товар '{item_name}' не найден.")
    elif действие == "список":
        выбранный_магазин.список_товаров()
    elif действие == "выйти":
        print("Выход из программы.")
        break
    else:
        print("Некорректное действие. Попробуйте снова.")