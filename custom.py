print("Select your ride!")
print("1. Bike")
print("2. Car")

choice = int(input("Choose:"))

if (choice == 1):
    print("What type of bike?")
    print("1. Scooter")
    print("2. Motorbike")

    if choice2==1:
        print("You have selected scooter!")
    else:
        print("You chose motorbike!")

elif (choice==2):
    print("What type of car?")
    print("1.Suzuki")
    print("2.Toyota")
    
    if choice3==1:
        print("You have chosen Suzuki!")
    else:
        print("You have chosen Toyota!")

else:
    print("Wrong Choice!")