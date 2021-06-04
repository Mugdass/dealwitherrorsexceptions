class ZeroDivisionError(Exception):
    pass

class ValueError(Exception):
    pass

    
    try:
        x=input("Enter your lucky number     ")
        print()
        if int(x) <= 0:
            raise ZeroDivisionError
    except ValueError:
            print(x,"is not a number.")
            print()
            print("please enter an actual number")
            print()
            print("for example: ")
            print()
            print('"Enter you lucky number: "')
            print()
            print(">>>10")
            print()
            print("or")
            print()
            print(">>>5")
            print()
            print("or")
            print()
            print(">>>9")
            print()
            print("or")
            print()
            print(">>>22")
            print()
            print("or even")
            print()
            print(">>>101")
            print()
            print("it an be any random number")
            print()
            print("or any other number!")
            print()
            print("Run IDLE again!")
    except ZeroDivisionError:
        print("DO NOT ENTER 0")
        print()
        print("Run IDLE again!")

        raise Exception("0 is not allowed")
            
        
   
    else:
            print ("Thank you!")
            print("no errors found")
