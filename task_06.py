class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(array):
    if len(array) > 2:
        raise WrongNumberOfPlayersError

    elif array[0][1].lower() == 'p' and array[1][1].lower() == 'a':
        raise NoSuchStrategyError

    elif array[0][1].lower() == 'r' and array[1][1].lower() == 's':
        return 'player1 R'
    elif array[0][1].lower() == 's' and array[1][1].lower() == 'r':
        return 'player2 R'

    elif array[0][1].lower() == 's' and array[1][1].lower() == 'p':
        return 'player1 S'
    elif array[0][1].lower() == 'p' and array[1][1].lower() == 's':
        return 'player2 S'

    elif array[0][1].lower() == 'r' and array[1][1].lower() == 'p':
        return 'player2 P'
    elif array[0][1].lower() == 'p' and array[1][1].lower() == 'r':
        return 'player1 P'

    elif array[0][1].lower() == 'r' and array[1][1].lower() == 'r':
        return 'player1 R'
    elif array[0][1].lower() == 's' and array[1][1].lower() == 's':
        return 'player1 S'
    elif array[0][1].lower() == 'p' and array[1][1].lower() == 'p':
        return 'player1 P'


print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])) #=> WrongNumberOfPlayersError
print(rps_game_winner([['player1', 'P'], ['player2', 'A']])) #=> NoSuchStrategyError
print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))  # => 'player2 S'
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))  # => 'player1 P'