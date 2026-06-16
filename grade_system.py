#Input isNumber Validation Function
def IsNumber(number):
    try:
        num=int(number)
        return True
    except:
        return False

#Function Gets Input from User   
def GetInput():
    print("Enter your Mark [0-100]")
    number= input()
    return number

#Grade Constants
grade=("A","B","C","D","E")

#Function Valdate the Mark
def ValidateMark(mark):
    if mark >=90 and mark<=100:
        PrintResult(mark,grade[0])
    elif mark >=80 and mark<90:
        PrintResult(mark,grade[1])
    elif mark >=70 and mark<80:
        PrintResult(mark,grade[2])
    elif mark >=60 and mark<70:
        PrintResult(mark,grade[3])
    elif mark>=0 and mark<60:
        PrintResult(mark,grade[4])
    else:
        return "Enter Mark within [0-100]"
    
def PrintResult(mark, grade):
     print("--------------------")
     print("Your Mark is ",mark)
     print("Your Grade is ",grade)
     print("--------------------")

#Grade Calcualtion
def GradeSystem():

    #Get Input from User
    mark= GetInput()

    #Validate the input is number or not
    isDigit= IsNumber(mark)

    #Validate the Mark
    if isDigit:
      ValidateMark(int(mark))
    else:
        print("Enter Valid Digit")

#Main Execution
GradeSystem()
