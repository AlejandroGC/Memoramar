import random

def crear_tableros(reng, col):
    return [[0] * col] * reng

def desplegar_tablero_jugador(tablero,juego, r1,c1,r2,c2):
    for iR in range(len(tablero)):
        for iC in range(len(tablero[iR])):
            print(f'{tablero[iR][iC]:>10}')
        #saltar de renglon
        print()
        
def desplegar(matriz):
    for iR in range(len(matriz)):
        for iC in range(len(matriz[iR])):
            print(f'{matriz[iR][iC]:>10}', end = ' ')
        #saltar de renglon
        print()

def inicializar_tablero(tablero):
    tablero = [["Tiburon","Estrella","Caballito","Ballena","Camaron","Cangrejo"],["Delfin","Langosta","Pulpo","Mantaraya","Medusa","Pez"],["Calamar","Tortuga","Anguila","Foca","Pinguino","Almeja"],["Tiburon","Estrella","Caballito","Ballena","Camaron","Cangrejo"],["Delfin","Langosta","Pulpo","Mantaraya","Medusa","Pez"],["Calamar","Tortuga","Anguila","Foca","Pinguino","Almeja"]]
    return tablero

def inicializar_juego(juego):
    juego = [[0,1,2,3,4,5],[6,7,8,9,10,11],[12,13,14,15,16,17],[18,19,20,21,22,23],[24,25,26,27,28,29],[30,31,32,33,34,35]]
    return juego

def leer_tiro(r1, c1, r2, c2, cj1, cj2, i, tablero, juego):
  
    # if para comparar si lo que esta en las cartas es igual
    if tablero[r1][c1] == tablero[r2][c2]:
        #cambiar de valor, la carta se volteo y asi se queda, porque son iguales.
        juego[r1][c1] = tablero[r1][c1]
        juego[r2][c2] = tablero[r2][c2]
        desplegar(juego)
        print("Obtuviste 1 punto!")
        # if para conocer a que jugador darle el punto
        return 1
        
    else:
        #guardar ambos valores iniciales para no perderlos
        guardar = juego[r1][c1]
        guardar2 = juego[r2][c2]
        #cambiar valores del juego por su contenido
        juego[r1][c1] = (tablero[r1][c1]) + "*"
        juego[r2][c2] = (tablero[r2][c2]) + "*"
        desplegar(juego)
        #Se regresa al valor original ya que las cartas no son iguales
        juego[r1][c1] = guardar
        juego[r2][c2] = guardar2
        return 0
    

def menu():
    return int(input('''
1. Iniciar juego memorama
2. Desplegar tablero inicial
3. Desplegar juego inicial
4. Desplegar tablero con cartas elegidas por el jugador
5. Leer las 2 cartas del jugador y mostrar las cartas que eligio
0. Salir
Teclea la opcion: '''))
    
def main():
    
    tablero = crear_tableros(6,6) # vista al usuario
    juego = crear_tableros(6,6)   # detras del juego
    
    print("Tablero")
    desplegar(tablero)
    print("\nJuego")
    desplegar(juego)
    
    

    #1. Inicialiar el el ciclo centinela
    opcion = menu()
    print("\n")
    
    while opcion != 0:
        if opcion == 1:
            #Puntaje
            cj1 = 0
            cj2 = 0
            
            #Seguir o no seguir
            resp = "si"
            
            #Titulo
            print("                          BIENVENIDO A MEMORAMAR!")
            
            #Inicializacion de las cartas
            #ADELANTE
            juego = inicializar_juego(juego)
            #ATRAS
            tablero = inicializar_tablero(tablero)
            print("\n")
            #Contador entre jugadores (Dice a quien le toca tirar).
            i = 1
            
            random.shuffle(tablero)
            
            while resp.lower() == "si" and cj1 + cj2 < 18:
                desplegar(juego)
                if i % 2 != 0:
                    print("Jugador 1")
                else:
                    print("Jugador 2")
                    
                num1 = int(input("Introduce el numero de tu primera carta: "))
                
                #obtener las posiciones de la primera carta   
                r1 = num1 // 6
                c1 = num1 % 6
    
                while num1 < 0 or num1 > 35 or juego[r1][c1] != num1:
                    num1 = int(input("La carta tiene que ser entre 1 y 35, y no puedes repetir: "))
                    r1 = num1 // 6
                    c1 = num1 % 6   
                    
                    
                num2 = int(input("Introduce el numero de tu segunda carta: "))
                #obtener las posiciones de la primera carta  
                r2 = num2 // 6
                c2 = num2 % 6
                
                #Verificar que la carta no sea repetida a los pares completos, entre 1 y 35
                while num2 < 0 or num2 > 35 or num2 == num1 or juego[r2][c2] != num2:
                    num2 = int(input("La carta no puedes ser igual a la anterior carta, o tiene que ser entre 1 y 35, y no puedes repetir: "))
                    r2 = num2 // 6
                    c2 = num2 % 6
 
                if i % 2 != 0:
                    guardar = leer_tiro(r1, c1, r2, c2, cj1, cj2, i, tablero, juego)
                    cj1 += guardar
                else:
                    guardar = leer_tiro(r1, c1, r2, c2, cj1, cj2, i, tablero, juego)
                    cj2 += guardar
                
                
                i = i + 1
                
                resp = input("Quieres seguir jugando, si o no? ")
            
            #Fuera del while significa que la persona no quizo continuar
            print("Se acabo el juego!")
            
            #Se imprime el marcador
            if cj1 > cj2:
                print(f'Gano el Jugador 1 formo {cj1} par(es).')
            elif cj2 > cj1:
                print(f'Gano el Jugador 2 formo {cj2} par(es).')
            else:
                print(f'Empate entre Jugadores hicieron {cj1} par(es).')
        
            input("Presiona enter para continuar...")
        
        elif opcion == 2:
            tablero = inicializar_tablero(tablero)
            desplegar(tablero)
        elif opcion == 3:
            juego = inicializar_juego(juego)
        else:
            opcion
    

        opcion = menu()

main()

    