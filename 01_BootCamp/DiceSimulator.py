# The Dice Simulator

# Features: 
# -Random Number 
# -ASCII Graphic output
# -user input


# [---------]  11 ->
# [         ]   
# [         ]   | 5
# [         ]   v
# [---------]

FstSymbol = "["
LstSymbol ="]"
LineSymbol ="-"

for i in range(5):
    print("\n")
    if (i>1 and i<5):
        Printsymbol = "+"
    else:
        Printsymbol = LineSymbol
    
    for j in range (10):
        print(Printsymbol, end="")
