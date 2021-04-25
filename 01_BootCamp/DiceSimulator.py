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


FstSymbol = "["
LstSymbol ="]"
LineSymbol ="-"

num_rows = 5
num_cols = 11
matrix = [[0 for m in range(num_cols)] for n in range(num_rows)]
for i in range(5):
    matrix[i][0] = "["             #Enter row 0-5 and overwirte the first element [0]
    matrix[i][10] = "]"            #Enter row 0-5 and overwrite the last element[cols -1]
print(matrix)

# for i in range(5):
#     print("\n")
#     if (i>1 and i<5):
#         Printsymbol = "+"
#     else:
#         Printsymbol = LineSymbol
    
#     for j in range (10):
#         matrix = [[i], j]
#         print(Printsymbol, end="")

