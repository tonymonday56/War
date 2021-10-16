import random
from datetime import datetime

deck = []
player1_hand = []
player2_hand = []
score_player1 = 0
score_player2 = 0
round = 1
today = datetime.now()
todaystr = datetime.isoformat(today)
f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\war.dat", "a")
f.write("Begin New Game")
f.write("\n")
f.write(todaystr)
# f.write("  ")
# f.write(todaystime)
f.write("\n")
f.write("***********************************************")
f.write("\n")
f.close()
def play():
    player1_hand_used = []
    player2_hand_used = []
    global player1_hand
    global player2_hand
    global score_player1
    global score_player2
    global round
    
    for i in player1_hand:
        print("Round: ",round)
        player1_card = player1_hand.pop()
        print("player1_card: ",player1_card)
        player2_card = player2_hand.pop()
        print("player2_card: ", player2_card)
        
        if player1_card > player2_card:
            print("Player1 wins Battle!")
            f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\war.dat", "a")
            f.write("Round: ")
            f.write(str(round))
            f.write("\n")
            f.write("Player1 Card: ")
            f.write(player1_card)
            f.write("\n")
            f.write("Player2 Card: ")
            f.write(player2_card)
            f.write("\n")
            f.write("Player1 wins Battle!")
            f.write("\n")
            f.close()
            player1_hand_used.append(player1_card)
            player1_hand_used.append(player2_card)
        elif player2_card > player1_card:
            f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\war.dat", "a")
            f.write("Round: ")
            f.write(str(round))
            f.write("\n")
            f.write("Player1 Card: ")
            f.write(player1_card)
            f.write("\n")
            f.write("Player2 Card: ")
            f.write(player2_card)
            f.write("\n")
            f.write("Player2 wins Battle!")
            f.write("\n")
            f.close()
            print("Player2 wins Battle!")
            player2_hand_used.append(player1_card)
            player2_hand_used.append(player2_card)
    print("player1_hand_used: ", player1_hand_used)
    print("player2_hand_used: ", player2_hand_used)
    if len(player1_hand_used) == 0:
        print("Player2 Wins Game!")
        f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\war.dat", "a")
        f.write("Player2 Wins Game!")
        f.write("\n")
        f.write("----------------------------------------------")
        f.write("\n")
        f.close
        f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\warplayer2wins.dat", "r")
        player2wins = f.readline()
        f.close()
        player2winsnow = int(player2wins) + 1
        f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\warplayer2wins.dat", "w")
        f.write(str(player2winsnow))
        f.close()
    elif len(player2_hand) == 0:
        print("Player1 Wins Game!")
        f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\war.dat", "a")
        f.write("Player1 Wins Game!")
        f.write("\n")
        f.write("----------------------------------------------")
        f.write("\n")
        f.close
        f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\warplayer1wins.dat", "r")
        player1wins = f.readline()
        f.close()
        player1winsnow = int(player1wins) + 1
        f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\warplayer1wins.dat", "w")
        f.write(str(player1winsnow))
        f.close()
    else:
        player1_hand = player1_hand_used
        player2_hand = player2_hand_used
        round = round + 1
        play()


    


def create_deck():
    global player1_hand
    global player2_hand
    global deck
    cards = ["13", "12", "11", "10", "09", "08", "07", "06", "05", "04", "03", "02", "01"]
    suits = ["Clubs", "Spades", "Hearts", "Diamonds"]

    for suit in suits:
        for card in cards:
            deck.append(card + suit)
    print("count: ", len(deck))
    
 #   deal(deck)
    random.shuffle(deck)
    print("aftershuffle: ",deck)

    print("shuffled_deck: ",deck)
    print("Type: ", type(deck))
    for i in deck:
        if deck.index(i) % 2 == 0:
            player1_hand.append(i)
        elif deck.index(i) % 2 != 0:
            player2_hand.append(i)
    print("player1_hand: ", player1_hand)
    print("player2_hand: ", player2_hand)

    play()
create_deck()

# def deal(deck):
#     shuffled_deck = random.shuffle(deck)
#     player1_hand = []
#     player2_hand = []

