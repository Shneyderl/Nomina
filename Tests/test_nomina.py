import unittest

from empresa import Empresa
from departamento import Departamento
from empleado import Empleado
from gerente import Gerente

class TestEmpresa(unittest.TestCase):

    def test_crear_empresa(self):
        empresa = Empresa("Mi empresa")
        self.assertEqual(empresa.nombre, "Mi empresa")
        self.assertEqual(empresa.departamentos, [])

    def test_agregar_departamento(self):
        empresa = Empresa("Mi empresa")
        departamento_informatica = Departamento("Informática")
        empresa.departamentos.append(departamento_informatica)
        self.assertEqual(len(empresa.departamentos), 1)
        self.assertEqual(empresa.departamentos[0].nombre, "Informática")

    def test_calcular_nomina(self):
        empresa = Empresa("Mi empresa")
        departamento_informatica = Departamento("Informática")
        gerente_informatica = Gerente("Juan", "Pérez", "Gerente de Informática", 5000000)
        departamento_informatica.nombrar_gerente(gerente_informatica)
        empleado1 = Empleado("María", "Gómez")