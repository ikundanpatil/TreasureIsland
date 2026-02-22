print("Welcome To Python Pizza Deliveries: ")
size = input("What Size Of Pizza Do You Want? S, M, or L : ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You Typed wrong Input")

pepperoni = input("Do You Want Pepperoni On Your Pizza? (Y or N): ")

if pepperoni =="Y":
    if size =="S":
        bill += 2
    else:
        bill += 3

extra_chesse = input("Do You Want Extra Cheese? (Y or N): ")

if extra_chesse == "Y":
    bill += 1


print(f"Your Bill Is: {bill}")