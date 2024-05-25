class Empresa:
    """
    Clase que representa una empresa.

    Atributos:
        nombre (str): El nombre de la empresa.
        departamentos ([Departamento]): Una lista de departamentos de la empresa.
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.departamentos = []

    def calcular_nomina(self):
        """
        Calcula la nómina de la empresa.

        Este método recorre cada departamento de la empresa y calcula la nómina de cada uno.
        La nómina de un departamento se calcula sumando los salarios de todos sus empleados.
        """
        for departamento in self.departamentos:
            departamento.calcular_nomina()