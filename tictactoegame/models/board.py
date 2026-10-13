
from typing import List,Tuple, Optional

from .playing_piece import PlayingPiece

class Board:
    def __init__(self, size: int):
        self.size = size
        self.board: List[List[Optional[PlayingPiece]]] = [
            [None for _ in range(size)] for _ in range(size)
        ]

    def add_piece(self, row: int, col: int, playing_piece: PlayingPiece) -> bool:

        if not (0 <= row < self.size) or not( 0 <= col < self.size):
            return False

        if self.board[row][col] is not None:
            return False

        self.board[row][col] = playing_piece
        return True

    def get_free_cells(self) -> List[Tuple[int, int]]:

        free_cells: List[Tuple[int, int]] = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is None:
                    free_cells.append((i, j))

        return free_cells

    def print_board(self) -> None:

        print("-"*(self.size * 4+1))
        for i in range(self.size):
            row_str = "|"

            for j in range(self.size):
                piece = self.board[i][j]

                if piece is not None:
                    row_str += f" {piece.piece_type.name} "
                else:
                    row_str += f"   "

                row_str += "|"

            print(row_str)
            print("-"*(self.size * 4+1))
        print()

