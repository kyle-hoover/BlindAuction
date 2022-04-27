import os
from art import logo

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear') #function to clear the console

bidders = {}

more_bidders = True

def bidding_function():
#Show the logo
    print(logo)
#Ask for name input
    name = input("What is the bidders name?\n")
#Ask for Bid Price
    bid = int(input("What is the bidders price?\n"))
#Add Name and Bid into a dictionary as the key and value
    bidders[name] = bid    

#While there are still bidders, clear the screen and run again
while more_bidders == True:
    clearConsole()
    bidding_function()
    #Asks if there are any other bidders
    add_bidders = input("Are there any other bidders? (Y/N)\n").upper()
    if add_bidders == "N":
        more_bidders = False

#Find the highest bid in the dictionary and declare them the winner
clearConsole()
winning_bid = 0
winning_bidder = "Nobody"

for x in bidders:
    if bidders[x] > winning_bid:
        winning_bid = bidders[x]
    if bidders[x] == winning_bid:
        winning_bidder = x

print(logo)
print(f"The winner is {winning_bidder} with a bid of ${winning_bid}!")
