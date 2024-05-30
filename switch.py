# Match(switch) requires python 3.10 or greater

direction = input("Which direction? ").lower()

match direction:
    case "north" or "n":
        print("up")
    case "sorth" or "s":
        print("down")
    case "east" or "e":
        print("right")
    case "west" or "w":
        print("left")
    case _: # if no other cases match
        print("Invalid direction.")