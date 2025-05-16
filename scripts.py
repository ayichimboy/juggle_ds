# object oriented programming
from datetime import datetime

# create a simple class
# begin with defining your class
class Machinelearnging: # class is a blueprint for creating objects
    
    # initialization using init to setup your class attributes
    # use of self is important but can be replaced with something set by the user. But per conversion, use 
    # self instead of replacement as this may confuse other users. 
    # init method is run ones an object is instantiated
    # instance of a specific object in 
    def __init__(self, supervised, unsupervised, blackbox):# init is a python method used to initialize the class
        self.supervised = supervised
        self.unsupersion = unsupervised
        self.blackbox = blackbox
        
## Ceate a model for the skill vuss
    def my_ml(self):
        print(f'Supervised machine learning is: {self.supervised}')
        
        
        # -------------------------start user class -------------------------------
# create a user class
class User:# always use pascal naming for class name
    # static attribute
    user_count = 0
    
    def __init__(self, username, email, password):
        self.username = username
        self._email = email # protected with self._email, underscore after dot
        self.password = password
        User.user_count += 1
        
        ## -----------------getter and setter with Java script method -------------
       # create a getter method 
    def get_email(self): # get a protected attribute
        print(f'Email accessed at {datetime.now()}')
        return self._email
        
    # create a setter method
    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email
        else:
            print('Please include @ in your email')
            
    # getter and setter method using pythong method
    @property # getter property
    def email(self):
        print('Email Accessed')
        return self._email
        
    @email.setter #setter property
    def email(self, new_email):
        self._email= new_email
        
# static properties
    
    ## ---------------------------- end -----------------------------    
# test code
ml = Machinelearnging('linear_regression', 'kmeans', 'xgboost')
ml.my_ml()
# my_ml(ml)

user1 = User('davidjones', 'david_jones@icecream.com', 'chocolate')
user2 = User('johnjohn', 'john_john@icecream.com', 'vanilla')
user3 = User('danking', 'dan_king@icecream.com', 'mint')

print(user1.get_email())

user1.set_email('dave_james@icecream.com')
print(user1.get_email())

user1.email = 'vipper_king@snakeworld.com'
print(user1.email)

print(User.user_count)