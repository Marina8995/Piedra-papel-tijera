import random

def turno_usuario():
    
    print("1.PIEDRA")
    print("2.PAPEL")
    print("3.TIJERA")
    usuario = int(input("Selecciona una opción: "))

    return usuario

   

def turno_maquina():
    maquina = random.choice([1, 2, 3])     
    return maquina
    
def play():

    opciones = {1: "PIEDRA", 2: "PAPEL", 3: "TIJERA"}
    
    
    veces_victoria_usuario = 0
    veces_victoria_maquina = 0

    while not (veces_victoria_usuario >= 3 or veces_victoria_maquina >= 3):   
        opcion_usuario=turno_usuario()
        opcion_maquina=turno_maquina()
        print(opciones[opcion_usuario], opciones [opcion_maquina]) 

        if opcion_usuario==opcion_maquina:
            print("Empate")
            
        elif opcion_usuario==1 and opcion_maquina==2:
            print("Has perdido")
            veces_victoria_maquina+=1
        elif opcion_usuario == 3 and opcion_maquina ==1:
            print("Has perdido")    
            veces_victoria_maquina+=1
        elif opcion_usuario == 2 and opcion_maquina == 3:  
            print("Has perdido") 
            veces_victoria_maquina+=1 
        
        else:
            print("Has ganado")
            veces_victoria_usuario+=1

    if veces_victoria_usuario == 3:
        print("Has ganado, fin de la partida")    

    if veces_victoria_maquina == 3:
        print("Has perdido, fin de la partida")        

    


play ()    

