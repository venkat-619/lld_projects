from .piece_type import PieceType
from .playing_piece import PlayingPiece

class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)