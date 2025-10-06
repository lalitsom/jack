import random


def player1_strategy(current_hand, current_deck_length, memory):
    return False, memory
    
def player2_strategy(current_hand, current_deck_length, memory):
    if sum(current_hand) >= 13:
        return False, memory
    else:
        return True, memory





strategy_map = {
    "player_1": player1_strategy,
    "player_2": player2_strategy
}



    