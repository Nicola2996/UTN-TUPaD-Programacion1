usuariok='alumno'
claveok='python123'

intentos = 0



while intentos <3:
    usuario= input("Ingrese el usuario ").strip()
    clave = input ("Ingrese la clave ").strip()
    
    if usuariok==usuario and claveok==clave:
        print("Acceso concedido")
        break
    else:
        print("Datos incorrectos")
        intentos+=1
if intentos == 3:
    print ("Cuenta Bloqueada")

else:
    while True:
        print("Opcion 1)Estado  2)Cambiar Clave 3)Mensaje 4)Salir")
        opcion= input("Opcion").strip()

        if not opcion.isdigit():
            print("Ingrese numero valido")
            continue

        opcion= int(opcion)

        if not opcion in range(1,5) :
            print("Opcion inexistente")
            
            continue
        
        if opcion == 1:
            print("Inscripto")
            


        elif opcion == 2:
            nueva = input("Nueva clave: ").strip()

            if len(nueva) < 6:
                print("Error: mínimo 6 caracteres.")
                continue

            confirmar = input("Confirmar clave: ").strip()

            if nueva != confirmar:
                print("Error: las claves no coinciden.")
            else:
                claveok = nueva
                print("Clave actualizada correctamente.")

        
        
        elif opcion == 3:

            print ("Maquinaaaa segui asi!!")

        elif opcion == 4:
            print("Saliendo del sistema...")
            break




