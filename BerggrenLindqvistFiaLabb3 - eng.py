"""
Fia Berggren Lindqvist
Windows 10
"""

December_temperature = []

#This function collects and validates the users input
def December ():
    for x in range (1, 32):
        while True:
            temperature = input("Please write the temperature for %s December: " %x)
            try:
                temperature = float(temperature)
                break
            except ValueError:
                print("Wrong type of input, please write a number")
        December_temperature.append(temperature)

#This function calculates the lowest temperature
def actionMin():
    print("The lowest temperature in December was ", min(December_temperature), "degrees")

#This function calculates the average temperature
def actionMid():
    sumDecember_temperature = sum(December_temperature)
    midValue = sumDecember_temperature / 31
    print ("The average temperature in December was ", midValue, "degrees")

#This function calculates the highest temperature
def actionMax():
    print("The highest temperature in December was ", max(December_temperature), "degrees")

#This function returns answer to which temperature it was on the selected date picked by the user
def actionDay():
    while True:
        try:
            day = int(input("Which date would you like to know the temperature of? "))
            if day > 0 and day < 32:
                print(December_temperature[day - 1], "degrees")
                break
            else:
                print("Please write a number between 1-31")
        except ValueError:
            print("Please write a number between 1-31")

#This function receives the users input to know what the user would like to do
#and returns an answer based of the users choices
def mainMenu():
    while True:
        user_input = input("\n\n For the months highest temperature, write MAX \n For the months lowest temperature, write MIN \n For the months average temperature, write AVERAGE \n Choose day by writing DAY \n Finish by writing EXIT \n\n Enter your choice: ")
        if user_input.lower() == "MAX":
            actionMax()
        elif user_input.lower() == "MIN":
            actionMin()
        elif user_input.lower() == "AVERAGE":
            actionMid()
        elif user_input.lower() == "DAY":
            actionDay()
        elif user_input.lower() == "EXIT":
            print ("Welcome back, bye!")
            break
        else:
            print("Wrong input, please try again!")

#Starts the programme
December()
mainMenu()
