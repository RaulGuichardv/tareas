import asyncio
import websockets

async def chat_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        
        async def receive_messages():
            try:
                async for message in websocket:
                    print(f"\n< Mensaje de otro usuario: {message}\nEscribe tu mensaje y presiona Enter: ", end="", flush=True)
            except websockets.exceptions.ConnectionClosed:
                print("\nConexión cerrada por el servidor.")

        async def send_messages():
            while True:
                message = await asyncio.to_thread(input, "Escribe tu mensaje y presiona Enter: ")
                if message.lower() == 'exit':
                    await websocket.close()
                    break
                await websocket.send(message)

        receive_task = asyncio.create_task(receive_messages())
        send_task = asyncio.create_task(send_messages())

        await asyncio.gather(receive_task, send_task)

if __name__ == "__main__":
    try:
        asyncio.run(chat_client())
    except KeyboardInterrupt:
        print("\nCerrando cliente.")
