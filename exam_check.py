medical_cause = input("Did you have a medical cause: Yes or No?")

attendance = int(input("Enter the attendance of the student:"))

if medical_cause == 'Yes':
    print("You're medical cause is Okay!")

else:
    if attendance >= 75:
        print("Allowed.....Barely")
    else:
        print("Not Allowed!")