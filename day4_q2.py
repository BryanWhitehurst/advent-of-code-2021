
def changeStatus(val, board, markedBoard):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == str(val): markedBoard[i][j] = True

def checkWinner(board):
    #check for row of all True's
    for row in board:
        for i in range(5):
            if not(row[i]): break #not a winner, go to next row
            if(row[i] and i == 4): return True

    #check for col of all True's
    for i in range(5):
        for j in range(5):
            if not(board[j][i]): break #not a winning col, go to next col
            if board[j][i] and j == 4: return True
    
    return False

def sumUnmarked(board, marked):
    sum = 0

    for i in range(5):
        for j in range(5):
            if not marked[i][j]: sum += int(board[i][j])
    return sum
    
def bingo(bingoInput, boards):
    numBoards = len(boards)
    winners = [False] * numBoards
    numWinners = 0
    marked = []
    for i in range(len(boards)):
        marked.append([[False for i in range(5)] for j in range(5)])
    
    for val in bingoInput:
        for i in range(len(boards)):
            if not winners[i]: changeStatus(val, boards[i], marked[i])
        
        for i in range(len(boards)):
            #check to see if board wins
            if winners[i]: continue

            if checkWinner(marked[i]) and numWinners == numBoards - 1:
                return int(val) * sumUnmarked(boards[i], marked[i])
            
            if checkWinner(marked[i]):
                winners[i] = True
                numWinners += 1


f = open("input.txt", "r")
bingoInput = f.readline().strip() #get rid of newLine
bingoInput = bingoInput.split(",") #convert to list

#boards
#array of 2D board arrays
boards = []
curBoard = []

f.readline()
i = 0
for x in f:
    if x != "\n":
        curBoard.append(x.strip().split())
        i += 1
    if(i == 5):
        i = 0
        boards.append(curBoard)
        curBoard = []

print(bingo(bingoInput, boards))