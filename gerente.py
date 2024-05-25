from .empleado import Empleado

class Gerente(Empleado):
    """
    Clase que representa un gerente de una empresa.
    Herencia:
        Empleado: La clase Gerente hereda de la clase Empleado.
    Atributos:
        calcular_salario(): int: Este método calcula el salario del gerente.
    """

    def calcular_salario(self):
        """
        Calcula el salario del gerente.

        Este método devuelve el salario del gerente, que se calcula como el salario base más un bono.
        El bono del gerente es un porcentaje del salario base.
        """
        bono = self.salario * 0.1
        salario_total = self.salario + bono
        return salario_total