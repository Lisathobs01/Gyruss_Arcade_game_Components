import asyncio
import websockets
import json

connected_players = set()
waiting_players = {}


async def handle_connection(websocket, path):
    print("New connection established")
    connected_players.add(websocket)
    try:
        while True:
            message = await websocket.recv()
            data = json.loads(message)

            if data['type'] == 'join_queue':
                print(f"Player joined the queue: {websocket}")
                waiting_players.append(websocket)
                await match_players()

    except websockets.ConnectionClosed:
        print("Connection closed")
        pass
    finally:
        connected_players.remove(websocket)
        if websocket in waiting_players:
            waiting_players.remove(websocket)


async def match_players():
    while len(waiting_players) >= 2:
        player1 = waiting_players.pop(0)
        player2 = waiting_players.pop(0)
        match_id = str(len(connected_players))

        game_type = 'friendly'  # Change this logic as needed

        print(f"Match found: {player1} vs {player2}")
        await player1.send(
            json.dumps({'type': 'match_found', 'match_id': match_id, 'opponent': 'player2', 'game_type': game_type}))
        await player2.send(
            json.dumps({'type': 'match_found', 'match_id': match_id, 'opponent': 'player1', 'game_type': game_type}))


async def main():
    start_server = websockets.serve(handle_connection, "localhost", 8765)
    await start_server


# Create and set the event loop
if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.run_forever()
