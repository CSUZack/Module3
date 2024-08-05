#recursive function to ask for a valid integer and to ask for a retry on any value error
def inputValidFloat(prompt, retries=5):
    if retries <= 0:
        print("Too many failures in user input, aborting.\n")
        exit()
    try:
        return float(input(prompt))
    except ValueError:
        print("Something was wrong with that input, please try again.\n")
        retries -=1
        return inputValidFloat(prompt, retries)

subtotal = inputValidFloat("Please enter the cost of the meal.\n")
tip = subtotal * 0.18
salesTax = subtotal * 0.07

print(f"""
SUBTOTAL:       $ {subtotal:.2f}
TIP(18%):       $ {tip:.2f}
SALES TAX(7%):  $ {salesTax:.2f}
TOTAL:          $ {subtotal + tip + salesTax:.2f}
""")


