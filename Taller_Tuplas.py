'''
Taller tuplas

Punto 1
'''
A=("Taller", "Algoritmos", "Programación",[2,9,2022])
print(A)
#1)
print(A[slice(0,3)])
#2)
print("Taller" in A)
#3)
print(A.index("Programación"))
#4)
print(len(A))
#5)
print(list(A))
''''
Punto 2
'''
#1)
a=int(input( "Ingres un Número: "))
b=int(input( "Ingres un Número: "))
c=int(input( "Ingres un Número: "))
d=a,b,c
print(d)
#2)
p1=d.index(a)
p2=d.index(b)
p3=d.index(c)

if p3%2 != 0:
    print(c)
elif p2%2 != 0:
    print(b)
elif p1%2 != 0:
    print(a)
#3)
Suma=sum(d)
print(Suma)
#4)
mini=min(d)
print(mini)

'''
Punto 3
'''

Usuario=("UsuarioEan")
Insertar_Usuario=input("Inserte Usuario: ")

if Insertar_Usuario != Usuario:
    respuesta= input("Este usuario no existe, por favor intente nuevamente: ")
    Insertar_Usuario
elif Insertar_Usuario==Usuario:
        print("Usuario reconocido")


Contraseña=("Uean2022")
Insertar_Contraseña=input("Inserte Contraseña: ")
if Insertar_Contraseña != Contraseña:
    respuesta= input("Contraseña incorrecta, por favor intente de nuevo: ")
    Insertar_Contraseña
elif Insertar_Contraseña==Contraseña:
    print("Contraseña correcta")
