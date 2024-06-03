
"""constant"""
minimum_length = 8

"""main function"""


def main():
    password = get_password(minimum_length)


"""other functions"""

def get_password(minimum_length):
    password = input("Please enter your password: ")
    while len(password) < minimum_length:
        password = input(f"Please enter you password again with at least {minimum_length} characters: ")
    print('*' * len(password))


main()