# Multiplayer Component
This component enables real-time matchmaking for your multiplayer game using WebSockets. 
It efficiently pairs players and facilitates communication between the server and clients.
### Features:
1. Asynchronous matchmaking for smooth player pairing.
2. Real-time communication via WebSockets for low-latency gameplay.
3. Scalable design for handling multiple players.

### Usage:
1. Server: Integrate `server.py` into your game server for player management and matchmaking.
2. Client: Include `client.py` in each client application to connect, join queues, and receive updates.

### #Dependencies:

1. asyncio
2. ebsockets
3. json

### Installation:
`pip install asyncio websockets json`

# Accessibility Component

## Files
1. `accessibility_features.py`: Contains the implementation of the accessibility features.
2. `gyruss_game.py`: Contains the main game logic integrating the accessibility features

## Running the Game

1. Clone the repository.
2. Navigate to the project directory.
3. Run the game with:
   ```bash
   python gyruss_game.py