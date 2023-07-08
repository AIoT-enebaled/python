# Define a function named wear
def wear():
    # Ask the user to input the weather for the day
    weather = input("Please enter the weather of the day to get what to wear (sunny, cloudy, rainy or windy): ")
    print("Your weather today is ",weather)
    
    # Check the weather condition and suggest appropriate clothing
    if weather == "sunny":
        print("You should wear light clothes.")
    elif weather == "cloudy":
        print("Wear heavy clothes as it's going to be a bit cold outside.")
    elif weather == "rainy":
        print("Go with a jacket, an umbrella or most definitely travel by car.")
    elif weather == "windy":
        print("Stay indoors if possible, wear heavy clothes to protect you from the strong winds outside.")
    else:
        print("We don't have that weather in Uganda.")
    
    # Ask the user if they want to check the weather again
    check_again = input("Do you want to check the weather again? (y/n)").lower()
    
    # Start a while loop to keep checking the weather if the user wants to
    while check_again == 'y':
        # Ask the user to input the weather for the day
        weather = input("Please enter the weather of the day to get what to wear (sunny, cloudy, rainy or windy): ")
        print("Your weather today is ",weather)
        
        # Check the weather condition and suggest appropriate clothing
        if weather == "sunny":
            print("You should wear light clothes.")
        elif weather == "cloudy":
            print("Wear heavy clothes as it's going to be a bit cold outside.")
        elif weather == "rainy":
            print("Go with a jacket, an umbrella or most definitely travel by car.")
        elif weather == "windy":
            print("Stay indoors if possible, wear heavy clothes to protect you from the strong winds outside.")
        else:
            print("We don't have that weather in Uganda.")
        
        # Ask the user if they want to check the weather again
        check_again = input("Do you want to check the weather again? (y/n)").lower()
    
    # Print a message thanking the user for using the program
    print("Thank you for using the weather checker!")

# Call the wear function to start the program
wear()
