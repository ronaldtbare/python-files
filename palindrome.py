# This program checks strings to see if they are palindromes
# Palindromes are the strings that are the same forwards and backwards

def reverse_it(my_text):
    #This is the function to reverse the string
    global reversed_text
    reversed_text = my_text[::-1].lower()
    return reversed_text
print("**** Palindromes ****")
print()
my_text = input("Enter a string to test if it is a palindrome. \n")

# This strips away the punctuation
my_text = my_text.replace(".","").replace("!","").replace("?","").replace("!","").replace(" ","")
 

reverse_it(my_text)

print("Enterd text: ",my_text)
print("Reversed text: ",reversed_text)

if my_text.lower() == reversed_text.lower():
    print("This is a palindrome.")
else:
    print("This is NOT a palindrome.")


