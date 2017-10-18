#!/usr/bin/env python3

"""A short python example code being pulled and pushed onto
github"""

def main():


    setpass = input("Please create your password")
    password = input("Please enter in your password: ")

    count = 5;
    while password != setpass and count > 0:
        print("You have entered in the wrong password!\n")
        print("You have %d tries left" % count)
        count -= 1
        password = input("Please enter it in again: ")
    if count == 0:
        print("You are temporarily blocked from entering your password")
    else:
        print("Yay you entered the correct password!")


if __name__ == "__main__":
    main()
