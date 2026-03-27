class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def get_total(self):
        return sum(
            item["product"].price * item["quantity"] for item in self.items
        )

    def show_cart(self):
        if not self.items:
            print("Корзина пуста")
            return
        print("Корзина:")
        for item in self.items:
            p = item["product"]
            print(f"  {p.name} x{item['quantity']} = "
                  f"{p.price * item['quantity']} руб.")
        print(f"Итого: {self.get_total()} руб.")


p1 = Product("Ноутбук", 50000)
p2 = Product("Мышь", 1500)

cart = Cart()
cart.add_product(p1)
cart.add_product(p2, 2)
cart.show_cart()
