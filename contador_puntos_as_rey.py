## Contador de puntos juego de cartas As al Rey.

# inicializamos los contadores de los participantes, en caso de más jugadores añadir más contadores.
contador_a = 0
contador_b = 0
rondas = ["AS", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# starter
print("¡¡Empieza la partida!!")

# comienza el bucle for.
for carta in rondas:
    print (f"\n -- RONDA DE LA CARTA {carta} --")
    puntos_a = int(input("Puntos de Jugador 1: "))
    contador_a = contador_a + puntos_a

    puntos_b = int(input("Puntos de Jugador 2: "))
    contador_b = contador_b + puntos_b

# salida del bucle al recorrer la lista rondas.
print(f"FIN DE LA PARTIDA, RESULTADO:\n Jugador 1: {contador_a} y Jugador 2: {contador_b}.")

# anunciamos el ganador.
if contador_a > contador_b:
    print("¡¡El ganador es el Jugador 1!!")
elif contador_a < contador_b:
    print("¡¡El ganador es el Jugador 2!!")
else:
    print("Empate!! tendréis que jugar la revancha!! :)")