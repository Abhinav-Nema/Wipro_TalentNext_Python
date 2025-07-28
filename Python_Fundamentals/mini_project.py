
'''
MINI PROJECT
1.create a python program that asks the user how far they want to travel. if they want to travel less than three miles tell them to ride Bicycle. if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle. if they want to travel three hundred miles or more tell them to driver Super-Car.
Sample Output:
How far would you like to travel in miles? 2500
I suggest Super-Car to your destination
'''

def vehcle_suggestion():
    distance = int(input("How far would you like to travel in miles?"))

    if distance <= 3:
        print("I suggest riding a Bycycle to your destination")

    elif distance > 3 and distance < 300:
        print("I suggest riding a Motor-cycle to your destination")
    
    elif distance >= 300:
        print("I suggest Super-Car to your destination")


'''
MINI PROJECT
2.Let's assume you are planning to use your python skills to build an App for Mobile.
You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
Write a python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How much days can I operate one server with $918?
'''    
def cost_provider():
    #0.51 per hour
    cost_per_day = 0.51 * 24
    cost_per_week = cost_per_day * 7
    cost_per_month = cost_per_day * 30 #assuming 30 days in a month 

    total_days = 918 / cost_per_day

    print(f"cost to operate one server per day is ${cost_per_day}")
    print(f"cost to operate one server per week is ${cost_per_week}")
    print(f"cost to operate one server per month is ${cost_per_month}")
    print(f"the number of days one server can be operated with $918 are {total_days} days")



