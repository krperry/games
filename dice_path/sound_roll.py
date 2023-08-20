import random
import winsound as ws

ws.PlaySound("sounds/dice.wav", ws.SND_FILENAME | ws.SND_NOWAIT)
print(f"{random.randint(1,6)}")
