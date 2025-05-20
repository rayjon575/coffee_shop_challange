import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    def test_name_property(self):
        coffee = Coffee("Espresso")
        self.assertEqual(coffee.name, "Espresso")
        with self.assertRaises(ValueError):
            Coffee("ab")

    def test_orders_and_customers(self):
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        coffee = Coffee("Latte")
        order1 = Order(customer1, coffee, 3.5)
        order2 = Order(customer2, coffee, 4.0)
        self.assertIn(order1, coffee.orders())
        self.assertIn(order2, coffee.orders())
        self.assertIn(customer1, coffee.customers())
        self.assertIn(customer2, coffee.customers())

    def test_num_orders_and_average_price(self):
        coffee = Coffee("Mocha")
        self.assertEqual(coffee.num_orders(), 0)
        self.assertEqual(coffee.average_price(), 0)
        customer = Customer("Carl")
        Order(customer, coffee, 5.0)
        Order(customer, coffee, 7.0)
        self.assertEqual(coffee.num_orders(), 2)
        self.assertAlmostEqual(coffee.average_price(), 6.0)

if __name__ == "__main__":
    unittest.main()
