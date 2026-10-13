
from tictactoegame.tictactoe_game import TicTacToeGame
from tictactoegame.models.game_status import GameStatus

def main():

    print("\n ---- TIC TAC TOE GAME ---- \n")

    game = TicTacToeGame()
    game.initialize_game()

    status = game.start_game()

    print("\n ---- GAME OVER : ---- ", end="")

    match status:
        case GameStatus.WIN:
            print(f"{game.winner.player_name} WON GAME...")
        case GameStatus.DRAW:
            print(f"GAME DRAW...")
        case _:
            print(f"GAME ENDS...")

    


if __name__ == "__main__":
    main()