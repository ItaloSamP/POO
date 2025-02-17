import unittest
import sys
import os

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Agora o Python consegue encontrar o módulo layer
from layer import Layer

class TestLayer(unittest.TestCase):
    def test_layer_values(self):
        self.assertEqual(Layer.BACKGROUND, 1)
        self.assertEqual(Layer.OBSTACLE, 2)
        self.assertEqual(Layer.FLOOR, 3)
        self.assertEqual(Layer.PLAYER, 4)
        self.assertEqual(Layer.UI, 5)

if __name__ == "__main__":
    unittest.main()