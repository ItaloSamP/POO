import unittest
import sys
import os

# Define o caminho correto para os módulos
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import configs

class TestConfigs(unittest.TestCase):
    def test_screen_dimensions(self):
        self.assertTrue(hasattr(configs, "SCREEN_WIDTH"), "SCREEN_WIDTH não definido")
        self.assertTrue(hasattr(configs, "SCREEN_HEIGHT"), "SCREEN_HEIGHT não definido")
        self.assertEqual(configs.SCREEN_WIDTH, 288, "Valor incorreto para SCREEN_WIDTH")
        self.assertEqual(configs.SCREEN_HEIGHT, 512, "Valor incorreto para SCREEN_HEIGHT")

    def test_fps(self):
        self.assertTrue(hasattr(configs, "FPS"), "FPS não definido")
        self.assertEqual(configs.FPS, 60, "Valor incorreto para FPS")

    def test_gravity(self):
        self.assertTrue(hasattr(configs, "GRAVITY"), "GRAVITY não definido")
        self.assertEqual(configs.GRAVITY, 0.4, "Valor incorreto para GRAVITY")

if __name__ == "__main__":
    unittest.main()
