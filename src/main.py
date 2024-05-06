from src.user_logic.LogIn import LogIn
from src.user_logic.Register import Register
from src.engine.game import run_game


def welcome():
    print("----------Welcome to Knots & Crosses!----------")
    verified = False

    while True:
        print("Press 1 to Log in:")
        print("Press 2 to Register:")
        print("Press 3 to Quit:")
        x = input("Enter your choice: ")

        if x == '1':
            if LogIn().log_in():
                verified = True
                break
        elif x == '2':
            Register("customer.csv").register()
        elif x == '3':
            break
        else:
            print("Invalid input. Please enter a number within the valid range.")

    return verified

def game_start():
    print("**********Welcome to Knots & Crosses!**********")
    run_game()

if __name__ == "__main__":
    verified = welcome()

    if verified:
        game_start()
