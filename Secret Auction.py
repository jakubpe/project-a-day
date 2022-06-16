import os
clear = lambda: os.system('cls')
Continue = True
Book = {}
print("Welcome to the secret auction")
while Continue:
    Name = input("What is your name?: ")
    Bid = int(input("What is your bid?: "))
    Book[Name] = Bid
    if input("Are there any other bidders? Type 'yes' or 'no'") == 'no':
        Continue = False
        clear()
    clear()
highest_bid = 0
highest_bidder = str
for key in Book:
    if Book[key] > highest_bid:
        highest_bid = Book[key]
        highest_bidder = key
print("The winner is {} with a bid of ${}".format(highest_bidder, highest_bid))