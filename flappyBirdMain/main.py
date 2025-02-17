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

def carregar_usuarios():
    """Carrega os usuários do arquivo e retorna um dicionário {nome: senha}"""
    cadastro = "cadastro.txt"
    usuarios = {}

    if os.path.exists(cadastro):
        with open(cadastro, "r") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    partes = linha.split(",")
                    if len(partes) == 2:
                        nome, senha = partes
                        usuarios[nome] = senha
    return usuarios

def salvar_usuario(nome, senha):
    """Salva um novo usuário no arquivo"""
    with open("cadastro.txt", "a") as f:
        f.write(f"{nome},{senha}\n")

def cadastro():
    while True:
        usuarios = carregar_usuarios()

        nome = input("Digite seu nome (apenas letras): ").strip()
        if not nome.isalpha():
            print("Nome inválido! Use apenas letras.")
            continue
        if nome in usuarios:
            print("Este nome de usuário já existe! Tente outro.")
            continue

        senha = input("Digite sua senha (mínimo 3 números): ").strip()
        if not senha.isdigit() or len(senha) < 3:
            print("Senha inválida! Use apenas números e no mínimo 3 dígitos.")
            continue

        salvar_usuario(nome, senha)
        print("Cadastro realizado com sucesso!")

        while True:
            deseja_login = input("Deseja fazer login agora? [S/N]: ").strip().upper()
            if deseja_login == "S":
                login()
                return
            elif deseja_login == "N":
                return
            else:
                print("Opção inválida! Digite 'S' para sim ou 'N' para não.")

def login():
    usuarios = carregar_usuarios()

    if not usuarios:
        print("Nenhum usuário cadastrado. Por favor, faça o cadastro primeiro.")
        return

    while True:
        nome = input("Digite seu nome: ").strip()
        if nome in usuarios:
            senha = input("Digite sua senha: ").strip()
            if senha == usuarios[nome]:
                print("Login realizado com sucesso!")
                return
            else:
                print("Senha incorreta! Tente novamente.")
        else:
            print("Nome de usuário incorreto! Tente novamente.")

while True:
    entrando = input("Deseja Cadastrar? [S/N] ").strip().upper()
    if entrando == "S":
        cadastro()
        break
    elif entrando == "N":
        deseja_logar = input("Deseja fazer login? [S/N] ").strip().upper()
        if deseja_logar == "S":
            login()
            break
        elif deseja_logar == "N":
            print("Encerrando o programa...")
            sys.exit()
        else:
            print("Entrada inválida! Digite 'S' para sim ou 'N' para não.")
    else:
        print("Entrada inválida! Digite 'S' para sim ou 'N' para não.")

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird Game v1.0.2")

base_path = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(base_path, 'assets', 'icons', 'red_bird.png')
img = pygame.image.load(icon_path)
pygame.display.set_icon(img)

assets.load_sprites()
assets.load_audios()

clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT + 1
running = True
gameover = False
gamestarted = False

sprites = pygame.sprite.LayeredUpdates()

def create_sprites():
    Background(0, sprites)
    Background(1, sprites)
    Floor(0, sprites)
    Floor(1, sprites)
    return Bird(sprites), GameStartMessage(sprites), Score(sprites)

bird, game_start_message, score = create_sprites()

def display_message(text):
    font = pygame.font.Font(None, 15)
    text_surface = font.render(text, True, (255, 255, 255), (0, 0, 0))
    text_rect = text_surface.get_rect(center=(configs.SCREEN_WIDTH//2, configs.SCREEN_HEIGHT//3))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    pygame.time.delay(2000)

def game_loop():
    global running, gameover, gamestarted
    global bird, game_start_message, score

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not gamestarted and not gameover:
                        gamestarted = True
                        game_start_message.kill()
                        pygame.time.set_timer(column_create_event, 1500)
                    bird.handle_event(event)
                if event.key == pygame.K_ESCAPE and gameover:
                    display_message("VOCÊ PERDEU! JOGAR NOVAMENTE? [S/N]")
                    waiting_for_response = True
                    while waiting_for_response:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_s:
                                    gameover = False
                                    gamestarted = False
                                    sprites.empty()
                                    bird, game_start_message, score = create_sprites()
                                    waiting_for_response = False
                                elif event.key == pygame.K_n:
                                    display_message("ENCERRANDO O JOGO...")
                                    running = False
                                    pygame.quit()
                                    sys.exit()

            if event.type == column_create_event:
                Column(sprites)

        screen.fill(0)
        sprites.draw(screen)

        if gamestarted and not gameover:
            sprites.update()

        if bird.check_collision(sprites) and not gameover:
            gameover = True
            gamestarted = False
            GameOverMessage(sprites)
            pygame.time.set_timer(column_create_event, 0)
            assets.play_audio("hit")

        for sprite in sprites:
            if isinstance(sprite, Column) and sprite.is_passed():
                score.value += 1
                assets.play_audio("point")

        pygame.display.flip()
        clock.tick(configs.FPS)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
