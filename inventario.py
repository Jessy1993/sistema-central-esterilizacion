class Instrumental:
    """Representa un instrumental médico de la Central de Esterilización."""

    def __init__(self, nombre, stock=0):
        if not nombre.strip():
            raise ValueError("El nombre del instrumental es obligatorio")

        if stock < 0:
            raise ValueError("El stock inicial no puede ser negativo")

        self.nombre = nombre
        self.stock = stock

    def registrar_ingreso(self, cantidad):
        """Aumenta el stock cuando ingresa instrumental."""
        if cantidad <= 0:
            raise ValueError("La cantidad de ingreso debe ser mayor que cero")

        self.stock += cantidad
        return self.stock

    def registrar_salida(self, cantidad):
        """Disminuye el stock sin permitir cantidades negativas."""
        if cantidad <= 0:
            raise ValueError("La cantidad de salida debe ser mayor que cero")

        if cantidad > self.stock:
            raise ValueError("No existe suficiente instrumental disponible")

        self.stock -= cantidad
        return self.stock

    def consultar_stock(self):
        """Devuelve la cantidad disponible."""
        return self.stock
