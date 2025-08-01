# This program calculates the volume of a sphere. 
pi = 3.14159
radius = float(input("What is the radius of the sphere? "))

volume = (4/3) * pi * radius**3
print("\n*** Sphere Volume ***")
print()
# print("Given a sphere is a radius of", radius)
print(f"Given a sphere with a raduis of {radius},")
# print("The volume of the sphere is", volume, "units\u00B3")
print(f"The volume of the sphere is {volume:.1f} units\u00B3")
print()
