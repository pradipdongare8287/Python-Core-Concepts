class Fan:
    def __init__(self,colour,speed,company):
        self.color = colour
        self.speed = speed
        self.company = company

    def start(self):
        print(self.company,"Fan Start")

    def stop(self):
        print(self.company,'Fan Stop')

f1 = Fan('Red',4,'Bajaj')
f1.start()
f1.stop()

f2 = Fan('black',4,'Usha')
f2.start()
f2.stop()