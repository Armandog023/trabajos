numero = 4

def operation_addition(nuero2):
    return numero + nuero2

resultado2= operation_addition(2)


def rest (nuero2):
    return numero - nuero2

resultado=rest(2)

def mul (nuero2):
    return numero * nuero2

resultado3=mul(2)

def div (nuero2):
    return numero / nuero2

resultado4=div(2)

def res (nuero2):
    return numero % nuero2

resultado5=res(5)
 
def pot (nuero2):
    return numero ** nuero2

resultado6=pot(5)


print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)

num1=int (input('escribe un numero '))
num2=int (input('escribe otro numero '))
operacion= (input('que quieres hacer: 1-sumar, 2-restar, 3-multiplicar, 4-dividir '))

def opertation (num1, num2, operacion):
    if operacion == '1':
        return num1 + num2

    elif operacion == '2':
        return num1 - num2
    
    elif operacion == '3':
        return num1 * num2
    
    elif operacion == '4':
        return num1 / num2
    

resultado = opertation(num1, num2, operacion)
print (resultado)

