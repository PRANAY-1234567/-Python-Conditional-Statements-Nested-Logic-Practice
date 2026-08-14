"""#wap to check the given number is odd and divisible by 7
num = int(input("Enter the number: "))
if num%2==1:
    print(f'The given number {num} is odd')
    if num%7==0:
        print(f'The given number {num} is  divisible by 7')

    else:
        print(f'The given number {num} is not divisible by 7')

else:
    print(f'The given number {num} is even')
#==========================================================================


#WAP to perform list operations user should enter only 

data = eval(input("Enter the data type: "))
if isinstance(data,list):
    print("Hey its List Data Type")
    options=eval(input("Enter the option(1,2,3): "))
    if options==1:
        print(data.pop())

    elif options==2:
        print(data.pop())

    elif options==3:
        data.clear()
        print(data)

    else:
        print("invalid options")

else:
    print("Invalid Data Type")

#=================================================================

#Wap to validate facebook username and password condition is :-->username--->"Python" and password="Pyhon masters"
print("Welcome to facebook page")
user_name=eval(input("enter the name"))
if user_name=="Python":
    print("User name is valid ")
    password = eval(input("Enter the password"))
    if password=="python masters":
        print("User name password also valid")
    else:
        print("User name password is invalid ")

else:
    print("Username is invalid")

#----------------------------------------------------------------------------------------

#WAP to check: If the age is 18 or above, check whether the person has a driving license.
# If yes "Can drive " otherwise "Get licenses".If age is below 18 "Under Age".

age = eval(input("Enter the age: "))

if age>=18:
    license=eval(input("Licenence is Yes|No: "))
    if license=="Yes":
        print("can drive")
    else:
        print("Get licenence")

else:
    print("Under age")

-------------------------------------------------------------------------------------------------

# WAP to check: First check whether the pin is correct If correct, check whether the withdrawal amount is within the balance.
#If yes "Withdraw Money" otherwise "Insufficient Balance" If PN is wrong "Wrong Pin"

pin=int(input("Enter the Pin: "))
pin1=1234

if pin == pin1:
    print("Pin is corect")
    amount=int(input("Enter the withdrawal amount: "))
    balance= 5000
    if amount<=balance:
        print("Yes, Withdraw Money",amount)
    else:
        print("Insufficient Balance")

else:
    print("Wrong Pin")

====================ANOTHER METHOD==========================================

pin=eval(input("enter the Pin number"))
if pin==1234:
    balance=eval(input("enter the total Balance"))
    print("total Balance in My account---->",balance)
    amount=eval(input("enter the amount"))
    if amount<=balance:
        print("withdraw Money done")
        print("Total balance is ",balance-amount)
    else:
        print("Insufficient balance")
else:
    print("wrong Pin number") 

-----------------------------------------------------------------------------------------------------------

#WAP to check if age is 21 or above, check whether the salary is 25000 or more 
# if salary is sufficient "Loan Eligible" Otherwise "Salary is too low" 
# if age is below 21 "Age Not Eligible"

age=eval(input("Enter the age: "))
if age>=21:
    sal=eval(input("Enter the salary: "))
    if sal>=25000:
        print("Loan Eligible")
    else:
        print("Salary is too low")

else:
    print("Age is not eligible")

--------------------------------------------------------------------------------------------------------------

#WAP to book a ticket in book my show
print("Welcome to BookMy Show")
theater = ["PVR","Inox","cinipole"]
user = eval(input("Enter the theater name: "))
if user in theater:  #For choosing theater use (in)
    print(f'user is selected the theater is {user}')
    movies = ["RRR","Spiderman","Hulk","Captain america"]
    user1=eval(input("Enter the movie name: "))
    if user1 in movies:
        print(f'user is selected the Theater name is {user} '
        f'user1 is selected the movie is {user1} ')
        Ticket_price=[200,300,400,500]
        amount=int(input("Enter the amount: "))

        if amount==Ticket_price[0]:
            print(f'user is selected the Theater name is {user} '
            f'user1 is selected the movie is {user1} '
            f'Total ticket amount is {amount}')

        elif amount==Ticket_price[2]:
            print(f'user is selected the Theater name is {user} '
            f'user1 is selected the movie is {user1} '
            f'Total ticket amount is {amount} ')

        elif amount==Ticket_price[3]:
            print(f'user is selected the Theater name is {user} '
            f'user1 is selected the movie is {user1} '
            f'Total ticket amount is {amount} ')

    
    else:
        print("Wrong Movie Name")


else:
    print("Wrong Theater selected")"""