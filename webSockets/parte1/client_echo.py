import asyncio
import websockets

async def send_and_receive():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message_to_send = "Hola, Servidor!"
        await websocket.send(message_to_send)
        print(f"> Enviado: {message_to_send}")
        response = await websocket.recv()
        print(f"< Recibido: {response}")

if __name__ == "__main__":
    asyncio.run(send_and_receive())
