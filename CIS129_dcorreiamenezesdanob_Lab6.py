# Diego Nobrega
# Lab6

def main():

    # Import math library
    import math

    # Declare hot dogs and hot dog buns
    DOGS = 10
    BUNS = 8

    # Get the number of people attending the cookout
    people = int(input('Enter the number of people attending the cookout: '))

    # Get the number of hot dogs each person will be given
    hotDogs = int(input('Enter the number of hot dogs for each person: '))

    # Number of hot dogs needed
    total = people * hotDogs
    minDogs = math.ceil(total / DOGS)

    # Number of hot dog buns needed
    minBuns = math.ceil(total / BUNS)

    print(f"Minimum packages of hot dogs needed {minDogs} ")
    print(f"Minimum packages of hot dog buns needed {minBuns} ")

    # Number of left over hot dogs
    dogsLeft =total % DOGS
    if dogsLeft != 0:
        print(f'Hot dogs left over {dogsLeft} ')

    # Number of left over hot dog buns
    bunsLeft = total % BUNS
    if bunsLeft != 0:
        print(f'Hot dog buns left over {bunsLeft} ')
main()
