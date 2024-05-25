class Departamento:
    """
    Clase que representa un departamento de una empresa.

    Atributos:
        nombre (str): El nombre del departamento.
        gerente (Gerente): El gerente del departamento.
        empleados ([Empleado]): Una lista de empleados del departamento.
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.gerente = None
        self.empleados = []

    def nombrar_gerente(self, gerente):
        """
        Nombra un gerente para el departamento.
        Este método recibe un objeto de tipo Gerente y lo asigna al atributo `gerente` del departamento.
        """
        self.gerente = gerente

    def agregar_empleado(self, empleado):
        """
        Agrega un empleado al departamento.
        Este método recibe un objeto de tipo Empleado y lo agrega a la lista `empleados` del departamento.
        """
        self.empleados.append(empleado)

    def agregar_empleados(self, empleados):
        """
        Agrega una lista de empleados al departamento.
        Este método recibe una lista de objetos de tipo Empleado y la agrega a la lista `empleados` del departamento.
        """
        self.empleados.extend(empleados)

    def calcular_nomina(self):
        """
        Calcula la nómina del departamento.
        Este método recorre la lista de empleados del departamento y suma sus salarios.
        El resultado se asigna al atributo `nomina` del departamento.
        """
        nomina = 0
        for empleado in self.empleados:
            nomina += empleado.salario
        self.nomina = nomina