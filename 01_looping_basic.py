# function goes here

# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:

            error = "Please enter a number that is more than zero."

            try:
                 # ask the user to enter a number
                 response = float(input(question))

                 # check if the number is more than zero
                 if response > 0:
                      return response

                 # outputs error if input is invalid
                 else:
                     print(error)
                     print()

            except ValueError:
                print(error)


# Main Routine goes here
width = num_check("width: ")
height = num_check("height: ")
print()
print("width", width)
print("height", height)
print()

# checks the users enter a number more than zero