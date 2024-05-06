def get_valid_input(prompt, valid_range):
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            else:
                print("Invalid input. Please enter a number within the valid range.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
