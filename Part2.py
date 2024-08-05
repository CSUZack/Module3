#recursive function to ask for a valid integer and to ask for a retry on any value error
def InputValidInt(prompt, retries=5):
    if retries <= 0:
        print("Too many failures in user input, aborting.\n")
        exit()
    try:
        return int(input(prompt))
    except ValueError:
        print("Something was wrong with that input, please try again.\n")
        retries -=1
        return InputValidInt(prompt, retries)
    
num1 = InputValidInt("Please enter the current time in 24hr format.\n")
num2 = InputValidInt("Please enter the number of hours until the alarm goes off.\n")

print((num1 + num2) % 24)