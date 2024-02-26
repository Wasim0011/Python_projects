import os   #for accessing screen clear
print("************ Welcome to the Silent Auction Program ************")
def find_winner(bidding_details):
    highestBid=0;
    winner=""
    for bidder in bidding_details:
        if bidding_details[bidder]>highestBid:
            highestBid=bidding_details[bidder]
            winner=bidder
    print(f"Here is the details of all the bidders: {bidding_details}")
    print(f"The Winner is {winner} with a bid price of {highestBid}")

bidder_data={}  #creating empty dictionary
end_of_bidding=False;
while not end_of_bidding:
    name=input("What is your name? ")
    price=int(input("What is your bid? "))
    bidder_data[name]=price #storing details in dictionary
    more_bidder=input("Are there more bidders? Type 'Yes' or 'No'").lower()
    if more_bidder=='yes':
        os.system('cls')    #to clear screen
    else:
        end_of_bidding=True;
        find_winner(bidder_data)

