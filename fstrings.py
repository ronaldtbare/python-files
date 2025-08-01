name = "NIFTY"
price = 19500
formatted_string = f"The current index of {name} is {price}."
print(formatted_string)

float_variable = 3.141592653589793
print(f"{float_variable:.2f}")
# output is 3.14

money = 3_142_671.76 
# This is the same as 3142671.76
print(f"${money:,.2f}") # currency

# Output length of 20, and pad the rest with zeros. 
int_variable =  1_234_567
print(f"{int_variable:020}")
# 00000000000001234567

# Output length of 24, and pad the rest with zeros. 
int_variable =  30
print(f"{int_variable:024}")
# 000000000000000000000030

# Output length of 10, and pad the rest with leading whitespace
int_variable = 20_21
print(f"{int_variable:10d}")

# Output length of 5, and pad the rest with leading whitespace
int_variable = 20_21
print(f"{int_variable:5d}")

# Output 20 asterisks, change any asterisk to any character
pet = "Rufus"
print(f"{pet:*<20}")
print(f"{pet:*>20}")
print(f"{pet:*^20}")
