import random
import playsound 

playsound.playsound("sound/dice.wav")
for i in range(5):    
    print (f"{random.randint(1,6)}")
