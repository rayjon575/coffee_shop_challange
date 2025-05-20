import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def test_order_creation(self):
        customer = Customer("Jane")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 2.5)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 2.5)

    def test_price_validation(self):
    customer = Customer("John")
    coffee = Coffee("Espresso")
    # Ensure the price is within the valid range
    with self.assertRaises(ValueError):
        Order(customer, coffee, 0.5)  # Too low
    with self.assertRaises(ValueError):
        Order(customer, coffee, 11.0)  # Too high
    with self.assertRaises(TypeError):
        Order(customer, coffee, "free")  # Invalid price type (string)

    def test_customer_and_coffee_type_validation(self):
        coffee = Coffee("Mocha")
        with self.assertRaises(TypeError):
            Order("not a customer", coffee, 5.0)
        customer = Customer("Alice")
        with self.assertRaises(TypeError):
            Order(customer, "not a coffee", 5.0)

if __name__ == "__main__":
    unittest.main()
