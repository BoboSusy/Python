def switch(operace):
    if operace == "+":
        return print("Vysledek: ", a + b)
    elif operace == "-":
        return print("Vysledek: ", a - b)
    elif operace == "/":
        return print("Vysledek: ", a / b)
    elif operace == "*":
        return print("Vysledek: ", a * b)
    elif operace == "pow":
        return print("Vysledek: ", a ** b)

while True:
    print("Zadej prvni cislo: ")
    a = int(input())
    print("Zadej druhe cislo: ")
    b = int(input())
    print("Vyber oberaci: /,*,-,+,pow")
    operace = input()

    switch(operace)
    print("Chcete pokracovat napiste: \"ano\" \"ne\"")
    if (input() == "ne"):
        break