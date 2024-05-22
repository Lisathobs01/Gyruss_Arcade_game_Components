import asyncio
import websockets
import json

async def connect_to_server():
    async with websockets.connect("ws://localhost:8765") as websocket:
        print("Connected to server")
        await websocket.send(json.dumps({'type': 'join_queue'}))
        print("Joined the queue")

        while True:
            message = await websocket.recv()
            data = json.loads(message)

            if data['type'] == 'match_found':
                print(f"Match found! Match ID: {data['match_id']}")
                await game_loop(websocket, data['match_id'])

async def game_loop(websocket, match_id):
    while True:
        action = {'type': 'move', 'direction': 'left', 'match_id': match_id}
        await websocket.send(json.dumps(action))

        message = await websocket.recv()
        data = json.loads(message)
        print(f"Received message: {data}")
        # Update the game state based on server message

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(connect_to_server())

