import unittest
import pygame
import sys
import os

# Define o caminho correto para os módulos
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import assets

class TestAssets(unittest.TestCase):
    def setUp(self):
        assets.load_sprites()
        assets.load_audios()

    def test_load_sprites(self):
        self.assertIn("bird", assets.sprites, "Sprite 'bird' não encontrado")
        self.assertIsInstance(assets.sprites["bird"], pygame.Surface, "Objeto 'bird' não é uma Surface")

    def test_load_audios(self):
        self.assertIn("hit", assets.audios, "Áudio 'hit' não encontrado")
        self.assertIsInstance(assets.audios["hit"], pygame.mixer.Sound, "Objeto 'hit' não é um Sound")

if __name__ == "__main__":
    unittest.main()
