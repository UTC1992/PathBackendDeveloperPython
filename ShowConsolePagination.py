import os
from pynput import keyboard as kb


def paginar_dataframe(df, filas_por_pagina=10):
    """Muestra un DataFrame paginado en la consola"""
    total_filas = len(df)
    pagina_actual = 0
    total_paginas = (total_filas + filas_por_pagina - 1) // filas_por_pagina

    while True:
        # Limpiar consola (opcional)
        os.system('clear' if os.name == 'posix' else 'cls')

        # Calcular inicio y fin de la página
        inicio = pagina_actual * filas_por_pagina
        fin = min(inicio + filas_por_pagina, total_filas)

        # Mostrar datos de la página actual
        print(f"\n{'=' * 80}")
        print(f"Página {pagina_actual + 1} de {total_paginas} | Mostrando filas {inicio + 1}-{fin} de {total_filas}")
        print(f"{'=' * 80}\n")
        print(df.iloc[inicio:fin].to_string(index=False))
        print(f"\n{'=' * 80}")

        # Menú de navegación
        print("\n[N]ext | [P]revious | [Q]uit")
        opcion = input("Opción: ").lower()

        if opcion == 'n' and pagina_actual < total_paginas - 1:
            pagina_actual += 1
        elif opcion == 'p' and pagina_actual > 0:
            pagina_actual -= 1
        elif opcion == 'q':
            break


def paginar_con_flechas(df, filas_por_pagina=10):
    """Muestra un DataFrame paginado navegable con flechas del teclado"""
    pagina_actual = [0]  # Lista para modificar en closure
    total_paginas = (len(df) + filas_por_pagina - 1) // filas_por_pagina

    def mostrar_pagina():
        os.system('clear' if os.name == 'posix' else 'cls')
        inicio = pagina_actual[0] * filas_por_pagina
        fin = min(inicio + filas_por_pagina, len(df))

        print(f"\n{'=' * 80}")
        print(f"Página {pagina_actual[0] + 1} de {total_paginas} | Mostrando filas {inicio + 1}-{fin} de {len(df)}")
        print(f"{'=' * 80}\n")
        print(df.iloc[inicio:fin].to_string(index=False))
        print(f"\n{'=' * 80}")
        print("\n← → para navegar | ESC para salir")

    def on_press(key):
        try:
            if key == kb.Key.right and pagina_actual[0] < total_paginas - 1:
                pagina_actual[0] += 1
                mostrar_pagina()
            elif key == kb.Key.left and pagina_actual[0] > 0:
                pagina_actual[0] -= 1
                mostrar_pagina()
            elif key == kb.Key.esc:
                return False  # Detiene el listener
        except:
            pass

    mostrar_pagina()

    with kb.Listener(on_press=on_press) as listener:
        listener.join()


def paginar_ansi(df, filas_por_pagina=10):
    """Muestra un DataFrame paginado usando secuencias ANSI para actualizar en el mismo lugar"""
    pagina_actual = [0]
    total_paginas = (len(df) + filas_por_pagina - 1) // filas_por_pagina

    def limpiar_consola_ansi():
        """Limpia la consola usando secuencias ANSI"""
        print("\033[2J\033[H", end='')  # Limpia pantalla y mueve cursor al inicio

    def mostrar_pagina():
        limpiar_consola_ansi()
        inicio = pagina_actual[0] * filas_por_pagina
        fin = min(inicio + filas_por_pagina, len(df))

        print(f"\n{'=' * 80}")
        print(f"Página {pagina_actual[0] + 1} de {total_paginas} | Mostrando filas {inicio + 1}-{fin} de {len(df)}")
        print(f"{'=' * 80}\n")
        print(df.iloc[inicio:fin].to_string(index=False))
        print(f"\n{'=' * 80}")
        print("\n← → para navegar | ESC para salir")

    def on_press(key):
        try:
            if key == kb.Key.right and pagina_actual[0] < total_paginas - 1:
                pagina_actual[0] += 1
                mostrar_pagina()
            elif key == kb.Key.left and pagina_actual[0] > 0:
                pagina_actual[0] -= 1
                mostrar_pagina()
            elif key == kb.Key.esc:
                return False
        except:
            pass

    mostrar_pagina()

    with kb.Listener(on_press=on_press) as listener:
        listener.join()
