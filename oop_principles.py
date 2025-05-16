# create an oop using the various principles

# OOP principles 
# 1 - Encapsulation
# 2 - Abstraction     
# 3 - Inheritance
# 4 - Polymorphism
# 5 - Cooupling 
# 6 - Compostion 
# 7 - Composition vs Inheritance           
# 8 - Fragile Base Class Problems

class Cars:
    
    def __init__(self, vin_num, year, model, num_drive):
        
        self.vin_num = vin_num
        self.year = year
        self.model = model
        self.num_drive = num_drive
        # self.electric_gas = electric_gas
        
    def speed_60(self,speed):
        if speed > 60:
            print('fast vehicles')
        else:
            print('maybe gas engine')

            
class Electric(Cars):
    
    def __init__(self, vin_num, year, model, num_drive, electric_gas):
        super().__init__(vin_num, year, model, num_drive)
        self.electric_gast = electric_gas
          

# checkout results----------------
car1 = Cars(3322, 2025, 'chevy', '2wd')
car2 = Electric(4566, 2016, 'ford', '2wd', 'gas')
car1.speed_60(100)

# print dict
print(car1.__dict__)
print(car1.speed_60(100))