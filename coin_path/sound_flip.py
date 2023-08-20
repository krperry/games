import random
import winsound as ws

ws.PlaySound("sounds\\flip.wav", ws.SND_FILENAME | ws.SND_NOWAIT)
coin = ["Head", "tail"]
print(f"{random.choice(coin)}")
