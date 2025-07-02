
reservas = {}

def mostrar_menu():
    print("TOTEM AUTOATENCIÓN RESERVA STRIKE")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas")
    print("3.- Cancelar reserva de zapatillas")
    print("4.- Salir")

def reservar_zapatillas():
    print("-- Reservar Zapatillas --")
    if len(reservas) >= 20:
        print("Ya se alcanzó el máximo de reservas (20).")
        return
    
    nombre = input("Nombre del comprador: ").strip()
    if nombre in reservas:
        print("El comprador ya tiene una reserva.")
        return

    clave = input("Digite la palabra secreta para confirmar la reserva: ")
    if clave != "EstoyEnListaDeReserva":
        print("Palabra secreta incorrecta. No se realizó la reserva.")
        return
    
    reservas[nombre] = 1
    print(f"Reserva realizada exitosamente para {nombre}.")

def buscar_reserva():
    print("-- Buscar Zapatillas Reservadas --")
    nombre = input("Nombre del comprador a buscar: ").strip()
    if nombre not in reservas:
        print("No se encontró ninguna reserva con ese nombre.")
        return
    
    pares = reservas[nombre]
    tipo = "VIP" if pares == 2 else "estándar"
    print(f"Reserva encontrada: {nombre} - {pares} par(es) ({tipo}).")

    if pares == 1:
        respuesta = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").lower()
        if respuesta == "s":
            reservas[nombre] = 2
            print(f"Reserva actualizada a VIP. Ahora {nombre} tiene 2 pares reservados.")
        else:
            print("Manteniendo reserva actual.")

def cancelar_reserva():
    print("-- Cancelar Reserva --")
    nombre = input("Nombre del comprador cuya reserva desea cancelar: ").strip()
    if nombre not in reservas:
        print("No se encontró ninguna reserva con ese nombre.")
    else:
        del reservas[nombre]
        print(f"La reserva de {nombre} ha sido cancelada.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            reservar_zapatillas()
        elif opcion == "2":
            buscar_reserva()
        elif opcion == "3":
            cancelar_reserva()
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

if __name__ == "__main__":
    main()
