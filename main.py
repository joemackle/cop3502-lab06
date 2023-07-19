# Lab 06: Software Engineering
# Encoder / Decoder and Version Control
# First part coded by Joseph Mackle

def main():
    password = ""
    while True:  # looping menu
        print("Menu", "-------------", "1. Encode", "2. Decode", "3. Quit", sep="\n")
        choice = int(input("\nPlease enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            print(f'The encoded password is {password}, and the original password is {decode(password)}.')
        elif choice == 3:
            break
        else: print("Error: invalid option\n")


def encode(password):
    new_password = ""
    for i in range(len(password)):
        j = int(password[i]) + 3
        if j > 9: j -= 10
        new_password += str(j)
    return new_password


def decode(nums):
    deco = ''
    for i in nums:
        i = int(i)
        if i > 2:
            deco += str(i - 3)
        else:
            deco += str(i + 7)
    return deco


if __name__ == '__main__': main()
