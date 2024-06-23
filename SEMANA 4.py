# sistema_reservas.py

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False

    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            print(f'Habitación {self.numero} reservada.')
        else:
            print(f'Habitación {self.numero} ya está ocupada.')

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            print(f'Habitación {self.numero} liberada.')
        else:
            print(f'Habitación {self.numero} ya está libre.')


class Cliente:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def __str__(self):
        return f'{self.nombre} (DNI: {self.dni})'


class Reserva:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente
        self.habitacion = habitacion

    def confirmar(self):
        self.habitacion.reservar()

    def cancelar(self):
        self.habitacion.liberar()


# Ejemplo de uso
if __name__ == "__main__":
    # Crear algunas habitaciones
    habitacion1 = Habitacion(101, 'Individual', 50)
    habitacion2 = Habitacion(102, 'Doble', 80)

    # Crear un cliente
    cliente1 = Cliente('Juan Pérez', '12345678X')

    # Crear una reserva
    reserva1 = Reserva(cliente1, habitacion1)
    reserva1.confirmar()  # Reserva la habitación 101
    reserva1.cancelar()   # Libera la habitación 101
