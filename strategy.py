import random

global_memory = {}

def get_action(player, current_hand, current_deck_length):
    
    if (player == "player_1"):
        return player1_strategy(player, current_hand, current_deck_length)
    if (player == "player_2"):
        return player2_strategy(player, current_hand, current_deck_length)


def player1_strategy(player, current_hand, current_deck_length):
    return False
    
def player2_strategy(player, current_hand, current_deck_length):
    if sum(current_hand) >= 13:
        return False
    else:
        return True 
    
    
    
    # global global_memory
    # if player not in global_memory:
    #     global_memory[player] = []
    
    # global_memory[player].append(1)
    # return sum(global_memory[player]) > 10000
    


    