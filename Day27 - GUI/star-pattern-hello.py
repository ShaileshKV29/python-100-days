for i in range(1, 6):
    for j in range(1, 30):
        if i == 1:
            if j == 1 or j == 5:
                print("*", end="")
            elif j in (6,12,18,24):
                print(" ", end="")
            elif j in range(7, 12):
                print("*", end="")
            elif j == 13 or j == 19:
                print("*",end="")
            elif j in range(25, 30):
                print("*", end="")
            else:
                print(" ",end="")

        elif i == 2 or i == 4:
            if j == 1 or j == 5:
                print("*", end="")
            elif j in (6,12,18,24):
                print(" ", end="")
            elif j == 7:
                print("*", end="")
            elif j == 13 or j == 19:
                print("*",end="")
            elif j == 25 or j == 29:
                print("*", end="")
            else:
                print(" ",end="")
        
        elif i == 3:
            if j in range(1, 6):
                print("*", end="")
            elif j in (6,12,18,24):
                print(" ", end="")
            elif j in range(7, 12):
                print("*", end="")
            elif j == 13 or j == 19:
                print("*",end="")
            elif j == 25 or j == 29:
                print("*", end="")
            else:
                print(" ",end="")

        elif i == 5:
            if j == 1 or j == 5:
                print("*", end="")
            elif j in (6,12,18,24):
                print(" ", end="")
            elif j in range(7, 12):
                print("*", end="")
            elif j in range(13, 24):
                print("*",end="")
            elif j in range(25, 30):
                print("*", end="")
            else:
                print(" ",end="")
    print() 

