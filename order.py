class Order:
    _all_orders = []

    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee
        if not isinstance(price, (float, int)) or price < 1.0 or price > 10.0:
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance.")
        self._customer = customer
        self._coffee = coffee
        self._price = float(price)
        self.__class__._all_orders.append(self)
        coffee._orders.append(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee
