import unittest
# We are designing a 2D game and we have a game map that we represent by an integer matrix. For now, each cell can be a wall (denoted by -1) or a blank space (0).

# board = [
#   [0,  0,  0,  0, -1],
#   [0,  0, -1,  0,  0],
#   [0, -1,  0, -1,  0],
#   [0,  0, -1,  0,  0],
#   [0,  0,  0,  0,  0],
#   [0,  0,  0,  0,  0],
#   [0,  0,  0,  0,  0],
# ]

# The player can move 1 space at a time up, down, left, or right. The player can't go through walls or land on a wall, or go through the edges of the board.

# Write a function that, given a board and a player starting position (represented as a row-column pair), returns all of the possible next positions for the player.

# Expected output (in any order):

# findLegalMoves(board, (3, 1)) =>
#   (3, 0), (4, 1)

# findLegalMoves(board, (5, 3)) =>
#   (5, 2), (5, 4), (4, 3), (6, 3)

# findLegalMoves(board, (6, 0)) =>
#   (5, 0), (6, 1)

# findLegalMoves(board, (6, 4)) =>
#   (5, 4), (6, 3)

# findLegalMoves(board, (0, 0)) =>
#   (0, 1), (1, 0)

# findLegalMoves(board, (2, 2)) =>
#   [empty]



board = [
  [0,  0,  0,  0, -1],
  [0,  0, -1,  0,  0],
  [0, -1,  0, -1,  0],
  [0,  0, -1,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
]

start1 = [3, 1]
start2 = [5, 3]
start3 = [6, 0]
start4 = [6, 4]
start5 = [0, 0]
start6 = [2, 2]

# row = first index
# col = second index

# -1 wall
# l or r or u or d


class Solution(object):
    def findLegalMoves(self, board, start):
        result = []
        row, column = start[0], start[1]
        try:
            left = board[row][column - 1]
            if (left != -1) and ((column - 1) != -1):
                result.append((row, column - 1))
        except:
            pass

        try:
            right = board[row][column + 1]
            if right != -1:
                result.append((row, column + 1))
        except:
            pass

        try:
            up = board[start[0] - 1][column]
            if (up != -1) and ((row - 1) != -1):
                result.append((row - 1, column))
        except:
            pass

        try:
            down = board[start[0] + 1][column]
            if down != -1:
                result.append((row + 1, column))
        except:
            pass

        return result

class Test(unittest.TestCase):
    def test_findLegalMoves_1(self):
        actual = Solution().findLegalMoves(board, start1)
        expected = [(3, 0), (4, 1)]

        self.assertEqual(actual, expected)

    def test_findLegalMoves_2(self):
        actual = Solution().findLegalMoves(board, start2)
        expected = [(5, 2), (5, 4), (4, 3), (6, 3)]

        self.assertEqual(actual, expected)

    def test_findLegalMoves_3(self):
        actual = Solution().findLegalMoves(board, start3)
        expected = [(6, 1), (5, 0)]

        self.assertEqual(actual, expected)

    def test_findLegalMoves_4(self):
        actual = Solution().findLegalMoves(board, start4)
        expected = [(6, 3), (5, 4)]

        self.assertEqual(actual, expected)

    def test_findLegalMoves_5(self):
        actual = Solution().findLegalMoves(board, start5)
        expected = [(0, 1), (1, 0)]

        self.assertEqual(actual, expected)

    def test_findLegalMoves_6(self):
        actual = Solution().findLegalMoves(board, start6)
        expected = []

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
