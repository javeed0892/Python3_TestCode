class student:
    def __init__(self, name, gpa, major):
        self.name = name
        self.gpa = gpa
        self.major = major
    def in_honors(self):
        Stundent_name = self.name
        Student_GPA = self.gpa
        Student_Major = self.major
        if self.gpa <= 3.5:
            you_gpa = self.gpa - 3.5
            return "Sorry you GPA is less then 3.5 = "  + str(you_gpa) + "\n" +Stundent_name +"\n"+ str(Student_GPA) +"\n" + Student_Major
        else:
            return "you are going to Honors"+ "\n" +Stundent_name +"\n"+ str(Student_GPA) +"\n" + Student_Major