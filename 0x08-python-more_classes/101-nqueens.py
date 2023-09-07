#!/usr/bin/python3
'''
    The N queens puzzle
    refer to the flowchart file ()
'''
import sys


def init_board(n):
    '''
        Initialize an empty chessboard
        with n rows and n columns filled with spaces (' ')
    '''
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return board


def board_deepcopy(board):
    '''
        creates and return a deepcopy of the board
    '''
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board


def get_solution(board):
    '''
        retrieve the queens position
        on the board as list of lists
    '''
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 'Q':
                solution.append([r, c])
                break
    return solution


def xout(board, row, col):
    '''
        marks the spot where queens cannot be played
    '''

    '''retrieves all forward spots marked as X'''
    for c in range(col + 1, len(board)):
        board[row][c] = 'x'

    '''retrieves all backwards spots marked as X'''
    for c in range(col - 1, -1, -1):
        board[row][c] = 'x'

    '''retrieves all spots below marked as X'''
    for r in range(row + 1, len(board)):
        board[r][col] = 'x'

    '''retrieves all spots above marked as X'''
    for r in range(row - 1, -1, -1):
        board[r][col] = 'x'

    '''retrieves all diagonal spots down to right marked as X'''
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = 'x'
        c += 1

    '''retrieves all diagonal spots up to left marked as X'''
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1

    '''retrieves all diagonal spots up to right marked as X'''
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = 'x'
        c += 1

    '''retrieves all diagonal spots down to down marked as X'''
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = 'x'
        c -= 1


def recursive_solve(board, row, queens, solutions):
    '''
        Recursively solving the N queens
    '''
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == ' ':
            # Create a temporary copy of the board
            tmp_board = board_deepcopy(board)
            # Place a queen on the board
            tmp_board[row][c] = 'Q'
            # Mark spot where queens cannot be placed
            xout(tmp_board, row, c)
            # Recursively call the next row
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return solutions


if __name__ == '__main__':
    # Check the number of args
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    # Validate the args as (int(s))
    if sys.argv[1].isdigit() is False:
        print('N must be a number')
        sys.exit(1)

    # Check if N is < 4
    if int(sys.argv[1]) < 4:
        print('N must be at least 4')
        sys.exit(1)

    # initialize board
    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for solution in solutions:
        print(solution)
