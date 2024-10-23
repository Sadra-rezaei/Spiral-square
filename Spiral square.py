n = int(input())

matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(0)


counter = 1
floatingScale_X = n
floatingScale_Y = 0


while counter <= n*n:
    
    # move right to left:
    i = floatingScale_X - 1
    for j in range(floatingScale_Y, floatingScale_X):
        matrix[i][j] = counter
        counter += 1
    
    
    # move down to up:
    j = floatingScale_X - 1
    for i in range(floatingScale_X - 2, floatingScale_Y - 1, -1):
        matrix[i][j] = counter
        counter += 1


    # move left to right:
    i = floatingScale_Y
    for j in range(floatingScale_X - 2, floatingScale_Y - 1, -1):
        matrix[i][j] = counter
        counter += 1


    # move up to down:
    j = floatingScale_Y
    for i in range(floatingScale_Y + 1, floatingScale_X - 1):
        matrix[i][j] = counter
        counter += 1

    floatingScale_X -= 1
    floatingScale_Y += 1


# print Matrix
for t in range(n):
    for p in range(n):
        print(matrix[t][p], end=" ")
    print()