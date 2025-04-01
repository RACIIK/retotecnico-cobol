import unittest
from procesamiento import Transaccion, ProcesadorTransacciones  # Importa las clases

class TestProcesadorTransacciones(unittest.TestCase):

   def setUp(self):
        """ Configura un conjunto de datos de prueba antes de cada prueba. """
        self.procesador = ProcesadorTransacciones(archivo_csv="")  # No se carga un archivo real

        # Creamos transacciones de prueba manualmente
        self.procesador.transacciones = [
            Transaccion("T001", "Crédito", 1500.0),
            Transaccion("T002", "Débito", 500.0),
            Transaccion("T003", "Crédito", 1200.5),
            Transaccion("T004", "Débito", 200.0),
            Transaccion("T005", "Crédito", 800.0)
        ]

        def test_calcular_balance_final(self):
            """ Verifica si el balance final se calcula correctamente. """
        balance_esperado = (1500.0 + 1200.5 + 800.0) - (500.0 + 200.0)
        self.assertEqual(self.procesador.calcular_balance_final(), balance_esperado)

        def test_obtener_transaccion_mayor_monto(self):
            """ Verifica si la transacción con el mayor monto es la correcta. """
        transaccion_max = self.procesador.obtener_transaccion_mayor_monto()
        self.assertIsNotNone(transaccion_max)
        self.assertEqual(transaccion_max.transaccion_id, "T001")
        self.assertEqual(transaccion_max.monto, 1500.0)

        def test_contar_transacciones(self):
            """ Verifica si el conteo de transacciones es correcto. """
        conteo_esperado = {"Crédito": 3, "Débito": 2}
        self.assertEqual(self.procesador.contar_transacciones(), conteo_esperado)

if __name__ == '__main__':
    unittest.main()
