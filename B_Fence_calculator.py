# Ask user for values and loop until they
# Enter a value more than zero

def num_check(question):
    error = "please enter a number that is more that zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print("please enter a number that is more than zero")

        except ValueError:
            print(error)


# Main code starts here

keep_going = ""
while keep_going == "":
    # Get width and height, must be numbers more than zero
    width = num_check("Width: ")
    length = num_check("Length: ")
    cost = num_check("Cost: ")

    # calculate area / perimeter
    perimeter = 2 * (width + length)
    cost = perimeter * cost

    # display output
    print()
    print(f"perimeter: {perimeter} units")
    print(f"Cost: ${cost}")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit.")
    print()

    print("Thank you for using the Fence calculator")
