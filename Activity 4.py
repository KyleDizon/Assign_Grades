#Assign_Grades
def grades():
    grades = int(input("Enter your grade: "))
    if grades <0 or grades > 100:
        print("Invalid Score! Kindly Please Enter a Value Between 0 and 100")
    elif grades >90:
        print("Grade: A")
    elif grades >80:
        print("Grade: B")
    elif grades >70:
        print("Grade: C")
    elif grades >60:
        print("Grade: D")
    elif grades >0:
        print("Grade: F")
        
        
grades()


while True:
    a = input("Run Again?: ")
    if a == "Yes":
        grades()
        
    else:
        b = print("Program Done")
        break