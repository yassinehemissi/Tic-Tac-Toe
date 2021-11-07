from random import randrange

WINNING_COMBINATIONS = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6]
]

class Board:
    def __init__(self):
        self.board = [i + 1 for i in range(9)]
        self.show_board()
        self.board = [" " for i in range(9)]
        self.winner = None 
    def choose_sign(self):
        print("Chooes Sign X/O:")
        self.sign = input()
        if self.sign != "X" and self.sign != "O":
            self.choose_sign()
        else: 
            self.coop_sign = "O" if self.sign == "X" else "X" 
    def show_board(self):
        for i in range(0,9,3):
            print(f"{self.board[i]}|{self.board[i + 1]}|{self.board[i + 2]}")
            if i < 6:
                print("-----")
    def pick(self):
        print("Choose your next position move:")
        pick_pos = int(input()) or 0 
        if pick_pos not in range(1,10):
            return self.pick()
        if self.board[pick_pos - 1] == "X" or self.board[pick_pos - 1] == "O":
            print("Position already Chosen!")
            self.pick()
        else:
            self.board[pick_pos - 1] = self.sign
            if self.check_for_win(self.sign):
                self.winner = self.sign
                return 
            self.random_pick()
    def random_pick(self):
        if self.board.count(" ") == 0:
            return
        pick_pos = randrange(0,9)
        if self.board[pick_pos] == "X" or self.board[pick_pos] == "O":
            return self.random_pick()
        else:
            self.board[pick_pos] = self.coop_sign
            if self.check_for_win(self.sign):
                self.winner = self.coop_sign
                return 
            self.show_board()

    def check_for_win(self, sign):
        for c in WINNING_COMBINATIONS:
            if self.board[c[0]] == sign and self.board[c[1]] == sign and self.board[c[2]] == sign:
                print(sign + " Wins!")
                return True
        return None 
    def play(self):
        while self.board.count(" ") != 0 and self.winner == None:
            state = self.pick()
        self.show_board()
        print("Game ended!")


def main():
    newBoard = Board()
    newBoard.choose_sign()
    newBoard.play()
    newBoard.show_board()

main()