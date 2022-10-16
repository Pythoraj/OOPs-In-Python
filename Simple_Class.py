# A Sample class with init method
class Person:
    #Class variable
    Age = 31
    # init method or Constructor
    def __init__(self, Name) -> None:
        self.Name = Name                # self.Name is an instance variable.
    
    def Display(self, Add):
        # Using instance variable we can access the init method variable.
        print("Hello, My name is ",self.Name)
        print("My age is ", self.Age)    # We can access class variable using self as well as class name.
        print("Access class variable using class object", Person.Age)
        self.Add = Add
        print("My address is ", Add)
        print("My address is ", self.Add)
        print("self.Add",id(self.Add))
        print("Add",id(Add))
Obj = Person('Rajkumar Rajbhar')
Obj.Display('Gopal Pur')
Obj1 = Person("Seema Rajbhar")
Obj1.Display('Chane pur')
