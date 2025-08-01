# get the chest size from user
# evaluate to find the size...small, med, etc
# print the result for the user

print("\n*** Shirt Sizer ***")
chest = int(input("\nWhat is the chest size in inches? "))
text = "Your shirt size is:"

if chest <= 38:
    print(f"\n{text} S \n")    
elif chest >= 39 and chest <= 41:
    print(f"{text} M \n")    
elif chest >= 42 and chest <= 44:
    print(f"{text} L \n")
elif chest >= 45 and chest <= 47:
    print(f"{text} XL \n")   
elif chest >= 48 and chest <= 50:
    print(f"{text} XXL \n")   
elif chest >= 51 and chest <= 53:
    print(f"{text} XXXL \n")      