from collections import deque
from typing import Deque, Optional

from tictactoegame.models import Player, Board, PieceType, PlayingPiece, PlayingPieceX, PlayingPieceO, GameStatus

class TicTacToeGame:
    def __init__(self):
        self.players: Deque[Player] = deque()
        self.game_board: Optional[Board] = None
        self.winner: Optional[Player] = None 

    def initialize_game(self) -> None:

        self.players = deque()

        player1 = Player("Venkat", PlayingPieceX())
        player2 = Player("Adithya", PlayingPieceO())

        self.players.extend([player1, player2])

        self.game_board = Board(size=3)

    def start_game(self) -> GameStatus:

        game_not_finished = True

        while game_not_finished:

            current_player = self.players.popleft()

            self.game_board.print_board()

            free_spaces = self.game_board.get_free_cells()
            if not free_spaces:
                return GameStatus.DRAW

            try:
                user_input = input(f"Player : {current_player.player_name} -- Please enter [row, column] : ")
                values = user_input.split(",")
                row = int(values[0].strip())
                column = int(values[1].strip())
            except (ValueError, IndexError):
                print("Invalid input Format! Please enter numeric coordinates separated by a comma (e.g., 0,1).")
                self.players.appendleft(current_player)
                continue

            valid_move = self.game_board.add_piece(row, column, current_player.playing_piece)
            if not valid_move:
                print(f"Incorrect Position chosen...")
                self.players.appendleft(current_player)
                continue

            self.players.append(current_player)

            is_winner = self.check_winner(row, column, current_player.playing_piece)

            if is_winner:
                self.game_board.print_board()
                self.winner = current_player
                return GameStatus.WIN

        return GameStatus.DRAW

    def check_winner(self, row: int, col: int, piece_type: PieceType) -> bool:

        row_match = True
        col_match = True
        diagonal_match = True
        anti_diagonal_match = True

        size = self.game_board.size
        grid = self.game_board.board

        for i in range(size):
            if grid[row][i] is None or grid[row][i] is not piece_type:
                row_match = False
                break

        for i in range(size):
            if grid[i][col] is None or grid[i][col] is not piece_type:
                col_match = False
                break

        for i in range(size):
            if grid[i][i] is None or grid[i][i] is not piece_type:
                diagonal_match = False
                break

        for i in range(size):
            j = size - i - 1
            if grid[j][j] is None or grid[j][j] is not piece_type:
                anti_diagonal_match = False
                break

        return row_match or col_match or diagonal_match or anti_diagonal_match
