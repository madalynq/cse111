import math

width = int(input("Enter the width of the tire in mm (ex 205): "))
ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * width ** 2 * ratio * (width * ratio + 2540 * diameter)) / 10000000000

print(f"The approximate volume is {volume:.2f} liters.")





from datetime import datetime
current_date_and_time = datetime.now(tz=None)

with open("volumes.txt", mode="at") as volumes_file:
    print(f"{current_date_and_time: %Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}", file=volumes_file)


#extra
done = False

while not done:
    user_answer = input("Would you like to buy tires that match your tire dimensions? Enter '1' for yes, or '2' for no: ")
    if user_answer == "2":
        print("Have a good day!")
        done = True
    elif user_answer == "1":
        phone = input("Please enter your phone number with no spaces, hyphens, or parethesis, and we will reach out to you with tires that match your dimensions (ex 2093334455): ")
        if len(phone) == 10:
            print("Thank you, we will reach out to you shortly.")
            with open("volumes.txt", mode="at") as volumes_file:
                print(phone, file=volumes_file)
            done = True
        else:
            print("Invalid input, please try again.")
    else:
        print("Invalid input, please try again.")
