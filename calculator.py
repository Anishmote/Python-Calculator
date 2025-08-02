

def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def devidation(x ,y):
    if y == 0:
        return "Cant Divide By Zero"
    return x/y
            
while True:
     
    print("✖️➗➕➖\nWelcome To Calculator")
    print("1.Addition(+)")
    print("2.Substraction(-)")
    print("3.Multiplication(x)")
    print("4.Divide(/)")

    num1 = (input("Enter Your Choice (1/2/3/4):"))
    
    try:

        x1 = float(input("Enter The First Number:"))
        y1 = float(input("Enter Tne Second Number"))

        if num1 == "1":
            print(f"Result Is:✅", addition(x1,y1))

        elif num1 == "2":
            print(f"Result Is:✅",subtraction(x1,y1))

        elif num1 =="3":
            print(f"Result Is {multiplication(x1,y1)}✅")

        elif num1 == "4":
            print(f"Result Is {devidation(x1,y1)}✅")
        
        else:
             print("Invilde Value..❌")

    except ValueError:
        print("Invilde Value..")


    choice = input("🟢Enter Your Choice (y/n):")


    if choice == "n":
                print("🔴You Exited Calculator")
                break
