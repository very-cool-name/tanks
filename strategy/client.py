"""Works with server. Probably like this:
1. Connects to server
2. Receives player_id and creates player
3. On every MOVE_NOTIFICATION deserializes Game, World. Gets player's tank from world and calls move
4. Serializes Move and sends to server
5. Repeats 3 until GAME_END notification
"""

import socket

from strategy.StrategyReceive import StrategyReceive

if __name__ == '__main__':
    socket = socket.socket()
    socket.connect(('localhost', 8080))
    strategy_receive = StrategyReceive(socket)
    
    while strategy_receive.is_running():
        strategy_receive.move()
    
    socket.close()