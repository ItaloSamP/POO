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
        """
        Método executado antes de cada teste.
        Carrega os sprites e áudios necessários para os testes.
        """
        assets.load_sprites()
        assets.load_audios()

    def test_load_sprites(self):
        """
        Testa se os sprites foram carregados corretamente.
        Verifica se as chaves dos sprites do pássaro estão presentes e se são instâncias de pygame.Surface.
        """
        # Verifica se as variações do pássaro estão carregadas
        bird_sprites = ["redbird-downflap", "redbird-midflap", "redbird-upflap"]
        for sprite in bird_sprites:
            self.assertIn(sprite, assets.sprites, f"Sprite '{sprite}' não encontrado")
            self.assertIsInstance(assets.sprites[sprite], pygame.Surface, f"Objeto '{sprite}' não é uma Surface")

        # Verifica outros sprites importantes
        self.assertIn("background", assets.sprites, "Sprite 'background' não encontrado")
        self.assertIsInstance(assets.sprites["background"], pygame.Surface, "Objeto 'background' não é uma Surface")

        self.assertIn("pipe-green", assets.sprites, "Sprite 'pipe-green' não encontrado")
        self.assertIsInstance(assets.sprites["pipe-green"], pygame.Surface, "Objeto 'pipe-green' não é uma Surface")

    def test_load_audios(self):
        """
        Testa se os áudios foram carregados corretamente.
        Verifica se a chave 'hit' está presente e se é uma instância de pygame.mixer.Sound.
        """
        self.assertIn("hit", assets.audios, "Áudio 'hit' não encontrado")
        self.assertIsInstance(assets.audios["hit"], pygame.mixer.Sound, "Objeto 'hit' não é um Sound")

if __name__ == "__main__":
    unittest.main()