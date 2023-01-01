class Car():
    def __init__(self,modelname,yearm,price):
        self.modelname = modelname
        self.yearm = yearm
        self.price = price
    def price_inc(self):
        self.price = (self.price*2)
honda = Car('city',2017, 1000000)
tata = Car('bolt', 2016, 6000000)

tata.price_inc()
print(tata.price)

class Supercar(Car):
    pass
honda = Supercar('city',2017, 1000000)
tata = Car('bolt', 2016, 6000000)

honda.price_inc()
print(tata.yearm)
