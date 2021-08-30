def main():
    # escribe tu código abajo de esta línea

    gramos_de_harina = float(input('Dame la harina en gramos: '))
    gramos_levadura = round(((gramos_de_harina / 1000) * 50), 1)

print('Necesitas estos gramos de levadura:', gramos_levadura)

if __name__ == '__main__':
    main()
