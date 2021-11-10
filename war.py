import random
import time
import sqlite3
from sqlite3 import Error


deck = []
player1_hand = []
player2_hand = []
score_player1 = 0
score_player2 = 0
current_round = 1
t = time.asctime()
current_time = time.strftime(t)
games_played = 0
current_hand = 1
game_number = 1
game_winner = ""
round_winner = ""
number_of_hands = 1

#f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\war.dat", "a")
f = open("C:\\Users\\tony_\\War\\war.dat", "a")

f.write("Begin New Game")
f.write("\n")
f.write(current_time)
f.write("\n")
f.write("***********************************************")
f.write("\n")
f.close()

def insertVariableIntoWarHandsTable(game_number, current_time, current_round, current_hand, player1_card, player2_card, round_winner):
    """ insertVariableIntoWarHandsTable() - Used to insert hand data into sqlite table war_hands.  
        database - ("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\war.sqlite")
    """
    try:
       #sqliteConnection = sqlite3.connect("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\war.sqlite")
        
        sqliteConnection = sqlite3.connect("C:\\Users\\tony_\\War\\war.sqlite")
      
        cursor = sqliteConnection.cursor()
        print("Successfully connected to SQLite database [War] for war hand data insertion...")

        
        sqlite_insert_with_param_hands = """INSERT INTO war_hands
                          (game_number, current_time, current_round, current_hand, player1_card, player2_card, round_winner) 
                          VALUES (?, ?, ?, ?, ?, ?, ?);"""

        data_tuple_hands = (game_number, current_time, current_round, current_hand, player1_card, player2_card, round_winner)
        cursor.execute(sqlite_insert_with_param_hands, data_tuple_hands)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SQLite database [War] table=war_hands...")

        cursor.close()

    except sqlite3.Error as error:
        print("Failure to insert war hand variable into SQLite database [War] table=war_hands...", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection to insert War Hand data SQLite database [War] is closed...")


def insertVariableIntoGameWinDataTable(games_total, current_time, game_winner, number_of_hands):
    """ insertVariableIntoGameWinDataTable() - Used to game ending data into sqlite table war_hand.  
        database - ("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\war.sqlite")
    """            

    try:
       #sqliteConnection = sqlite3.connect("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\war.sqlite")
        
        sqliteConnection = sqlite3.connect("C:\\Users\\tony_\\War\\war.sqlite")
      
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite database [War]")

        #global number_of_hands
        sqlite_insert_with_param_game = """INSERT INTO game_win_data
                          (game_number, current_time, game_winner, number_of_hands) 
                          VALUES (?, ?, ?, ?);"""
        
        data_tuple_game_data = (game_number, current_time,  game_winner, number_of_hands)
        cursor.execute(sqlite_insert_with_param_game, data_tuple_game_data)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SQLite database [War] table=game_win_data...")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into SQLite database [War] table=game_win_data", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection to SQLite database [War] table=game_win_data is closed")


def play():
    player1_hand_used = []
    player2_hand_used = []
    global player1_hand
    global player2_hand
    global score_player1
    global score_player2
    global current_round
    global current_time
    global current_hand
    global game_number
    global round_winner
    global game_winner
    global number_of_hands
    
 #   conn = sqlite3.connect("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\war.sqlite")
 #   print("Opened database successfully...")
    
    for i in player1_hand:
        if player1_hand != [] and player2_hand != []:
            print("Game: ", game_number)
            print("Round: ",current_round)
            print("Hand: ", current_hand)
            player1_card = player1_hand.pop()
            print("player1_card: ",player1_card)
            player2_card = player2_hand.pop()
            print("player2_card: ", player2_card)
        else:
            break
            
        if player1_card > player2_card:
            print("Player1 wins Hand!")
            #f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\war.dat", "a")
            f = open("C:\\Users\\tony_\\War\\war.dat", "a")
            f.write("Round: ")
            f.write(str(current_round))
            f.write("\n")
            f.write("Hand: ")
            f.write(str(current_hand))
            f.write("\n")
            f.write("Player1 Card: ")
            f.write(player1_card)
            f.write("\n")
            f.write("Player2 Card: ")
            f.write(player2_card)
            f.write("\n")
            f.write("Player1 wins hand!")
            f.write("\n")
            f.close()
            print("Player1 wins hand!")
            round_winner = "Player 1"
            insertVariableIntoWarHandsTable(game_number, current_time, current_round, current_hand, player1_card, player2_card, round_winner)
            player1_hand_used.append(player1_card)
            player1_hand_used.append(player2_card)
            current_hand = current_hand + 1
            number_of_hands = number_of_hands + 1
                        
        elif player2_card > player1_card:
            #f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\war.dat", "a")
            f = open("C:\\Users\\tony_\\War\\war.dat", "a")
            f.write("Game Number: ")
            f.write(str(game_number))
            f.write("Round: ")
            f.write(str(current_round))
            f.write("\n")
            f.write("Hand: ")
            f.write(str(current_hand))
            f.write("\n")
            f.write("Player1 Card: ")
            f.write(player1_card)
            f.write("\n")
            f.write("Player2 Card: ")
            f.write(player2_card)
            f.write("\n")
            f.write("Player2 wins hand!")
            f.write("\n")
            f.close()
            print("Player2 wins hand!")
            round_winner = "Player 2"
            current_hand = current_hand + 1
   
            number_of_hands = number_of_hands + 1
            insertVariableIntoWarHandsTable(game_number, current_time, current_round, current_hand, player1_card, player2_card, round_winner)

            player2_hand_used.append(player1_card)
            player2_hand_used.append(player2_card)
            
    print("player1_hand_used: ", player1_hand_used)
    print("player2_hand_used: ", player2_hand_used)
    if len(player1_hand_used) == 0 and len(player1_hand) == 0:
        print("Player2 Wins Game!")
        #f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\war.dat", "a")
        f = open("C:\\Users\\tony_\\War\\war.dat", "a")
        f.write("Player2 Wins Game!")
        f.write("\n")
        f.write("----------------------------------------------")
        f.write("\n")
        f.close
        #f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\warplayer2wins.dat", "r")
        f = open("C:\\Users\\tony_\\War\\warplayer2wins.dat", "r")

        player2wins = f.readline()
        f.close()
        player2winsnow = int(player2wins) + 1
        #f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\warplayer2wins.dat", "w")
        f = open("C:\\Users\\tony_\\War\\warplayer2wins.dat", "w")

        f.write(str(player2winsnow))
        f.close()
        
        f = open("C:\\Users\\tony_\\War\\war_games_total.dat", "r")
        games_total = f.readline() 
        f.close()
        games_total = int(games_total) + 1
        f = open("C:\\Users\\tony_\\War\\war_games_total.dat", "w")
        f.write(str(games_total))
        f.close()
        #number_of_hands = number_of_hands + 0
        game_winner = "Player 2"
        insertVariableIntoGameWinDataTable(games_total, current_time, game_winner, number_of_hands)
    elif len(player2_hand_used) == 0 and len(player2_hand) == 0:

        print("Player1 Wins Game!")
        #f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\war.dat", "a")
        f = open("C:\\Users\\tony_\\War\\war.dat", "a")
        f.write("Player1 Wins Game!")
        f.write("\n")
        f.write("----------------------------------------------")
        f.write("\n")
        f.close
        
        #f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\warplayer1wins.dat", "r")
        f = open("C:\\Users\\tony_\\War\\warplayer1wins.dat", "r")
        player1wins = f.readline()
        f.close()
        player1winsnow = int(player1wins) + 1

        #f = open("C:\\Users\\tony_\\Google Drive\\Dev\\Programming\\Python\\Projects\\War\\warplayer1wins.dat", "w")
        f = open("C:\\Users\\tony_\\War\\warplayer1wins.dat", "w")
        f.write(str(player1winsnow))
        f.close()
        f = open("C:\\Users\\tony_\\war\\war_games_total.dat", "r")
        games_total = f.readline() 
        f.close()
        games_total = int(games_total) + 1
        f = open("C:\\Users\\tony_\\war\\war_games_total.dat", "w")
        f.write(str(games_total))
        f.close()
        game_winner = "Player 1"
        #number_of_hands = number_of_hands + 0
        insertVariableIntoGameWinsTable(games_total, current_time, game_winner, number_of_hands)
    else:
        player1_hand = player1_hand_used
        player2_hand = player2_hand_used 
        current_round = current_round + 1
        current_hand = 1
        play()
        

def create_deck():
    global player1_hand
    global player2_hand
    global deck
    global current_round
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

