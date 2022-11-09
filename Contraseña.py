contraseña= input("800000-00000-0000-100-90-5: ")
contraseña2= "800195"
 
while contraseña != contraseña2:
    respuesta = input("Contraseña incorrecta ¿desea intentarlo nuevamente? (si/no) ")
    if respuesta == "si":
        contraseña= input("800000-00000-0000-100-90-5: ")
    else:
        break
 
if contraseña == contraseña2:
    print("Bienvenido al sistema")
for I in (1,4,1):
    print("Estudiante ", I)
    print("dame tus notas")
    nota1,I=input("primera nota ")
    nota2,I=input("segunda nota ")
    nota3,I=input("tercera nota ")
    nota4,I=input("cuarta nota ")
    Nota=float((nota1+nota2+nota3+nota4)/4)

    if Nota>=60:
        print("pasaste")
    else:
        print("perdiste")
        print("te falto ", 60-Nota)

    while Nota>= 60:
        if Nota==60:
            print("Por la minima!")
        elif Nota==80:
            print("Bine hecho!")
        elif Nota==100:
            print("Excelente!!!")
        else:
            print("Bien")
    Nota=Nota-Nota


