def main():
    # escribe tu código abajo de esta línea
    saldo_anterior = float(input('Dame el saldo del mes anterior: '))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    numero_cheques = int(input("Dame el número de cheques: "))
    saldo = (saldo_anterior + ingresos - egresos - numero_cheques * 13)
    saldo_final = saldo - (saldo * 0.075)
    print("El saldo final de la cuenta es:", saldo_final)

if __name__ == '__main__':
    main()
