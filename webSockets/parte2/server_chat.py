import asyncio
import websockets
import json

# Un conjunto para almacenar todas las conexiones de clientes activas.
CONNECTED_CLIENTS = set()

async def handler(websocket):
    # Añade el nuevo cliente al conjunto de conexiones.
    CONNECTED_CLIENTS.add(websocket)
    print(f"Nuevo cliente conectado. Total: {len(CONNECTED_CLIENTS)}")
    
    try:
        # Escucha mensajes de este cliente.
        async for message in websocket:
            print(f"Mensaje recibido: {message}")
            
            # Broadcast a todos los clientes conectados.
            tasks = [client.send(message) for client in CONNECTED_CLIENTS]
            await asyncio.gather(*tasks)
            
            print(f"Mensaje '{message}' enviado a {len(CONNECTED_CLIENTS)} clientes.")

    except websockets.exceptions.ConnectionClosed:
        print("Un cliente se ha desconectado.")
    finally:
        # Elimina al cliente del conjunto cuando se desconecta.
        CONNECTED_CLIENTS.remove(websocket)
        print(f"Cliente eliminado. Total: {len(CONNECTED_CLIENTS)}")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Servidor de Chat iniciado en ws://localhost:8765")
        await asyncio.Future()  # Mantiene el servidor activo.

if __name__ == "__main__":
    asyncio.run(main())
