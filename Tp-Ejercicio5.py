print("BIENVENIDO A LA ARENA!!!")

nombre=input("Ingrese el nombre del gladiador:  ").strip()
vida_gladiador=100
vida_enemigo=100
pociones_vida=3
dano_gladiador= 15
dano_enemigo= 12
danorafaga=5
turnogladiador=True
critico=22.5


while not nombre.isalpha():
    print("Nombre invalido (solo letras)")
    nombre=input("Ingrese el nombre del gladiador:  ").strip()




while vida_gladiador >0 and vida_enemigo > 0 :
        
        
            
        print("==ESTADO ACTUAL==")
        print(f"Gladiador: {nombre} HP: {vida_gladiador} vs Enemigo HP: {vida_enemigo}")
        
       

        
        if turnogladiador:
            print("==INICIO DEL COMBATE==")
            print(f"Gladiador: {nombre} HP: {vida_gladiador} vs Enemigo HP: {vida_enemigo}")
        
            print("1. ATAQUE PESADO")
            print("2. RAFAGA VELOZ")
            print("3. CURAR")
            accion=input("Elige accion: ").strip()
            
            while not accion.isdigit() or not int(accion) in range(1,4):
                print("Accion invalida...")
                accion=input("Elige accion: ").strip()
                
            accionint=int(accion)
                


            if accionint == 1:
                    
                print("ATAQUE PESADOOO!!")
                    
                    
                if vida_enemigo < 20:
                    
                
                    vida_enemigo -= critico
                    print("CRITICAL HIT!!")

                    print(f"¡Atacaste al enemigo por {critico} puntos de daño!")
                else:
                    
                    vida_enemigo = vida_enemigo - dano_gladiador

                    print(f"¡Atacaste al enemigo por {dano_gladiador} puntos de daño!")
                    
            
            elif accionint ==2:
                print("RAFAGAAAAA!!")
                for i in range (3):
                        
                    print(f"Golpe conectado por {danorafaga}")
                    vida_enemigo-=danorafaga
                    
                        
            elif accionint==3:
                print("CURACION!!")
                
                
                if pociones_vida > 0:
                    pociones_vida -=1
                    vida_gladiador += 30

                    if vida_gladiador >=100:
                        
                            vida_gladiador=100

                    
                else:
                    print("SIN POCIONES!!!")
                 
        else:
      
            print("\n-- TURNO DEL ENEMIGO --")

        if vida_enemigo > 0:
            vida_gladiador -= dano_enemigo
            print("¡El enemigo te atacó por", dano_enemigo, "de daño!")
        else:
            print("HAS DERROTADO A TU ENEMIGO")

  
          


print("\n--- FIN DEL JUEGO ---")

if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
    print(f"Terminaste con {vida_gladiador} puntos de vida")
else:
    print(f"DERROTA. {nombre} Has caído en combate.")
    print(f"El enemigo quedo con {vida_enemigo} puntos de vida")


        
