import unittest
import sys
import os

# Define o caminho correto para os módulos
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from layer import Layer

class TestLayer(unittest.TestCase):
    def test_layer_values(self):
        self.assertTrue(hasattr(Layer, "BACKGROUND"), "BACKGROUND não definido")
        self.assertTrue(hasattr(Layer, "OBSTACLE"), "OBSTACLE não definido")
        self.assertTrue(hasattr(Layer, "FLOOR"), "FLOOR não definido")
        self.assertTrue(hasattr(Layer, "PLAYER"), "PLAYER não definido")
        self.assertTrue(hasattr(Layer, "UI"), "UI não definido")

        self.assertEqual(Layer.BACKGROUND, 1, "Valor incorreto para BACKGROUND")
        self.assertEqual(Layer.OBSTACLE, 2, "Valor incorreto para OBSTACLE")
        self.assertEqual(Layer.FLOOR, 3, "Valor incorreto para FLOOR")
        self.assertEqual(Layer.PLAYER, 4, "Valor incorreto para PLAYER")
        self.assertEqual(Layer.UI, 5, "Valor incorreto para UI")

if __name__ == "__main__":
    unittest.main()
