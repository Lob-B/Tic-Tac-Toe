def start_g():
    print("\tWelcome to my game!")
    z = ["X"]
    w = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    a = input("1st player name(O): ")
    b = input("2nd player name(X): ")
    check_g(a, b, z, w)


def check_g(a, b, z, w):
    if w[0] == w[1] == w[2] == "O" or w[0] == w[4] == w[8] == "O" or w[0] == w[3] == w[6] == "O" or w[1] == w[4] == w[
        7] == "O" or w[2] == w[5] == w[8] == "O" or w[3] == w[4] == w[5] == "O" or w[6] == w[7] == w[8] == "O" or w[
        2] == w[4] == w[6] == "O":
        show_g1(w)
        print("\n{} win the match!\n".format(a))
        return exit_g()
    elif w[0] == w[1] == w[2] == "X" or w[0] == w[4] == w[8] == "X" or w[0] == w[3] == w[6] == "X" or w[1] == w[4] == w[
        7] == "X" or w[2] == w[5] == w[8] == "X" or w[3] == w[4] == w[5] == "X" or w[6] == w[7] == w[8] == "X" or w[
        2] == w[4] == w[6] == "X":
        show_g1(w)
        print("\n{} win the match!\n".format(b))
        return exit_g()

    elif len(z) == 10:
        show_g1(w)
        print("This match is Draw\n")
        return exit_g()
    else:
        if z[-1] == "X" or z[0] == " ":
            y = a
        else:
            y = b

    return show_g(a, b, z, w, y)


def show_g(a, b, z, w, y):
    print("|-----|-----|-----|")
    print("|  {}  |  {}  |  {}  |".format(w[0], w[1], w[2]))
    print("|-----|-----|-----|")
    print("|  {}  |  {}  |  {}  |".format(w[3], w[4], w[5]))
    print("|-----|-----|-----|")
    print("|  {}  |  {}  |  {}  |".format(w[6], w[7], w[8]))
    print("|-----|-----|-----|")
    enter_g(a, b, z, w, y)


def show_g1(w):
    print("|-----|-----|-----|")
    print("|  {}  |  {}  |  {}  |".format(w[0], w[1], w[2]))
    print("|-----|-----|-----|")
    print("|  {}  |  {}  |  {}  |".format(w[3], w[4], w[5]))
    print("|-----|-----|-----|")
    print("|  {}  |  {}  |  {}  |".format(w[6], w[7], w[8]))
    print("|-----|-----|-----|")


def enter_g(a, b, z, w, y):
    while True:
        c = input("{},it's your turn. Choose your place carefully.: ".format(y))
        if c.isdigit == False or int(c) > 9 or int(c) < 1:
            print("Enter a valid number between 1-9")
        else:
            m = int(c) - 1
            if w[m] != " ":
                print("Place already filled!")
            break
    change_g(a, b, z, w, y, m)


def change_g(a, b, z, w, y, m):
    if y == b:
        z.append("X")
        w[m] = "X"
    else:
        z.append("O")
        w[m] = "O"
    check_g(a, b, z, w, )


def exit_g():
    while True:
        n = input("Do you want to play Again?(Y/N): ")
        if n == "Y" or n == "y":
            return start_g()
        elif n == "n" or n == "N":
            print("Thanks for Playing!!")
            break
        else:
            print("Enter correct input.")


start_g()
