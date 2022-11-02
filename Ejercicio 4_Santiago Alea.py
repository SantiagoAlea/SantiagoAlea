#Bucle para mesclar operadores logicos y que imprima un resultado condicional

#x=input()
#if(type(x) is int):
    #print("Es entero")
    #if(x>0):
     #   print("x es mayor que 0")
    #elif(x==0):
     #   print("x es igual a 0")
    #else:
     #   print("x es menor que 0")
#else:
  #  print("x no es entero")



  #Bucle para definir notas
print("Ingrese su nota")
n=int(input())

if n>=60:
    print("Pasaste")
else:
    print("Perdiste")
    print("Te falto ", (60-n))
