"""
Main function (Login and Signup
"""
from authenticate import SignUp, LogIn
import menu


def main():
    """
    Main method contains login and signup features
    :return:
    """
    print("\n-----Welcome to MSS----- \n 1. Login \n 2. Signup")
    tryexit = 1
    choice = None
    while tryexit:
        try:
            choice = int(input("\nChoose 1/2: "))
            tryexit = 0
        except ValueError:
            print("Only choice 1 or 2 is allowed")
    if choice == 2:
        print("\n--Create Account--")
        signobj = SignUp(input("Username (Email): "), input("Password (Min. 8 characters): "))
        if signobj.usernameexist():
            if signobj.usernamevalidity() and signobj.passwordvalidity():
                signobj.saveindatabase()
                print("\nAccount Successfully created")
            else:
                print("Bad Username/Password, Check again")
        else:
            print("Account with this email already exists")

    if choice == 1:
        error = 1
        while error:
            print("\n--Log In--")
            loginobj = LogIn(input("Username:"), input("Password: "))
            print("---------")
            if loginobj.searchindatabase() == "Incorrect":
                print("\nWrong password")
            elif loginobj.searchindatabase() == 0:
                print("\nAccount doesn't exist")
            else:
                error = 0
                print("\nLogin Successful!")
                print("Redirecting...")
                menu.__menu__()


if __name__ == "__main__":
    main()
