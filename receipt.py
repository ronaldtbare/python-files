
item1_name = input("What is Item1: ")
item1_cost = float(input("Enter cost of item 1: "))

item2_name = input("What is Item2: ")
item2_cost = float(input("Enter cost of item 2: "))

item3_name = input("What is Item3: ")
item3_cost = float(input("Enter cost of item 3: "))

total = item1_cost + item2_cost + item3_cost 

print("\n*** Receipt ***")
print()

print(f"{item1_name}          {item1_cost}")
print(f"{item2_name}           {item2_cost}")
print(f"{item3_name}           {item3_cost}")
print("-" * 20)
print(f"Total          {total}\n")

