class Robot:
    def __init__(self , robotname , voltage , speed):
        self.name = robotname
        self.vlt = voltage
        self.spd = speed
        
bot = Robot("Baxter" , 12 , 300)
print(bot.name)
print(bot.vlt)
print(bot.spd)