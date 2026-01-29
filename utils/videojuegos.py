#!/usr/bin/env python3

juegos = ["Super Mario Bros", "Zelda: Breath of Wild", "Cyberpunk 2077", "Final Fantasy VII"]

limite = 500

# Generos
generos = {
        "Super Mario Bros": "Aventura",
        "Zelda: Breath of Wild": "Aventura",
        "Cyberpunk 2077": "Rol",
        "Final Fantasy VII": "Rol"
}

# Ventas y Stock
ventas_y_stock = {
    "Super Mario Bros": (400,200),
    "Zelda: Breath of Wild": (600,20),
    "Cyberpunk 2077": (60,120),
    "Final Fantasy VII": (924,3)
}

# Clientes
clientes = {
    "Super Mario Bros": {"Vladimyr", "Brayan", "Luigi", "Miguel", "Reatiga"},
    "Zelda: Breath of Wild": {"Brayan", "Luigi"},
    "Cyberpunk 2077": {"Vladimyr", "Miguel", "Reatiga"},
    "Final Fantasy VII": {"Brayan", "Miguel"}
}

def sumario(juego):
    # Sumario
    print(f"\n[i] Resumen del juego {juego}\n")
    print(f"\t[+] Genero del juego: {generos[juego]}")
    print(f"\t[+] Total de ventas para este juego: {ventas_y_stock[juego][0]} unidades")
    print(f"\t[+] Total de stock para este juego: {ventas_y_stock[juego][1]} unidades")
    print(f"\t[+] Clientes que han adquirido el juego: {', '.join(clientes[juego])}")

for juego in juegos:
    
    if ventas_y_stock[juego][0] > limite:
        sumario(juego)
        
ventas_totales = lambda: sum(ventas for juego, (ventas, _) in ventas_y_stock.items() if ventas_y_stock[juego][0] > limite)

print(f"\n[+] EL total de ventas de todos los productos ha sido de {ventas_totales()} productos")
