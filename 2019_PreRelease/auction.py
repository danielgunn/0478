# This program helps an Auction company
# An auction company has an interactive auction board at their sale rooms, which allows buyers to place
# bids at any time during the auction. Before the auction starts, the sellers place their items in the sale
# room with a unique number attached to each item (item number). The following details about each item
# need to be set up on the interactive auction board system: item number, number of bids, description
# and reserve price. The number of bids is initially set to zero.
# During the auction, buyers can look at the items in the sale room and then place a bid on the interactive
# auction board at the sale room. Each buyer is given a unique number for identification (buyer number).
# All the buyer needs to do is enter their buyer number, the item number and their bid. Their bid must be
# greater than any existing bids.
# At the end of the auction, the company checks all the items and marks those that have bids greater
# than the reserve as sold. Any items sold will incur a fee of 10% of the final bid to be paid to the auction
# company.
print("===== Auction Setup - Sellers =====")

num_items = int(input("Number of items to sell:"))
while num_items < 0:
    print("invalid number")
    num_items = int(input("how many items will be sold?"))

bids = 0
reserve_price = [0]*num_items
description = [""]*num_items
highest_bid = [0] * num_items
sold = [False]*num_items

for i in range(num_items):
    print("-- Item",i+1," --")
    description[i] = input("Enter the description:")
    while (len(description[i]) < 1):
        print("Invalid description")
        description[i] = input("Enter the description:")
    reserve_price[i] = float(input("Enter the reserve price:"))
    while(reserve_price[i] < 0):
        print("Invalid price")
        reserve_price[i] = float(input("Enter the reserve price:"))

print("===== The Bidding ======")
i = -1
while(i != 0):
    for i in range(num_items):
        print(i+1,description[i],highest_bid[i])
    i = int(input("Enter item number or 0 to quit:"))
    while (i<0 or i>num_items):
        print("Invalid choice")
        i = int(input("Enter item number or 0 to quit:"))
    if i > 0:
        bid = float(input("Enter the bid amount:"))
        while(bid < highest_bid[i-1]):
            print("bid too low")
            bid = float(input("Enter the bid amount:"))
        highest_bid[i-1] = bid

print("==== The End of the Auction ====")
total_fee = 0.0
num_items_sold = num_items_underbid = num_items_nobid = 0
print("-- Sold Items --")
print("number\tprice\titem")
for i in range(num_items):
    if (highest_bid[i] >= reserve_price[i]):
        sold[i] = True
        total_fee += 0.1 * highest_bid[i]
        num_items_sold += 1
        print(i+1,"\t",highest_bid[i],"\t",description[i])
print("total fee:",total_fee)
print("-- Items that did not reached reserve price --")
print("Number\tBid\tItem")
for i in range(num_items):
    if (not sold[i] and highest_bid[i] > 0):
        print(i+1,"\t",highest_bid[i],"\t",description[i])
        num_items_underbid += 1
print("-- Items that received no bids -- ")
print("Number\tItem")
for i in range(num_items):
    if (not sold[i] and highest_bid[i] == 0):
        print(i+1,"\t",description[i])
        num_items_nobid += 1
print("-- Summary --")
print(num_items_sold, "items sold")
print(num_items_underbid,"items that did not meet the reserve price")
print(num_items_nobid,"items did not receive any bids")