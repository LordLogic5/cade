#!/usr/bin/env python3

"""A short python example code being pulled and pushed onto
github"""

def main():

    inapprnames = ["Booger", "PototaHead", "L33tskillz", "Camp"]
    fname = input("Please enter in your first name: ")
    lname = input("Please enter in your last name:")
    usrname = input("Please enter in your 'appropiate' username: ")
    while usrname == inapprnames():
        usrname = input("Inappropiate name. \n Choose another: ")
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
