from src.user_logic.Customer import Customer


class FakeCustomerLoad:
    def load_customers(self):
        raw_customer_data = [
            {"email": "john@example.com", "first_name": "John", "last_name": "Doe", "password": "password123"},
            {"email": "jane@example.com", "first_name": "Jane", "last_name": "Smith", "password": "password456"},
        ]

        customers = [Customer(data) for data in raw_customer_data]
        return customers



# ***************NEEDS IMPLEMENTED***************
