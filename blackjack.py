# trying reinforcement learning by simple blackjack game

import random
import strategy

global_memory = {}

def get_memory(player):
    global global_memory
    if player in global_memory:
        return global_memory[player]
    else:
        global_memory[player] = {"name": player}
        return global_memory[player]

def update_memory(player, new_memory):
    global global_memory
    global_memory[player] = new_memory

def new_shuffled_deck():
    deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4
    random.shuffle(deck)
    return deck

def busted(hand):
    return sum(hand)>21


def get_action(player, current_hand, current_deck_length, round):
    memory = get_memory(player)
    pick, new_memory = strategy.strategy_map[player](current_hand, current_deck_length, memory)
    update_memory(player, new_memory)
    return pick


def someone_won(player_hands, players):
    busted_count = 0
    for player in players:
        if (sum(player_hands[player]) == 21):
            return True
        if sum(player_hands[player])>21:
            busted_count +=1
    
    # all lost, only one winner remaining
    if busted_count == len(players)-1:
        return True
    return False



def run_game(card_deck, players, round):
    player_hands = {}
    
    for player in players:
        player_hands[player] = []
    
    # initial 2 card pop
    for player in players:
        for i in range(2):    
            player_hands[player].append(card_deck.pop())    
    
    while True:
        # print(player_hands)
        someone_picked = False
        for player in players:
            hand = player_hands[player]
            if busted(hand):
                continue
            
            is_picked = get_action(player, hand, len(card_deck), round)
            if is_picked:
                someone_picked = True
                hand.append(card_deck.pop())
                if someone_won(player_hands, players):
                    break
        
        if (not someone_picked) or someone_won(player_hands, players):
            break
        
    return player_hands


def run_rounds_set(rounds):
    players = ["player_1", "player_2"]
    
    winners = []
        
    for round in range(rounds):
        card_deck = new_shuffled_deck()
        results = run_game(card_deck, players, round)
        
        # print(results)
        
        winner = ""
        max_score = 0
        for player in players:
            hand_sum = sum(results[player]) 
            if (hand_sum > 21):
                continue
            if hand_sum > max_score:
                max_score = hand_sum
                winner = player
        
        for player in players:
            if winner == player:
                strategy.strategy_map[player](results[player], 0, get_memory(player), action="won")
            else:
                strategy.strategy_map[player](results[player], 0, get_memory(player), action="lost")
        
        winners.append(winner)


    print("----------------round set result----------------")    
    for player in players:
        print(player, winners.count(player)*100 / len(winners), "%")


def main():
    
    for i in range(10):
        run_rounds_set(10)
    
main()