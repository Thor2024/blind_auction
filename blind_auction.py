from replit import clear

from art import logo
print(logo)

#adding empty dictionary
names_bids = {}
bidding_finished = False

print("Welcome to the blind auction - you look well.")

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  #looping through dictionary
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $" ))
  #adding to dictionary
  names_bids[name] = bid
  other_users = input("Are there other users who want to bid? Y or N \n").lower()
  if other_users == "n":
    bidding_finished = True
    find_highest_bidder(names_bids)
  elif other_users == "y":
    clear()