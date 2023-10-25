def main():
    run = True
    while run:

        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        choice = input("Please enter an option: ")
        
        if choice == "1":
            encode()
        elif choice == "2":
            print()
        elif choice == "3":
            run = False


def encode():
    num = 0
    str1 = ""
    user_input = input("Please enter your password to encode: ")
    for i in user_input:
        num = int(i) + 3
        str1 = str1 + str(num)
    print("Your password has been encoded and stored!")
    print()
    return str1


if __name__ == "__main__":
    main()