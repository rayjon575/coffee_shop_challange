import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_name_property(self):
        customer = Customer("John")
        self.assertEqual(customer.name, "John")
        customer.name = "Jane"
        self.assertEqual(customer.name, "Jane")
        with self.assertRaises(ValueError):
            customer.name = ""
        with self.assertRaises(ValueError):
            customer.name = "a" * 16

    def test_orders_and_coffees(self):
        customer = Customer("Alice")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Latte")
        order1 = Order(customer, coffee1, 3.5)
        order2 = Order(customer, coffee2, 4.0)
        self.assertIn(order1, customer.orders())
        self.assertIn(order2, customer.orders())
        self.assertIn(coffee1, customer.coffees())
        self.assertIn(coffee2, customer.coffees())

    def test_create_order(self):
        customer = Customer("Bob")
        coffee = Coffee("Mocha")
        order = customer.create_order(coffee, 5.0)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 5.0)

    def test_most_aficionado(self):
        customer1 = Customer("Carl")
        customer2 = Customer("Dana")
        coffee = Coffee("Americano")
        Order(customer1, coffee, 4.0)
        Order(customer2, coffee, 6.0)
        self.assertEqual(Customer.most_aficionado(coffee), customer2)

if __name__ == "__main__":
    unittest.main()
