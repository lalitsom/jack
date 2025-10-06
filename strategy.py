import random


def always_skip(current_hand, current_deck_length, memory, action="game_ongoing"):
    return False, memory

    
def player2_strategy(current_hand, current_deck_length, memory, action="game_ongoing"):
    if sum(current_hand) >= 16:
        return False, memory
    else:
        return True, memory



strategy_map = {
    # "player_1": memoize_current_hand,
    "player_1": always_skip,
    "player_2": player2_strategy
}



    