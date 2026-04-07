lunes1=""
lunes2=""
lunes3=""
lunes4=""

martes1=""
martes2=""
martes3=""

operador = input("Ingrese el nombre del operador: ").strip()
while not operador.isalpha():
    print("Error: Ingrese un nombre que solo contengan letras.")
    operador = input("Ingrese el nombre del operador: ").strip()

while True:
       print("1. Reservar turno. ") 
       print("2. Cancelar turno.  ")
       print("3. Ver agenda. ")
       print("4. Ver resumen general.")
       print("5. Salir del sistema.")
       opcionstr = input("Seleccione una de las opciones dadas:  ").strip()
       if not opcionstr.isdigit() or int(opcionstr) == 0:
            print("Error: Ingrese el numero de opcion valido")
            continue
       opcionint= int(opcionstr)
       if not opcionint in range (1,6):
            print("Error: No es un numero valido de opciones")
            continue
       if opcionint == 1:
           dia= input("Elija el dia, 1 para Lunes o 2 para Martes:  ").strip()
           if not dia.isdigit() or int(dia) == 0:
                print("Ingrese un numero valido, 1 o 2")
                continue
           diaint= int(dia)
           if not diaint in range(1,3):
                print("Ingrese un numero valido, 1 o 2")
                continue
           paciente= input("Ingrese el nombre del paciente:  ").lower().strip()
           if not paciente.isalpha():
            print("Error: Ingrese un nombre que contenga solo letras")
            paciente= input("Ingrese el nombre del paciente:  ").lower().strip()
            continue
           if diaint == 1:
                if paciente in (lunes1, lunes2, lunes3, lunes4):
                    print("Ya existe el nombre indicado")
                elif lunes1 == "": lunes1 = paciente
                elif lunes2 == "": lunes2 = paciente
                elif lunes3 == "": lunes3 = paciente
                elif lunes4 == "": lunes4 = paciente
                else: print("Lunes completo, no hay mas lugar")
           else:
                if paciente in (martes1, martes2, martes3):
                    print("Ya existe el nombre indicado")
                elif martes1 == "": martes1 = paciente
                elif martes2 == "": martes2 = paciente
                elif martes3 == "": martes3 = paciente
                else: print("Martes completo, no hay mas lugar")
       elif opcionint == 2:
           dia= input("Elija el dia, 1 para Lunes o 2 para Martes:  ").strip()
           if not dia.isdigit() or int(dia) == 0:
                print("Ingrese un numero valido, 1 o 2")
                continue
           diaint= int(dia)
           if not diaint in range(1,3):
                print("Ingrese un numero valido, 1 o 2")
                continue
           paciente= input("Ingrese el nombre del paciente:  ").lower().strip()
           if not paciente.isalpha():
            print("Error: Ingrese un nombre que contenga solo letras")
            paciente= input("Ingrese el nombre del paciente:  ").lower().strip()
            continue
           ok = False
           if diaint == 1:
                if lunes1 == paciente: lunes1 = ""; ok=True
                elif lunes2 == paciente: lunes2 = ""; ok=True
                elif lunes3 == paciente: lunes3 = ""; ok=True
                elif lunes4 == paciente: lunes4 = ""; ok=True
           else:
                if martes1 == paciente: martes1 = ""; ok=True
                elif martes2 == paciente: martes2 = ""; ok=True
                elif martes3 == paciente: martes3 = ""; ok=True
           print("Su turno a sido cancelado" if ok else "Paciente no encontrado")
       elif opcionint == 3:
            dia= input("Elija el dia, 1 para Lunes o 2 para Martes:  ").strip()
            if not dia.isdigit() or int(dia) == 0:
                print("Ingrese un numero valido, 1 o 2")
                continue
            diaint= int(dia)
            if not diaint in range(1,3):
                print("Ingrese un numero valido, 1 o 2")
                continue

            if diaint == 1:
                print("1:", lunes1 or "(Turno liberado)")
                print("2:", lunes2 or "(Turno liberado)")
                print("3:", lunes3 or "(Turno liberado)")
                print("4:", lunes4 or "(Turno liberado)")
            else:
                print("1:", martes1 or "(Turno liberado)")
                print("2:", martes2 or "(Turno liberado)")
                print("3:", martes3 or "(Turno liberado)")
       elif opcionint == 4:
           cantidadturnoslunes=0
           if lunes1 != "": cantidadturnoslunes += 1
           if lunes2 != "": cantidadturnoslunes += 1
           if lunes3 != "": cantidadturnoslunes += 1
           if lunes4 != "": cantidadturnoslunes += 1
           cantidadturnosmartes=0
           if martes1 != "": cantidadturnosmartes += 1
           if martes2 != "": cantidadturnosmartes += 1
           if martes3 != "": cantidadturnosmartes += 1
           print(f"La cantidad de turnos dados el dia lunes es: {cantidadturnoslunes}, y {4- cantidadturnoslunes} libres ")
           print(f"La cantidad de turnos dados el dia martes es: {cantidadturnosmartes}, y {3 - cantidadturnosmartes} libres ")
       elif opcionint == 5:
            print("Usted esta saliendo del sistema...!!")
            break


       

                 
