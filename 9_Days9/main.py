# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compared bids in dictionary

from art import logo



bids = {}
continue_bidding = True

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print("\n" * 20)
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
    print(logo)


while continue_bidding:
    name = input("What's your name?: ")
    price = float(input("What is your bid?: $"))
    bids[name] = price
    should_continue = str(input("is there any other users who want to bid? (yes or no):\n"))
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)


