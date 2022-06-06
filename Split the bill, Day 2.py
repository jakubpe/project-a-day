#Split the bill
print("Welcome to the tip calculator")
bill = float(input("What was the total bill?"))
tip = float(input("What percentage tip would you like to give?"))
people = int(input("How many peple to split the bill between?"))
bill_per_person = round(bill * (1 + tip / 100) / people, 2)
bill_per_person = "{:.2f}".format(bill_per_person)
print("Everybody will have to pay $", bill_per_person)
