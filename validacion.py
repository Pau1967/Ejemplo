# calculadora.py
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: división entre cero"
    return a / b

print("Calculadora básica")
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
except ValueError: 
    print("Entrada inválida. Debes ingresar números.")
    exit()

operacion = input("Operación (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", suma(num1, num2))
elif operacion == "-":
    print("Resultado:", resta(num1, num2))
elif operacion == "*":
    print("Resultado:", multiplicacion(num1, num2))
elif operacion == "/":
    print("Resultado:", division(num1, num2))
else:
    print("Operación inválida")

   
