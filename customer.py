class Customer:
    def __init__(self, name: str):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order._all_orders if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))
    
    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        orders = [order for order in Order._all_orders if order.coffee == coffee]
        if not orders:
            return None
        spending = {}
        for order in orders:
            spending[order.customer] = spending.get(order.customer, 0) + order.price
        max_spender = max(spending, key=spending.get)
        return max_spender
