import sys
import os
import pygame
import asyncio
import websockets
import assets
import configs
from objects.background import Background
from objects.bird import Bird
from objects.column import Column
from objects.floor import Floor
from objects.gameover_message import GameOverMessage
from objects.gamestart_message import GameStartMessage
from objects.score import Score

pygame.init()

# Configuração da tela do jogo
screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird Game v1.0.2")

# Configuração do ícone
base_path = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(base_path, 'assets', 'icons', 'red_bird.png')
img = pygame.image.load(icon_path)
pygame.display.set_icon(img)

# Carregar assets
assets.load_sprites()
assets.load_audios()

# Configurações do jogo
clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT + 1  # 🔥 Corrigido para evitar conflito com outros eventos
running = True
gameover = False
gamestarted = False
logged_in = False
current_user = None

# Criando sprites
sprites = pygame.sprite.LayeredUpdates()

def create_sprites():
    Background(0, sprites)
    Background(1, sprites)
    Floor(0, sprites)
    Floor(1, sprites)
    return Bird(sprites), GameStartMessage(sprites), Score(sprites)

bird, game_start_message, score = create_sprites()

# Função assíncrona para enviar mensagens ao WebSocket
async def send_message(message):
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        print(response)
        return response

# Registro e login do usuário
async def register(username, password):
    response = await send_message(f"register:{username}:{password}")
    return "register_success" in response

async def login(username, password):
    response = await send_message(f"login:{username}:{password}")
    return "login_success" in response

async def logout():
    response = await send_message("logout:")
    return "logout_success" in response

# Loop de Jogo
def game_loop():
    global running, gameover, gamestarted, logged_in, current_user
    global bird, game_start_message, score

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # O usuário pode pressionar espaço para iniciar o jogo
            if event.type == pygame.KEYDOWN:
                print(f"Tecla pressionada: {event.key}")  # Depuração

                if event.key == pygame.K_SPACE:
                    if not gamestarted and not gameover:
                        gamestarted = True
                        game_start_message.kill()
                        pygame.time.set_timer(column_create_event, 1500)  # 🔥 Agora os canos serão criados corretamente
                        print("Jogo iniciado! Canos serão gerados.")

                    bird.handle_event(event)  # 🔥 Pássaro pula corretamente

                if event.key == pygame.K_ESCAPE and gameover:
                    gameover = False
                    gamestarted = False
                    sprites.empty()
                    bird, game_start_message, score = create_sprites()

                if event.key == pygame.K_o and logged_in:  
                    asyncio.run(logout())
                    logged_in = False
                    current_user = None
                    print("Logout bem-sucedido!")

            # Criando canos no jogo
            if event.type == column_create_event:
                print("Criando um novo cano!")  # Depuração
                Column(sprites)  # 🔥 Canos agora aparecem corretamente

        # Atualiza o jogo
        screen.fill(0)
        sprites.draw(screen)

        if gamestarted and not gameover:
            print("Jogo rodando...")  # Depuração
            sprites.update()

        # Verifica colisões
        if bird.check_collision(sprites) and not gameover:
            gameover = True
            gamestarted = False
            GameOverMessage(sprites)
            pygame.time.set_timer(column_create_event, 0)
            assets.play_audio("hit")

        # Atualiza pontuação
        for sprite in sprites:
            if isinstance(sprite, Column) and sprite.is_passed():
                score.value += 1
                assets.play_audio("point")

        pygame.display.flip()
        clock.tick(configs.FPS)

    pygame.quit()

# ✅ Rodando o jogo separadamente do WebSocket
if __name__ == "__main__":
    game_loop()
