import fileinput
import pyglet


TILE_SIZE = 32
WIDTH = 2400
HEIGHT = 1300
MAX_HORIZONTAL_BOARDS = 12
MAX_BOARDS_ON_SCREEN = 72

NUMBER_LABELS = {}


class BingoBoard:
    def __init__(self, numbers):
        self.board = self.create_board(numbers)
        self.winner = False

    @staticmethod
    def create_board(numbers):
        # create coordinates matrix [(4, 0), (4, 1)...]
        coordinates_tuples = [(x, y) for y in reversed(range(5)) for x in range(5)]
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


class GameState:
    def __init__(self, game_data, draws):
        self.boards = self.load_boards(game_data)[:MAX_BOARDS_ON_SCREEN]
        self.draws = draws
        self.round = 0
        self.score = 0

    @staticmethod
    def load_boards(game_data):
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

    def play_game(self, dt):
        try:
            draw = self.draws[self.round]
        except IndexError:
            return
        for game_board in self.boards:
            if self.score:
                break
            game_board.play_round(draw)
            if game_board.eval_win():
                self.score = game_board.count_score(draw)
        if not self.score:
            self.round += 1

    def draw(self):
        round_text = "ROUND: " + str(self.round)
        round_label = get_label(
            round_text,
            2200,
            1260,
            anchor_x="right",
            color=(255, 255, 0, 255)
        )
        round_label.draw()

        score_text = "SCORE: " + str(self.score)
        score_label = get_label(
            score_text,
            2380,
            1260,
            anchor_x="right",
            color=(0, 255, 255, 255)
        )
        score_label.draw()

        offset_x = 0
        offset_y = 0
        counter = 0
        for board in self.boards:
            if counter == MAX_HORIZONTAL_BOARDS:
                counter = 0
                offset_y += 200
                offset_x = 0
            for field in board.board:
                if not field.hit:
                    flag = "G"
                    color = (0, 255, 0, 255)
                else:
                    flag = "R"
                    color = (255, 0, 0, 255)
                try:
                    label = NUMBER_LABELS.get(field).get(flag)
                except AttributeError:
                    label = None
                if not label:
                    label = get_label(
                        str(field.no),
                        field.x * TILE_SIZE + offset_x + 15,
                        field.y * TILE_SIZE + offset_y + 15,
                        anchor_x="center",
                        color=color
                    )
                    try:
                        NUMBER_LABELS[field][flag] = label
                    except KeyError:
                        NUMBER_LABELS[field] = {}
                        NUMBER_LABELS[field][flag] = label
                label.draw()
            offset_x += 200
            counter += 1


def get_label(text, x, y, anchor_x, color):
    label = pyglet.text.Label()
    label.text = text
    label.x = x
    label.y = y
    label.anchor_x = anchor_x
    label.font_size = 15
    label.color = color
    return label


window = pyglet.window.Window(width=WIDTH, height=HEIGHT)


@window.event
def on_draw():
    window.clear()
    title.draw()
    state.draw()


game_data = [line.strip().split() for line in fileinput.input()]
draws = game_data.pop(0)
draws = [int(d) for d in draws[0].split(",")]
state = GameState(game_data, draws)

title = get_label("SQUID BINGO!", x=10, y=1260, anchor_x="left", color=(255, 255, 255, 255))

pyglet.clock.schedule_interval(state.play_game, 1/6)
pyglet.app.run()
