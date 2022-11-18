

print("__________________________________________________")
print("Insertar nombre:")
Nombre=input()
while Nombre=="":
    print("Nombre no valido")
    Nombre=input()        
print("Ingresar edad")
Edad=int(input())
while Edad=="" or Edad<10:
    print("Edad no valida, debe ser mayor a 10")
    Edad=int(input())
print("Ingrsar usuario")
Usuario=str(input())
print("Ingrese contraseña")
Contraseña1=input()
print("Confirmar contraseña")
Contraseña_Confirmar=input()
while Contraseña_Confirmar != Contraseña1:
    print("No hay coincidencia")
    Contraseña_Confirmar=input()
else:
    print("_____________________________________________")
    print("Ingresar usuario")
    Usuario_Ingresado=input()
    while Usuario_Ingresado !=Usuario:
        print("Usuario no encontrado")
        print("Ingrese usuario")
        Usuario_Ingresado=input()
    else:  
        print("Ingrese la contraseña")
        Contraseñaingresada=input()
        while Contraseñaingresada != Contraseña1:
            print("Contraseña incorrecta")
            Contraseñaingresada=input()
            
        else:
            Datos={"Nombre": Nombre,  "Edad": Edad, "Usuario": Usuario, "Contraseña": Contraseña1}
            print("__________________________________")
            print("Bienvenido ",Nombre)            
            print("Que desea hacer?")
            Opciones=input("-Ver datos  -Salir: ")
            if Opciones=="Ver datos":
                print(Datos)
            elif Opciones=="Salir":
                print("Hasta la proxima")
        
