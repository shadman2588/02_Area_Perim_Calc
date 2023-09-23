# function goes here 

# check if number is more than zero 
def num_check(question):
    valid = False 
    while not valid:

        error = "Please enter a number more than zero."

        try:
            # ask the user to enter a number 
            respond = float(input(question))

            # check if the number is more than zero
            if respond > 0:
                return respond

            # outputs error if input is valid 
            else: 
                print(error)
                print()

        except ValueError:
            
            print(error)
        
# Main routine goes here 

# Starting statment 
print()
print("<<<<Fence Calculator>>>>")
print()

keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    length = num_check("Length: ")
    cost_per_m = num_check("Cost/m: ")

    # Calculate Perimeter (width + height) x 2 
    perimeter = 2 * (width + length)

    # Calculate Fence price 
    fence = perimeter * cost_per_m

    # Otuput Perimeter and Fence price 
    print("Perimeter: {}m" .format(perimeter))
    print("Fence: ${}" .format(fence))
    print()

    keep_going =  input("Press <enter> to keep going or any key to quit.")

print()
print("Thanks for useing Fence Calculator.😊")

        



