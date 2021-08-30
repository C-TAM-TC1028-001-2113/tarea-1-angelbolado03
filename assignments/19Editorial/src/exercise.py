def main():
    # escribe tu código abajo de esta línea
    pass

import math
num_palabras = int(input('Dame el número de palabras: '))
num_paginas = math.ceil(num_palabras / 475)
total = (num_paginas * 60)
porcentaje = 90 * total / 100

print('El costo de la publicación es:', porcentaje)

if __name__ == '__main__':
    main()
