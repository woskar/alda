# Gruppe : Oskar Weinfurtner, Ulrich Prestel

import time


def ca_step(ca1, rule):
    ca2 = ""

    n = len(ca1)

    for i in range(0, n):
        key = ca1[max((i - 1), 0):min((i + 2), n)]
        cell = ca1[i]

        try:
            rule_value = rule[key]
            ca2 += rule_value
        except KeyError:

            # Keine Regel gefunden => Zelle wird einfach so uebernommen
            ca2 += cell

    return ca2


def elementary1():
    # Baum / Ast
    rule = {
        "** ": " ",
        " **": " ",
        "* *": "*",
        "*  ": "*"
    }
    ca1 = "  **  *   ** *      *"
    for i in range(0, 30):
        print(ca1)
        ca1 = ca_step(ca1, rule)


def elementary2():
    # Cooles Muster 1
    rule = {
        " **": " ",
        "** ": " ",
        "  *": "*",
        "*  ": "*"
    }
    ca1 = "       **       "
    for i in range(0, 30):
        print(ca1)
        ca1 = ca_step(ca1, rule)


def elementary3():
    # Cooles Muster 2
    rule = {
        " **": " ",
        "***": " ",
        "*  ": "*",
        "  *": "*",
    }
    ca1 = "    *   ***    *   "
    for i in range(0, 30):
        print(ca1)
        ca1 = ca_step(ca1, rule)


def elementary4():
    # Cooles Muster 3
    rule = {
        " **": " ",
        "** ": " ",
        "*  ": "*",
        "  *": "*",
        "* *": "*",
        "***": " "

    }
    ca1 = " *               * "
    for i in range(0, 30):
        print(ca1)
        ca1 = ca_step(ca1, rule)


def pingpong():
    rule = {
        " o-": "-",
        "o- ": " ",
        "-o ": "-",
        " -o": " ",
        "#o-": "o",
        "-o#": "o",
        "#o ": "-",
        " o#": "-",
        "#-o": " ",
        "o-#": " ",
        "  #": " ",
        "#  ": " ",
        "o  ": "o",
        "  o": "o",
        "o #": "o",
        "# o": "o",

    }
    ca1 = " #      o-    # "
    while True:
        print(chr(27) + "[2J")  # Falls man es in der Konsole ausfuehrt
        ca1 = ca_step(ca1, rule)
        print(ca1)
        time.sleep(0.1)


if __name__ == "__main__":
    #elementary4()
    # elementary3()
    # elementary2()
    # elementary1()
    pingpong()
