import os
import pygame

# Configura o Pygame para usar o driver de áudio 'dsp' ou 'dummy'
os.environ["SDL_AUDIODRIVER"] = "dummy"  # ou "dummy" se "dsp" não funcionar

sprites = {}
audios = {}


def load_sprites():
    base_path = os.path.dirname(os.path.abspath(__file__))
    sprites_path = os.path.join(base_path, 'assets', 'sprites')
    
    if not os.path.exists(sprites_path):
        raise FileNotFoundError(f"Diretório não encontrado: {sprites_path}")
    
    global sprites  # Adicione esta linha para usar o dicionário global
    sprites = {}  # Limpe o dicionário global antes de carregar os sprites
    for file in os.listdir(sprites_path):
        if file.endswith('.png'):
            sprite_name = os.path.splitext(file)[0]
            sprites[sprite_name] = pygame.image.load(os.path.join(sprites_path, file))
    
    return sprites


def get_sprite(name):
    return sprites[name]


def load_audios():
    pygame.mixer.init()  # Inicializa o mixer do Pygame
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    audios_path = os.path.join(base_path, 'assets', 'audios')
    
    if not os.path.exists(audios_path):
        raise FileNotFoundError(f"Diretório não encontrado: {audios_path}")
    
    global audios  # Adicione esta linha para usar o dicionário global
    audios = {}  # Limpe o dicionário global antes de carregar os áudios
    for file in os.listdir(audios_path):
        if file.endswith('.wav') or file.endswith('.mp3'):
            audio_name = os.path.splitext(file)[0]
            audios[audio_name] = pygame.mixer.Sound(os.path.join(audios_path, file))
    
    return audios


def play_audio(name):
    audios[name].play()