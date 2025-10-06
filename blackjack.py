# trying reinforcement learning by simple blackjack game

import random
import strategy


def new_shuffled_deck():
    deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4
    random.shuffle(deck)
    return deck

def busted(hand):
    return sum(hand)>=21


def someone_won(player_hands, players):
    busted_count = 0
    for player in players:
        if busted(player_hands[player]):
            busted_count +=1
    
    if busted_count == len(players)-1:
        return True
    return False



def run_game(card_deck, players, rounds):
    player_hands = {}
    
    for player in players:
        player_hands[player] = []
    
    # initial 2 card pop
    for player in players:
        for i in range(2):    
            player_hands[player].append(card_deck.pop())    
    
    while True:
        someone_picked = False
        for player in players:
            hand = player_hands[player]
            if busted(hand):
                continue
            
            is_picked = strategy.get_action(player, hand, len(card_deck))
            if is_picked:
                someone_picked = True
                hand.append(card_deck.pop())
                if someone_won(player_hands, players):
                    break
        
        if (not someone_picked) or someone_won(player_hands, players):
            break
        
    return player_hands


def main():
    
    rounds = 1000
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
        winners.append(winner)
    
    # print(winners)
    
    for player in players:
        print(player, winners.count(player)*100 / len(winners), "%")
    
    
    if winners.count(""):
        print("empty", winners.count(""), len(winners), "%")
main()