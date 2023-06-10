import unittest
from claseSaludo import Saludo
import io
import sys

class TestSaludo(unittest.TestCase):
    def test_decir_hola(self):
        saludo = Saludo("hola")

        # Capturamos la salida estándar
        captured_output = io.StringIO()
        sys.stdout = captured_output

        saludo.decir_hola()

        # Restauramos la salida estándar
        sys.stdout = sys.__stdout__

        # Verificamos la salida esperada
        self.assertEqual(captured_output.getvalue().strip(), "Hola mundo")

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
