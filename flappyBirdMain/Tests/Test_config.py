import unittest
import sys
import os

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Agora o Python consegue encontrar o módulo configs
import configs

class TestConfigs(unittest.TestCase):
    def test_screen_dimensions(self):
        self.assertEqual(configs.SCREEN_WIDTH, 288)
        self.assertEqual(configs.SCREEN_HEIGHT, 512)

    def test_fps(self):
        self.assertEqual(configs.FPS, 60)

    def test_gravity(self):
        self.assertEqual(configs.GRAVITY, 0.4)

if __name__ == "__main__":
    unittest.main()