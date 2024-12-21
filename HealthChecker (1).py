#Lists 
femaleusernames = []
maleusernames = []
femalepasswords = []
malepasswords = []
femaleweights = []
maleweights = []
tries = 0

def loginchoices():
    print("Login Successful!")
    while True:
        print(f"Welcome {username}!")
        print("1. BMI Calculator")
        print("2. Waist to Hip Ratio")
        print("3. Weight Tracker")
        print("4. Logout")
        choicelogin = input("Choose an option (1/2/3/4): ")
        if choicelogin == "1": # Open BMI Calculator
            BMI()
        elif choicelogin == "2": # Open Waist to Hip Ratio
            WaistHipRatio()
        elif choicelogin == "3": # Open Weight Tracker
            WeightTracker()
        elif choicelogin == "4": # Logout of the program
            print(f"You have been logged out. Thank you {username}")
            break
        else:
            print("Invalid Input, Please Try Again!")

def BMI():
    weight = float(input("What is your weight in kg? "))
    cm = float(input("What is your height in cm? "))
    height = cm/100 # Convert height to meters
    bmi = weight / (height ** 2) # To calculate the BMI
    print(f"Your BMI is: {bmi:.2f}")
    print("You are classified as:")
     # To clasify your BMI
    if 12 <= bmi < 18.5:
        print("Underweight.")
    elif 18.5 <= bmi < 25:
        print("Normal Weight.")
    elif 25 <= bmi < 30:
        print("Overweight.")
    elif 30 <= bmi < 40:
        print("Obese.")
    elif 40 < bmi < 64:
        print("Morbidly Obese.")
    else:
        print("BMI is not within chart classifications.")

def WaistHipRatio():
    if sex == "1": # For Male
        waist = float(input("What is your waist measurement in cm? "))
        hip = float(input("What is your hip measurement in cm? "))
        waisthipratio = waist / hip # Calculate Waist-to-Hip Ratio
        print(f"Your Waist-to-Hip Ratio is {waisthipratio:.2f}")
        print("You are classified as:")
        if 0.70 <= waisthipratio <= 0.80:
            print("Pear. You have low health risks.")
        elif 0.80 < waisthipratio < 0.85:
            print("Avocado. You have moderate health risks.")
        elif 0.85 < waisthipratio <= 0.98:
            print("Apple. You have high health risks.")
        else:
            print("Ratio is not within chart classifications.")
        return True
    elif sex == "2": # For Female
        waist = float(input("What is your waist measurement in cm? "))
        hip = float(input("What is your hip measurement in cm? "))
        waisthipratio = waist / hip
        print(f"Your Waist-to-Hip Ratio is {waisthipratio:.2f}")
        if 0.80 <= waisthipratio <= 0.95:
            print("Pear. You have low health risks.")
        elif 0.95 < waisthipratio < 1:
            print("Avocado. You have moderate health risks.")
        elif 1 < waisthipratio <= 1.15:
            print("Apple. You have high health risks.")
        else:
            print("Ratio is not within chart classifications.")
        return True
    else:
        print("Invalid Input, Please Try Again.")

def WeightTracker():
    if sex == "1": # For Male
        pastweight = maleweights[index]
        currentweight = float(input("What is your current weight in kg? "))
        weightdif = pastweight-currentweight # To Calculate weight difference
        # Display weight change information
        if weightdif == 0:
            print(f"Your past weight was {pastweight} and your current weight is {currentweight}.")
            print(f"There is no difference between your past and current weight.")
        elif weightdif < 0:
            print(f"Your past weight was {pastweight} and your current weight is {currentweight}.")
            print(f"You have gained {abs(weightdif):.2f} kg.")
        elif weightdif > 0:
            print(f"Your past weight was {pastweight} and your current weight is {currentweight}.")
            print(f"You have lost {weightdif} kg.")
        maleweights[index] = currentweight
    elif sex == "2": # For Female
        pastweight = femaleweights[index]
        currentweight = float(input("What is your current weight in kg? "))
        weightdif = pastweight-currentweight # To Calculate weight difference
         # Display weight change information
        if weightdif == 0:
            print(f"Your past weight was {pastweight} and your current weight is {currentweight}.")
            print(f"There is no difference between your past and current weight.")
        elif weightdif < 0:
            print(f"Your past weight was {pastweight} and your current weight is {currentweight}.")
            print(f"You have gained {abs(weightdif):.2f} kg.")
        elif weightdif > 0:
            print(f"Your past weight was {pastweight} and your current weight is {currentweight}.")
            print(f"You have lost {weightdif} kg.")
        femaleweights[index] = currentweight

while True:
    print("Welcome to your Health Checker!")
    print("1. BMI Calculator")
    print("2. Waist to Hip Ratio")
    print("3. Register")
    print("4. Login")
    print("5. Exit")
    choice = input("Choose an option (1/2/3/4/5): ")

    if choice == '1': # For BMI
        BMI()
    elif choice == '2': # For Waist to Hip Ratio
        while True:
            sex = input("What is your sex? (1 for Male, 2 for Female): ")
            if WaistHipRatio() == True:
                break
    elif choice == '3': # For Registration
        while True:
            username = input("Enter a username: ")
            if username in femaleusernames or username in maleusernames:
                print("Username already exists. Please choose a different username.")
            else:
                password = input("Enter a password: ")
                weight = float(input("Enter your weight in kg: "))
                while True:
                    sex = input("Are you male or female? (1 for Male, 2 for Female): ")
                    if sex == "1":
                        maleusernames.append(username)
                        malepasswords.append(password)
                        maleweights.append(weight)
                        print("Registration successful!")
                        break
                    elif sex == "2":
                        femaleusernames.append(username)
                        femalepasswords.append(password)
                        femaleweights.append(weight)
                        print("Registration successful!")
                        break
                    else: 
                        print("Invalid Input, Please Try Again.")
                break
    elif choice == '4': # Login
        username = input("Enter your username: ")
        if username in maleusernames:
            index = maleusernames.index(username)
            while True:
                password = input("Enter your password: ")
                if malepasswords[index] == password:
                    sex = "1"
                    loginchoices()
                    break
                elif tries == 2:
                    print("Incorrect password. You will be returned to the Menu.")
                    tries=0
                    break
                else:
                    tries += 1
                    print(f"Incorrect password. You have {3-tries} tries left.")
        elif username in femaleusernames:
            index = femaleusernames.index(username)
            while True:
                password = input("Enter your password: ")
                if femalepasswords[index] == password:
                    sex = "2"
                    loginchoices()
                    break
                elif tries == 2:
                    print("Incorrect password. You will be returned to the Menu.")
                    tries=0
                    break
                else:
                    tries += 1
                    print(f"Incorrect password. You have {3-tries} tries left.")
        else:
            print("Username not found. Register your Username before logging in.")


    elif choice == '5': # Exit
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")