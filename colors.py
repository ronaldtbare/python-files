# This program tells the user
# about the meaning of their 
# favorite color. 

# Ask the user to input their fav color
# decide which meaning to print
# print the meaning of the color

# Title
print("\n   * Color Meanings *\n")

# Get user input
color = input("What is your favorite color? ").lower()

print(f"Your favorite color is {color}.")

# color descriptions
red = f"""Passion, urgency and energy. Often 
used to grab attention, red can stimulate
excitement, which is why the color is 
sometimes used in Call To Action buttons. Think: 
Buy now! Flash sale!"""

orange = f"""Warmth and vitality. Orange 
merges the energy of red and the cheerfulness 
of yellow to invite positivity and creativity."""

yellow = f"""Optimism and creativity. While 
yellow evokes happiness, overuse can provoke 
anxiety or visual fatigue, especially when 
paired with other high contrast colors like 
black (see: caution tape)."""

green = f"""Growth, health and tranquility. 
Associated with nature, green appeals to 
brands with eco-friendly or wellness-oriented 
missions."""

blue = f"""Trust, calm and professionalism. 
Widely regarded as calm and reliable, blue 
branding is a go-to for industries like 
finance and healthcare. Banking apps like 
PayPal or Chase, use blue as their primary 
brand color because users transfer their 
feelings of reliability and safety to the 
interface, even before interacting with 
the features."""

purple = f"""Luxury, mystery and imagination. 
Purple’s royal associations trace all the way 
back to Roman times, which makes it ideal for 
premium or luxury brands. It could also be 
well suited for brands that want to tap 
into its associations with magic, 
fantasy or creativity. (Here’s how Gen-Z 
purple became the new Millennial pink.)"""

# decision making

if color == "red":
    print(f"\nThe description for {color} is: \n")
    print(red)

elif color == "orange":
    print(f"\nThe description for {color} is: \n")
    print(orange)

elif color == "yellow":
    print(f"\nThe description for {color} is: \n")
    print(yellow)

elif color == "green":
    print(f"\nThe description for {color} is: \n")
    print(green)

elif color == "blue":
    print(f"\nThe description for {color} is: \n")
    print(blue)

elif color == "purple":
    print(f"\nThe description for {color} is: \n")
    print(purple)

else:
    print("This color is not in our database.")


print()


