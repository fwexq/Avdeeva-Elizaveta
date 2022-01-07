class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

class Game:
    def rps_game_winner(self, players_choice: list):
        if len(players_choice) > 2:
            raise WrongNumberOfPlayersError

        if players_choice[0][1].lower() == 'p' and players_choice[1][1].lower() == 'a':
            raise NoSuchStrategyError

        if players_choice[0][1].lower() == 'r' and players_choice[1][1].lower() == 's':
            return 'player1 R'
        if players_choice[0][1].lower() == 's' and players_choice[1][1].lower() == 'r':
            return 'player2 R'

        if players_choice[0][1].lower() == 's' and players_choice[1][1].lower() == 'p':
            return 'player1 S'
        if players_choice[0][1].lower() == 'p' and players_choice[1][1].lower() == 's':
            return 'player2 S'

        if players_choice[0][1].lower() == 'r' and players_choice[1][1].lower() == 'p':
            return 'player2 P'
        if players_choice[0][1].lower() == 'p' and players_choice[1][1].lower() == 'r':
            return 'player1 P'

        if players_choice[0][1].lower() == 'r' and players_choice[1][1].lower() == 'r':
            return 'player1 R'
        if players_choice[0][1].lower() == 's' and players_choice[1][1].lower() == 's':
            return 'player1 S'
        if players_choice[0][1].lower() == 'p' and players_choice[1][1].lower() == 'p':
            return 'player1 P'


game = Game()
print(game.rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])) #=> WrongNumberOfPlayersError
print(game.rps_game_winner([['player1', 'P'], ['player2', 'A']])) #=> NoSuchStrategyError
print(game.rps_game_winner([['player1', 'P'], ['player2', 'S']]))  # => 'player2 S'
print(game.rps_game_winner([['player1', 'P'], ['player2', 'P']]))  # => 'player1 P'