
import os
import time

repeat = 1
while (repeat):
    print("\nType 1 for addition")
    print("Type 2 for subtraction")

    math = input("\n")
    if math == "1":
        anum1 = input("Please enter a number to continue: ")
        anum2 = input("Please enter another number to continue: ")
        answr = print(float(anum1) + float(anum2))
        repeat = 0
    elif math == "2":
        snum1 = input("Please enter a number to continue: ")
        snum2 = input("Please enter another number to continue: ")
        snswr = print(float (snum1) - float(snum2))
        repeat = 0
    else:
        print("Please enter either \"1\" or \"2\" and try again.")
        