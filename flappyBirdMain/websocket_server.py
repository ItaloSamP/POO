import asyncio
import websockets

# Armazena os usuários registrados (em memória)
users = {}

async def handle_client(websocket, path):
    print("Novo cliente conectado.")

    try:
        async for message in websocket:
            print(f"Mensagem recebida: {message}")

            # Processa a mensagem do cliente
            if message.startswith("register:"):
                _, username, password = message.split(":")
                if username in users:
                    await websocket.send("register_failure: Usuário já existe.")
                else:
                    users[username] = password
                    await websocket.send("register_success: Registro bem-sucedido.")

            elif message.startswith("login:"):
                _, username, password = message.split(":")
                if username in users and users[username] == password:
                    await websocket.send("login_success: Login bem-sucedido.")
                else:
                    await websocket.send("login_failure: Nome de usuário ou senha incorretos.")

            elif message.startswith("logout:"):
                await websocket.send("logout_success: Logout bem-sucedido.")

            else:
                await websocket.send("unknown_command: Comando desconhecido.")

    except websockets.ConnectionClosed:
        print("Cliente desconectado.")

async def start_server():
    async with websockets.serve(handle_client, "localhost", 8765):
        print("Servidor WebSocket iniciado em ws://localhost:8765")
        await asyncio.Future()  # Executa para sempre

if __name__ == "__main__":
    asyncio.run(start_server())