import random
import playsound as ps

ps.playsound("sounds/flip.wav")
coin = ["Head", "tail"]
print(f"{random.choice(coin)}")
