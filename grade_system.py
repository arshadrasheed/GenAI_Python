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

#Function Valdate the Mark
def ValidateMark(mark):
    if mark >=90 and mark<=100:
        return "A"
    elif mark >=80 and mark<90:
        return "B"
    elif mark >=70 and mark<80:
        return "C"
    elif mark >=60 and mark<70:
        return "D"
    elif mark>=0 and mark<60:
        return "E"
    else:
        return "Enter Mark within [0-100]"
    
#Grade Calcualtion
def GradeSystem():
    mark= GetInput()

    isDigit= IsNumber(mark)

    if isDigit:
      print(ValidateMark(int(mark)))  
    else:
        print("Enter Valid Digit")

#Main Execution
GradeSystem()
