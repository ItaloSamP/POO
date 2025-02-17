import unittest
import pygame
import sys
import os

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Agora o Python consegue encontrar o módulo assets
import assets

class TestAssets(unittest.TestCase):
    def test_load_sprites(self):
        assets.load_sprites()
        self.assertIn("bird", assets.sprites)
        self.assertIsInstance(assets.sprites["bird"], pygame.Surface)

    def test_load_audios(self):
        assets.load_audios()
        self.assertIn("hit", assets.audios)
        self.assertIsInstance(assets.audios["hit"], pygame.mixer.Sound)

if __name__ == "__main__":
    unittest.main()