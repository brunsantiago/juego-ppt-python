jugador1 = input("Hola jugador 1 que eliges, Piedra, Papel o Tijera ?: ")
jugador2 = input("Hola jugador 1 que eliges, Piedra, Papel o Tijera ?: ")

if jugador1 == jugador2:
    print("Empate")
elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
    print("jugador 1 Ganador")
else:
    print("jugador 2 Ganador")