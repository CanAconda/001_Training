# The Dice Simulator

# Features: 
# -Random Number 
# -ASCII Graphic output
# -user input


# [---------]  11 ->
# [ 0     0 ]   
# [    0    ]   | 5
# [ 0     0 ]   v
# [---------]


#Create Dice Layout in matrix

num_rows = 5
num_cols = 11
matrix = [[" " for m in range(num_cols)] for n in range(num_rows)]
for i in range(5):
    matrix[i][0] = "["             #Enter row 0-5 and overwirte the first element [0]
    matrix[i][10] = "]"            #Enter row 0-5 and overwrite the last element[cols -1]

for j in range(1,10):
    matrix[0][j] = "-"
    matrix[4][j] = "-"
print(matrix)

# Print matrix in correct oder

for p in range(num_rows):
    print("\r")
    for k in range(num_cols):
        print(matrix[p][k], end="")



