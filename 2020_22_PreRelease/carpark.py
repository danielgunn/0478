day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
max_stay = [8,2,2,2,2,2,4]
price_per_hour = [2,10,10,10,10,10,3]

def get_parking_payment():
    arrival = -1
    while (arrival < 8) or (arrival > 24):    # range check!
        arrival = int(input("What time is it?"))
        if (arrival < 8) or (arrival > 24):
            print("No, invalid time!")

    stay = -1
    while (stay < 1 or stay > max_stay[day_index]):
        msg = "How long will you stay (1-" + str(max_stay[day_index]) + ")?"
        stay = int(input(msg))

    f_pnum = ""
    while (len(f_pnum) != 5):
        f_pnum = input("Enter the frequent parking number")
        if len(f_pnum) != 5:
            print("Invalid number, try again")

    total = 0
    for i in range(len(f_pnum) - 1):
        total += int(f_pnum[i]) * (i+1)

    check = total % 11

    if check == int(f_pnum[-1:]):
        print("Frequent parking number approved!")
        if (arrival) < 16:
            discount = 0.1
        else:
            discount = 0.5
    else:
        print("Frequent parking number rejected")
        discount = 0

    if arrival < 16:
        if arrival + stay > 16:
            price = (16 - arrival) * price_per_hour[day_index] + 2
        else:
            price = stay * price_per_hour[day_index]

    else:
        price = 2

    price -= price*discount

    print("You owe", price)

    payment = -1
    while (payment < price):
        payment = int(input("How much do you pay?"))
        if (payment < price):
            print("Not paid enough")

    return payment


# Validation
day_index = -1
while( day_index == -1):
    day = input("What day is it today? (e.g Monday):")
    for i in range(len(day_names)):
        if day == day_names[i]:
            day_index = i
    if day_index == -1:
        print("Invalid day. Try again YOU FOOL!")

total = 0
while True:
    print("Today is ", day_names[day_index])
    quit = input("Press Enter to add a payment for today, Q to quit:")
    if quit != "Q":
        total += get_parking_payment()
    else:
        break

print("Total for today is ", total)