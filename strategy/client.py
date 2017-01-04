"""Works with server. Probably like this:
1. Connects to server
2. Receives player_id and creates player
3. On every MOVE_NOTIFICATION deserializes Game, World. Gets player's tank from world and calls move
4. Serializes Move and sends to server
5. Repeats 3 until GAME_END notification
"""