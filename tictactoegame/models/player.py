from .playing_piece import PlayingPiece

class Player:
    def __init__(self, player_name: str, playing_piece: PlayingPiece):
        self.player_name = player_name
        self.playing_piece = playing_piece