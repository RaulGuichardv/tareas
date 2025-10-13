import asyncio
import websockets

async def echo(websocket):
    print(f"Cliente conectado desde {websocket.remote_address}")
    try:
        async for message in websocket:
            print(f"Recibido del cliente: {message}")
            await websocket.send(message)
            print(f"Enviado al cliente: {message}")
    except websockets.exceptions.ConnectionClosed:
        print(f"Cliente desconectado: {websocket.remote_address}")
    finally:
        print("Conexión cerrada.")

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        print("Servidor de Eco iniciado en ws://localhost:8765")
        await asyncio.Future()  # Mantiene el servidor corriendo indefinidamente.

if __name__ == "__main__":
    asyncio.run(main())
