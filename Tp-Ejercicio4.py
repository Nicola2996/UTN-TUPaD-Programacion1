energia = 100
tiempo = 12
cerradurasabiertas=0
alarma = False
codigoparcial=''
forzado=0
#inicializamos nombre del player con bucle while

agente=input('Ingrese su nombre Agente...:').strip()


while not agente.isalpha():
    print('Su nombre, sin numeros, Vamos de nuevo...')
    agente=input('Ingrese su nombre, Agente...:').strip()




while energia > 0 and tiempo > 0 and cerradurasabiertas < 3:  #MIENTRAS ESTO SE CUMPLA SIGUE EL JUEGO
    print(f'Bienvenido Agente: {agente} ')

    print(f'\n MENU ACCIONES:  ')
    print(f'Estado actual: ENERGIA: {energia}\n TIEMPO: {tiempo}\n Cerraduras abiertas {cerradurasabiertas}\n Alarma: {alarma}') 
    print(f"Turno 1")
    print(f"OPCIONES:\n 1) FORZAR CERRADURA \n 2) HACKEAR PANEL\n 3) DESCANSAR")
    
    opcionstr=input('Ingrese una accion...:1,2,o 3').strip()

    while not opcionstr.isdigit() or not int(opcionstr) in range (1,4):
        
        opcionstr=input('Ingrese una accion...:1,2,o 3').strip()
    opcionint=int(opcionstr)

    if opcionint == 1 :
        forzado+=1
        energia-=20
        tiempo-=2

        if  forzado == 3:
            alarma = True
            print("CERRADURA BLOQUEADA!!")
           
        

        if not alarma:
            if energia < 40:
                print("RIESGO DE ALARMA!!!")
                numerostr=input('RAPIDO ELIGE UN NUMERO ENTRE 1 y 3...').strip()
                while not numerostr.isdigit() or not int(numerostr) in range(1,4):
                    numerostr=input("ERROR. Ingrese numero 1-3: ").strip()
                numeroint=int(numerostr)
                if numeroint == 3:
                    print('PERDISTE EL JUEGO')
                    alarma = True
                else:
                    cerradurasabiertas += 1
                    print("Abriste la cerradura")
            else:
                cerradurasabiertas += 1
                print("Abriste la cerradura")


    elif opcionint ==2:
        forzado =0
        energia-=10
        tiempo-=3
        print("Hackeando cerradura...")
        for i in range(4):
            print(f'Progreso: {i+1}/4')
            codigoparcial+='A'
        if len(codigoparcial) >=8 and cerradurasabiertas <3:
            cerradurasabiertas+=1
            print("Hackeo completado!! Cerradura abierta")

    elif opcionint == 3:
        forzado = 0
        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1
          

        if alarma:
            energia -= 10
            print("\n Descansar con alarma activa consume energía extra")


    if alarma and tiempo <= 3 and cerradurasabiertas < 3:
        print("🚨 SISTEMA BLOQUEADO 🚨")
        break


# RESULTADO FINAL
print("\n--- RESULTADO ---")

if cerradurasabiertas == 3:
    print("🎉 ¡VICTORIA! Abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("💀 DERROTA. Te quedaste sin recursos.")
elif alarma and tiempo <= 3:
    print("🚨 DERROTA. Sistema bloqueado por alarma.")        


            




            

        














    




     

        





 





