class Car():
    def __init__(self,name,yearm,price):
        self.name = name
        self.yearm = yearm
        self.price = price
    def sendMessage(self):
        print(f"this is {self.name} car.")
class SuperCar(Car):
    def __init__(self,name,yearm,price,color):
        super(SuperCar,self).__init__(name,yearm,price)
        self.color = color
    def sendMessage(self):
        print(f"this is {self.name} super car.")
def main():
    bmw = Car("bwx x200" , 1984 , 2000)
    corvette = SuperCar("corvette zo6" , 2015,34000,"red")
    corvette.sendMessage()
    bmw.sendMessage()

if __name__ == '__main__':main()

