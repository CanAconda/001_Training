import random as rd

# The Dice Game Simulator

# Features: 
# -Random Number 
# -ASCII Graphic output
# -User input

# Dice layout:

# [---------]  11 ->
# [ 0     0 ]   
# [    0    ]   | 5
# [ 0     0 ]   v
# [---------]


while True:
    
    # Create Dice Layout in a matrix with num_rows x num_cols 
    # (If this part is not inside the while loop the previous dice layout will not be overwritten)
    num_rows = 5             
    num_cols = 11
    matrix = [[" " for m in range(num_cols)] for n in range(num_rows)]
    
    for i in range(5):
        matrix[i][0] = "["  # Enter row 0-5 and overwirte the first element [0]
        matrix[i][10] = "]"  # Enter row 0-5 and overwrite the last element[cols -1]

    for j in range(1, 10):
        matrix[0][j] = "-"
        matrix[4][j] = "-"

    answer = input("\n Would you like to role the dice? [y]/[n]: ")
    num_dice = rd.randrange(1, 6)    #Random number form Random Lib
    
    if (answer == "y"):
        # Convert Random number into dice eyes
        if (num_dice % 2 != 0):     # Only for the number 1,5,3 the center point is needed
            matrix[2][5] = 0       
        if (num_dice>1):
            matrix[1][2] = 0        # Only for the number 1,5,3 (Odd numbers)
            matrix[3][8] = 0        # Only for the number 2, 4, 6 (even numbers)
        if (num_dice>3):
            matrix[1][8]=0
            matrix[3][2]=0
        if (num_dice==6):
            matrix[2][2]=0
            matrix[2][8]=0
            

        # Print matrix in correct oder

        for p in range(num_rows):
            print("\r")
            for k in range(num_cols):
                print(matrix[p][k], end="")
    elif(answer== "n"):             #User quit the game
        break
    else:
        answer = input("Would you like to role the dice? [y]/[n]: ")    #user enters a different letter than "y" or "n"

