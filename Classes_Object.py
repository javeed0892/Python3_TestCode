class person:
    def __init__(self, name, age, gender, state):
        self.name = name
        self.age = age
        self.gender = gender
        self.state = state

    def added_information(self,name, age, gender, state, address, is_criminal_history):
        self.name = name
        self.age = age
        self.gender = gender
        self.state = state
        self.address = address
        self.is_criminal_history = is_criminal_history
class car:
    def __init__(self, MODEL, YEAR, COLOR,BODY,SITER):
        self.MODEL = MODEL
        self.YEAR = YEAR
        self.COLOR = COLOR
        self.BODY = BODY
        self.SITER = SITER
c1 = car("ford", 2022, "RED", "COUPE", 2)
c2 = car("MALIBU", 2012, "RED", "COUPE", 4)
print(c1.COLOR)



# p1 = person("kevin", 25, "M", "ZA")

