class Empleado:
    """
    Clase que representa un empleado de una empresa.
    Atributos:
        nombres (str): Los nombres del empleado.
        apellidos (str): Los apellidos del empleado.
        cargo (str): El cargo del empleado.
        salario (int): El salario del empleado.
    """

    def __init__(self, nombres, apellidos, cargo, salario):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cargo = cargo
        self.salario = salario