def get_bids():
    bids = {}
    while True:
        try:
            name = input("Enter your name: ")
            break
        except ValueError:
        
        while True:
            try:
                price = int(input("Enter your bid: $"))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Save data into dictionary {name: price}
        bids[name] = price
        
        should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if should_continue == 'no':
            break
    return bids

# Compare bids in dictionary using max
def find_highest_bidder(bidding_dictionary):
    winner = max(bidding_dictionary, key=bidding_dictionary.get)
    highest_bid = bidding_dictionary[winner]
    return winner, highest_bid

def main():
    bids = get_bids()
    winner, highest_bid = find_highest_bidder(bids)
    print(f"The bids are: {bids}, and the winner is {winner} with a bid of ${highest_bid}")

if __name__ == "__main__":
    main()
