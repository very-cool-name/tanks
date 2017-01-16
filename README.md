# tanks
AI game of tanks

Consists of server and client. 

##Server
Server is configured using file in json format. See _simulator/default_settings_ and _simulator/Simulator.py Settings_ class.
Server is run from root directory using command: `python -m simulator.Simulator simulator/default_settings.json`

##Client
Client uses _strategy/MyStrategy.py_ where method move should be implemented filling move parameter.
Client is run from root directory using command: `python -m strategy.client`
