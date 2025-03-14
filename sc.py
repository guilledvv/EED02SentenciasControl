# Bifurcaion
'''
a = 50
if a%2 == 0: 
    print (f"El valor {a} es un numero par. ")
else:
    print (f"El valor {a} es un numero impar. ")


    if a>50:
        print (f"El valor {a} es un mayor de 50. ")
    elif a<50:
        print (f"El valor {a} es menor de 50. ")
    else:
        print (f"El valor {a} es 50. ")



num= input("Introduce un valor:")
print ("El valor introducido",num)# input siempre devuelve una cadena de caracteres

num=int (num)
a=0
while a<num:
    print("a:",a)
    a+=1




    #for
sum=0
for a in range(10):
    sum+=a
    print("a: ",a,",sum:",sum)

num = input(f"Dame un numero:")
num = int(num)

while num%2 !=0:
    num = input ("introduce otro numero que sea par:")
    num = int(num)
print(f"Numero final: {num}")


#bucle que solicite numeros al usuario hasta que se introduzcan 2 numeros pares consecutivos
ultimopar = None
dosparesseguidos = False


while not dosparesseguidos:
    try:
        num = int(input("Dame un numero:  "))

        if num % 2 == 0: #verifica si es par
            if ultimopar is not None:
                dosparesseguidos = True

            else:    
                ultimopar = num
        else:
            ultimopar = None


    except ValueError:
        print("Dame otro numero valido.")

print("¡Dos pares consecutivos!FIN.")
'''
def es_palindromo(texto):
    
    texto = texto.lower().replace(" ", "")
   
    return texto == texto[::-1]


frase = input("Ingresa una palabra o frase: ")


if es_palindromo(frase):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")




