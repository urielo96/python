def condicional_simple():
    x = 10
    if x > 5:
        print("x es mayor que 5")

def condicional_compuesto():
    y = 10
    z = 5
    if y > z:
        print("y es mayor que z")
    elif y == z:
        print("y es igual a z")
    else:
        print("y es menor que z")

def condicional_anidado(): 
    a = 10
    b = 5
    if a > b:
        print("a es mayor que b")
        if a > 2 * b:
            print("a es mucho mayor que b")

def condicionales_falsy():
    x = 0
    if not x:
        print("x es falsy")
    else:
        print("x es truthy")

condicionales_falsy()