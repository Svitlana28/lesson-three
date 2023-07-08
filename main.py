day = int(input())
if day == 1:
    print("mandey")
if day == 2:
    print("tuesday")
if day == 3:
    print("wednesday")
if day == 4:
    print("thursday")
if day == 5:
    print("friday")
if day == 6:
    print("saturday")
if day == 7:
    print("sunday")

#2D

n1 = int(input(""))
n2 = int(input(""))
if (n1 == n2):
    print(f"{n1}")
if (n1 < n2):
    print(f"{n1} , {n2} ")
elif (n2 < n1):
    print(f"{n2}  , {n1} ")

    #3D
try:
    user1 = int(input("Enter number..."))
    user2 = int(input("Enter number.."))
    action_ = (input("Enter action (+,-,/,*)"))
    match action_:
        case "+":
            print(user1 + user2)
        case "-":
            print(user1 - user2)
        case "*":
            print(user1 * user2)
        case "/":
            print(user1 / user2)
except ValueError as error:
    print("error", error)
except Exception as error:
    print("error")


