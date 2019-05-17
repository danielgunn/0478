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
    print("-- Item ---",i+1)
    description[i] = input("Enter the description:")
    while (len(description[i]) < 1):
        print("Invalid description")
        description[i] = input("Enter the description:")
    reserve_price[i] = float(input("Enter the reserve price:"))
    while(reserve_price[i] < 0):
        print("Invalid price")
        reserve_price[i] = float(input("Enter the reserve price:"))

print("===== The Bidding ======")
bidding = True
while(bidding):
    for i in range(num_items):
        print(i+1,description[i],highest_bid[i])
    i = int(input("Enter item number or 0 to quit:"))
    while (i<0 or i>num_items+1):
        print("Invalid choice")
        i = int(input("Enter item number or 0 to quit:"))
    if i == 0:
        bidding = False
    else:
        i = i-1
        bid = float(input("Enter the bid amount:"))
        while(bid < highest_bid[i]):
            print("bid too low")
            bid = float(input("Enter the bid amount:"))
        highest_bid[i] = bid
        if bid > reserve_price[i]:
            sold[i] = True

print("==== The End of the Auction ====")
total_fee = 0.0
num_items_sold = num_items_underbid = num_items_nobid = 0
print("-- Sold Items --")
print("number\tprice\titem")
for i in range(num_items):
    if (highest_bid[i] > reserve_price[i]):
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