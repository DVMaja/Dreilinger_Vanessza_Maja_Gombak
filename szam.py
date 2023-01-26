import random


def elso():
    vel_szam = random.randint(1, 50)

    print(f"I/A:\n\tA generált szám: {vel_szam}")

    print("I/B:")
    if (vel_szam % 5 == 0) and (vel_szam % 3 == 0):
        print("\tA szám öttel és hárommal is osztható!")
    elif vel_szam % 3 == 0:
        print("\tA szám hárommal  osztható")
    elif vel_szam % 5 == 0:
        print("\tA szám öttel osztható!")

