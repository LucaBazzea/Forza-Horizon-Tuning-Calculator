
# <-------Clear Terminal------->

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# <-------Get the car's weight distrobution------->

def get_weight_per():

    front_weight = input("Please enter the weight distrobution % of your car: ")

    front_weight_per = f"0.{front_weight}" # Add "0." to the beginning of the weight % value
    front_weight_per = float(front_weight_per) # Convert that value from a string to a decimal
    rear_weight_per = 1.0 - front_weight_per # Find the weight % of the rear by subtracting the front weight % from 100

    clear()

    return front_weight_per, rear_weight_per

# <-------Get the max and min slider values------->

def get_max_min():

    max = float(input("What is the maximum value of the slider?\n"))
    min = float(input("What is the minimum value of the slider?\n"))

    clear()

    return max, min

# <-------Antiroll Bars------->

def antiroll_bars():

    front_weight_per, rear_weight_per = get_weight_per()

    front_antiroll = (65.0-1.0) * front_weight_per + 1.0
    rear_antiroll = (65.0-1.0) * rear_weight_per + 1.0

    front_antiroll = format(front_antiroll, "0.2f") # Formatting the float to 2 decimal places
    rear_antiroll = format(rear_antiroll, "0.2f")

    print("<-------Antiroll Bars------->\n")
    print(f"Front: {front_antiroll} \nRear: {rear_antiroll}")

    menu_2()

# <-------Springs------->

def springs():

    max, min = get_max_min()
    front_weight_per, rear_weight_per = get_weight_per()

    front_springs = (max-min) * front_weight_per + min
    rear_springs = (max-min) * rear_weight_per + min

    front_springs = format(front_springs, "0.2f") # Formatting the float to 2 decimal places
    rear_springs = format(rear_springs, "0.2f")

    print("<-------Springs------->\n")
    print(f"Front: {front_springs}\nRear: {rear_springs}\n")

    print("<-------Ride Height------->\n")
    print("A good baseline is the second lowest option")

    menu_2()

# <-------Damping------->

def damping():

    max, min = get_max_min()
    front_weight_per, rear_weight_per = get_weight_per()

    front_rebound_stiff = (max-min) * front_weight_per + min
    rear_rebound_stiff = (max-min) * rear_weight_per + min

    front_bump_stiff = front_rebound_stiff * 0.6 # Bump Stiffness is equal to 60% of Rebound Stiffness
    rear_bump_stiff = rear_rebound_stiff * 0.6

    front_rebound_stiff = format(front_rebound_stiff, "0.2f") # Formatting the float to 2 decimal places
    rear_rebound_stiff = format(rear_rebound_stiff, "0.2f")

    front_bump_stiff = format(front_bump_stiff, "0.2f") # Formatting the float to 2 decimal places
    rear_bump_stiff = format(rear_bump_stiff, "0.2f")

    print("<-------Rebound Stiffness------->\n")
    print(f"Front: {front_rebound_stiff}\nRear: {rear_rebound_stiff}\n")

    print("<-------Bump Stiffness------->\n")
    print(f"Front: {front_bump_stiff}\nRear: {rear_bump_stiff}")

    menu_2()

# <-------Menu------->

def menu():

    while True:
        print("<-------Forza Horizon Tuning Calculator------->\n")

        print("(1) Antiroll Bars")
        print("(2) Springs")
        print("(3) Damping")
        print("\n(q) Close Application\n")

        print("What would you like to tune?: ")
        
        answer = input()
        clear()

        if answer == "1":
            antiroll_bars()
        elif answer == "2":
            springs()
        elif answer == "3":
            damping()
        elif answer.lower() == "q":
            print("Bye Bye...")
            break

def menu_2():

    while True:
        answer = input(f"\n\n(c) Continue\n")

        if answer.lower() == "c":
            clear()
            break

menu()