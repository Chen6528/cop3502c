

def main():
    run = True
    password = ""
    while run:

        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        choice = input("Please enter an option: ")
        
        if choice == "1":
            password = encode()
        elif choice == "2":
            decode(password)
        elif choice == "3":
            run = False


def encode():
    num = 0
    str1 = ""
    user_input = input("Please enter your password to encode: ")
    for i in user_input:
        num = (int(i) + 3)%10
        str1 = str1 + str(num)
    print("Your password has been encoded and stored!")
    print()
    return str1


def decode(password):
    # hugo's code
    encoded = password
    decoded = ""
    for n in password:
        decoded += str((int(n)+7)%10)
    print(f"The encoded password is {encoded}, and the original password is {decoded}.\n")


if __name__ == "__main__":
    main()