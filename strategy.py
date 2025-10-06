import random

def get_action(player, current_hand, current_deck_length):
    match player:
        case "dealer":
            return dealer_strategy(current_hand)
        case "player1":
            return player1_strategy(current_hand, current_deck_length)
        case _ : return (random.randint(0, 1))



def player1_strategy(current_hand, current_deck_length):
    return 0
    # return (random.randint(0, 0))

def dealer_strategy(current_hand):
    if sum(current_hand) >= 17:
        return 0
    else:
        return 1
    