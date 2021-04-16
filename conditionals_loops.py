
# Conditionals  <-----------------------------------------

a = 4 # Even
b = 3 # Impar

if a > b:
    print("A es mayor que B")
elif a < b:
    print("A es menor que B")
else:
    print("A es igual a B")

# a lot of conditionals

a = "piedra"
b = "papel"

if a == "piedra" and b == "piedra":
    print("Empate!")
elif a == "piedra" and b == "papel":
    print("Gana B!")
elif a == "piedra" and b == "tijera":
    print("Gana A!")
elif a == "papel" and b == "piedra":
    print("Gana A!")
elif a == "papel" and b == "papel":
    print("Empate!")
elif a == "papel" and b == "tijera":
    print("Gana B!")
elif a == "tijera" and b == "piedra":
    print("Gana B!")
elif a == "tijera" and b == "papel":
    print("Gana A!")
elif a == "tijera" and b == "tijera":
    print("Empate!")

# nested conditionals

a = "piedra"
b = "papel"

if a == "piedra":
    if b == "piedra":
        print("Empate!")
    elif b == "papel":
        print("Gana B!")
    else:
        print("Gana A!")
elif a == "papel":
    if b == "piedra":
        print("Gana A!")
    elif b == "papel":
        print("Empate!")
    else:
        print("Gana B!")
else:
    if b == "piedra":
        print("Gana B!")
    elif b == "papel":
        print("Gana A!")
    else:
        print("Empate!")

# Loops  <-----------------------------------------
