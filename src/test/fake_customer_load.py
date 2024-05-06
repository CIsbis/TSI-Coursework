from src.user_logic.Customer import Customer


class FakeCustomerLoad:
    def load_customers(self):
        # Hardcoded customer data for testing
        raw_customer_data = [
            {"email": "john@example.com", "first_name": "John", "last_name": "Doe", "password": "password123"},
            {"email": "jane@example.com", "first_name": "Jane", "last_name": "Smith", "password": "password456"},
            # Add more sample customer data as needed
        ]

        # Convert raw data to Customer objects
        customers = [Customer(data) for data in raw_customer_data]
        return customers



# ***************NEEDS IMPLEMENTED***************
