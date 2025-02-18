class Student:
    def __init__(intro, name, age, course):
        intro.name = name
        intro.age = age
        intro.course = course

    def introduce(intro):
        print (f"I'm  {intro.name}.")
        print (f"I am {intro.age} years old.")
        print (f"I am {intro.course}.\n")

student1 = Student("Jhon Cris Besco", 21, "student in ADFC")
student2 = Student("Bobby Porta", 21, "student in ADFC")
student3 = Student("Axel Klien Congzon", 20, "student in ADFC")

student1.introduce()
student2.introduce()
student3.introduce()
