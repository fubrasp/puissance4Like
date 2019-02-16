def display_board(gameBoard):
    print("\n")
    for i in range(len(gameBoard)):
        for j in range(len(gameBoard[i])):
            print(gameBoard[i][j], end=' ')
        print()
    print("\n")
