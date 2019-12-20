# Python and Applications to Business Analytics Fall 2018, Module 1
# Assignment3
# Author: Ran Dou, Qimo Li

#import random package
import random

#define a empty space in the format of 6x7
def drawspace(space):
    print('   |   |   |   |   |   |')
    print(' ' + space[36] + ' | ' + space[37] + ' | ' + space[38] + ' | ' + space[39] + ' | ' + space[40] + ' | ' + space[41]+ ' | ' + space[42])
    print('   |   |   |   |   |   |')
    print('------------------------------------')
    print('   |   |   |   |   |   |')
    print(' ' + space[29] + ' | ' + space[30] + ' | ' + space[31] + ' | ' + space[32] + ' | ' + space[33] + ' | ' + space[34]+ ' | ' + space[35])
    print('   |   |   |   |   |   |')
    print('------------------------------------')
    print('   |   |   |   |   |   |')
    print(' ' + space[22] + ' | ' + space[23] + ' | ' + space[24] + ' | ' + space[25] + ' | ' + space[26] + ' | ' + space[27]+ ' | ' + space[28])
    print('   |   |   |   |   |   |')
    print('------------------------------------')
    print('   |   |   |   |   |   |')
    print(' ' + space[15] + ' | ' + space[16] + ' | ' + space[17]+ ' | ' + space[18]+ ' | ' + space[19]+ ' | ' + space[20]+ ' | ' + space[21])
    print('   |   |   |   |   |   |')
    print('------------------------------------')
    print('   |   |   |   |   |   |')
    print(' ' + space[8] + ' | ' + space[9] + ' | ' + space[10]+ ' | ' + space[11]+ ' | ' + space[12]+ ' | ' + space[13]+ ' | ' + space[14])
    print('   |   |   |   |   |   |')
    print('------------------------------------')
    print('   |   |   |   |   |   |')
    print(' ' + space[1] + ' | ' + space[2] + ' | ' + space[3]+ ' | ' + space[4]+ ' | ' + space[5]+ ' | ' + space[6]+ ' | ' + space[7])
    print('   |   |   |   |   |   |')

#define a function for placing the letter in to the 6x7 spaces
def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

#define a function to decide who will be the first player randomly
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'player'
    else:
        return 'computer'

#define the playAgain mechanism whenever the player lose the game
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

#define the function for making the move of the letters
def makeMove(space, letter, move):
    if space[move]==' ':
        space[move] = letter
    elif space[move+7]==' ':
        space[move+7] = letter
    elif space[move+14] == ' ':
        space[move+14] = letter
    elif space[move+21]==' ':
        space[move+21] = letter
    elif space[move+28]==' ':
        space[move+28] = letter
    elif space[move+35]==' ':
        space[move+35] = letter

#define the function of checking whether one of the player wins
def isWinner(bo, le):
    for i in (1, 2, 3, 4, 8, 9, 10, 11, 15, 16, 17, 18, 22, 23, 24, 25, 29, 30, 31, 32,36,37,38,39):
        if (bo[i] == le and bo[i + 1] == le and bo[i + 2] == le and bo[i + 3] == le):
            return True  # Horizontal
    for i in list(range(1,22)):
        if (bo[i] == le and bo[i + 7] == le and bo[i + 14] == le and bo[i + 21] == le):
            return True  # Vertical
    for i in list(range(1,19)):
        if (bo[i] == le and bo[i + 8] == le and bo[i + 16] == le and bo[i + 24] == le):
            return True  # Diagonal
    for i in list(range(4, 22)):
        if (bo[i] == le and bo[i + 6] == le and bo[i + 12] == le and bo[i + 18] == le):
            return True  # Diagonal
    else:
        return False

#define the function of copying the space
def getspaceCopy(space):
    dupespace = []
    for i in space:
        dupespace.append(i)
    return dupespace

#define the function of checking whether the space is empty
def isSpaceFree(space, move):
    if space[move] == ' ' or space[move+7] == ' ' \
            or space[move + 14] == ' ' or space[move+21] == ' '\
            or space[move+28] == ' 'or space[move+35] == ' ':
        return True

#define the function of getting the next move of the player
def getPlayerMove(space):
    move = ' '
    while move not in '1 2 3 4 5 6 7'.split() or not isSpaceFree(space, int(move)):
        print('What is your next move? Please input (1-7)')
        move = input()
    return int(move)

#define the possible position for the next moving decision
def chooseRandomMoveFromList(space, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(space, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
    else:
            return None

#define the moving mechanism of the computer player
def getComputerMove(space, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
        computerLetter = 'O'
    for i in range(1, 8):
        copy = getspaceCopy(space)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    for i in range(1, 8):
        copy = getspaceCopy(space)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    move = chooseRandomMoveFromList(space, [1,2,3,4,5,6,7])
    if move != None:
        return move

#define the function of checking whether the spaces are all full
def isspaceFull(space):
    for i in range(1, 8):
        if isSpaceFree(space, i):
            return False
    return True

#design the welcome message
print('Welcome to Connect Four!')

#start the game with an empty space, then conbining all the functions defined about into an integrated playing mechanism
while True:
    thespace = [' '] * 43
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            drawspace(thespace)
            move = getPlayerMove(thespace)
            makeMove(thespace, playerLetter, move)
            if isWinner(thespace, playerLetter):
                drawspace(thespace)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isspaceFull(thespace):
                    drawspace(thespace)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(thespace, computerLetter)
            makeMove(thespace, computerLetter, move)
            if isWinner(thespace, computerLetter):
                drawspace(thespace)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isspaceFull(thespace):
                    drawspace(thespace)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    if not playAgain():
        break