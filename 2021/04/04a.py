import fileinput


class BingoBoard:
    def __init__(self, numbers):
        self.board = self.create_board(numbers)
        self.winner = False

    @staticmethod
    def create_board(numbers):
        # create coordinates matrix [(4, 0), (4, 1)...]
        coordinates_tuples = [(x, y) for x in reversed(range(5)) for y in range(5)]
        return [Field(*c, no) for c, no in zip(coordinates_tuples, numbers)]

    def eval_win(self):
        if self.winner:
            return  # don't evaluate once game is won
        # horizontal check
        for i in range(0, 20, 5):
            if len(list(filter(lambda x: x.hit, self.board[i:i+5]))) == 5:
                self.winner = True
                return True

        # vertical check
        # 0, 5, 10.. then 1, 6, 11..
        for i in range(5):
            counter = 0
            for j in range(i, 25, 5):
                if self.board[j].hit:
                    counter += 1
            if counter == 5:
                self.winner = True
                return True

    def count_score(self, draw):
        not_hit = list(filter(lambda x: not x.hit, self.board))
        not_hit = [x.no for x in not_hit]
        return sum(not_hit) * draw

    def play_round(self, draw):
        if self.winner:
            return
        for field in self.board:
            if field.no == draw:
                field.mark_hit()
                break


class Field:
    def __init__(self, x, y, no):
        self.x = x
        self.y = y
        self.no = no
        self.hit = False

    def __repr__(self):
        is_hit = "hit" if self.hit else "not hit"
        return f"({self.x}, {self.y}): {self.no} - {is_hit}"

    def mark_hit(self):
        self.hit = True


def load_boards():
    board = []
    boards = []
    for board_line in game_data:
        if board_line:
            for number in board_line:
                board.append(int(number))
        if len(board) == 25:
            boards.append(BingoBoard(board))
            board = []
    return boards


def play_game(draws, boards):
    for draw in draws:
        for game_board in boards:
            game_board.play_round(draw)
            if game_board.eval_win():
                result = game_board.count_score(draw)
                print("SCORE", result)
                return


if __name__ == "__main__":
    game_data = [line.strip().split() for line in fileinput.input()]
    draws = game_data.pop(0)
    draws = [int(d) for d in draws[0].split(",")]
    play_boards = load_boards()
    play_game(draws, play_boards)
