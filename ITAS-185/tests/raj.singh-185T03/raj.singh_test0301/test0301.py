import classes.Orca as o
import classes.Humpback as h

def main():
    # Create a list of whale objects
    whales = []
    whales.append(o.Orca("Big Momma", 10, 10, "pod302.4"))
    whales.append(o.Orca("Big Momma", 10, 10, "pod302.4"))
    whales.append(h.Humpback("Pete", 30, 30, 16))
    whales.append(o.Orca("Big Pappy", 5, 12, "pod302.4"))
    whales.append(o.Orca("Stripey", 16, 11, "pod302.4"))
    whales.append(h.Humpback("Quicksilver", 16, 30, 9))
    whales.append(h.Humpback("Quicksilver", 16, 30, 9))
    whales.append(h.Humpback("Hanoi", 33, 27, 17))
    whales.append(h.Humpback("Big Boy", 9, 29, 8))

    # display the number of whales created
    print (f'{o.Orca.count} whales have been created')
    print()

    # loop and print out hte waits and what they eat and sing
    for whale in whales:
        print(str(whale))
        print(f"{whale.name} sings {whale.sing()}")
        if whale.__class__.__name__ == "Orca":
            whale.eat("manta ray")
        else:
            whale.eat("krill")
        print() 

    # compare some of the whales to see if they are the same or not
    if whales[0] == whales[1]:
        print("The first two whales are the same")
    else:
        print("The first two whales are different")

    if whales[3] == (whales[4]):
        print("The third and fourth whales are the same")
    else:
        print("The third and fourth whales are different")

    if whales[-1] == (whales[-2]):
        print("The last two whales are the same")
    else:
        print("The last two whales are different")

    if whales[-3] == (whales[-4]):
        print("The third and fourth last whales are the same")
    else:
        print("The third and fourth last whales are different")

# Only run this program if it is the running program
if __name__ == "__main__":
    main()
