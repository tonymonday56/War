CREATE TABLE war_wins (
player1_wins_total number not null,
player2_wins_total number not null);


CREATE TABLE war_hands (
game_number INTEGER NOT NULL,
current_time  TEXT NOT NULL,
current_round  INTEGER NOT NULL,
current_hand INTEGER NOT NULL,
player1_card  TEXT NOT NULL,
player2_card TEXT NOT NULL,
round_winner TEXT NOT NULL,
war_hands_idx  INTEGER  PRIMARY KEY ON CONFLICT ABORT AUTOINCREMENT
);

CREATE TABLE game_win_data (
    game_number NUMBER NOT NULL,
    current_time TEXT NOT NULL,
    game_winner TEXT NOT NULL,
    number_of_hands NUMBER NOT NULL,
    game_win_idx INTEGER PRIMARY KEY ON CONFLICT ABORT AUTOINCREMENT
);