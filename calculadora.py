# calculadora.py
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

if __name__ == "__main__":
    print("Suma: ", suma(10, 5))
    print("Resta: ", resta(10, 5))
    print("Multiplicación: ", multiplicacion(10, 5))
    print("División: ", division(10, 5))
