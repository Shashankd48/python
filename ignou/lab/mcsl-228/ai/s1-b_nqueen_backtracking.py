# Write a Python Program to implement the Backtracking approach to solve N Queen’s problem

class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solutions = []

    def solve_nqueens(self):
        self.solve(0)
        return self.solutions

    def solve(self, col):
        if col == self.n:
            self.solutions.append(self.create_solution())
            return True

        res = False
        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                res = self.solve(col + 1) or res
                self.board[i][col] = 0  # backtrack

        return res

    def is_safe(self, row, col):
        # Check if there's a queen in the same row to the left
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, self.n), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def create_solution(self):
        solution = []
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    solution.append((i, j))
        return solution

    def draw_board(self, solution):
        for i in range(self.n):
            for j in range(self.n):
                if (i, j) in solution:
                    print(" Q ", end="")
                else:
                    print(" - ", end="")
            print()

def main():
    global n
    n = input("Enter N: ")
    n = int(n)
    n_queens = NQueens(n)
    solutions = n_queens.solve_nqueens()
    for idx, sol in enumerate(solutions, start=1):
        print(f"Solution {idx}:")
        n_queens.draw_board(sol)
        print()

if __name__ == "__main__":
    main()
