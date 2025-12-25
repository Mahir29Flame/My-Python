class Train:
    def __init__(slf,name,age,trainno,seatno,_class="Economy",fare=200):      # soo everything is ok if u change all the self
        slf.name = name
        slf.age = age
        slf.trainno = trainno
        slf.seatno = seatno
        slf._class = _class
        slf.fare = fare
        print("The name is",name,", age is",age,", train number is",trainno,", The class is",_class,", The seat number is",seatno,"and The fare is",fare)
        Input = input("Are all the details correct? (Yes/No): ")
        if Input.lower() == "yes":
            print("Ticket Successfully Booked! \nWe hope you enjoy your journey 😊!")
        else:
            print("Ticket Booking Cancelled")

Name = input("Enter the name: ")
Age = int(input("Enter Your age: "))
trainno = int(input("Enter the train number: "))
_class = input("Enter which class you want to travel in (Economy/Business/First): ")
seatno = int(input("Enter the seat number: "))
if _class.lower() == "economy":
    fare = 200
elif _class.lower() == "business":
    fare = 500
elif _class.lower() == "first":
    fare = 1000
else:
    print("Invalid class selected")
ticket = Train(Name,Age,seatno,_class,fare)        