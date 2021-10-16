CREATE TABLE war_wins (
player1_wins_total number not null,
player2_wins_total number not null);
CREATE TABLE war_hands (
Event_date  TEXT NOT NULL,
Event_time  TEXT NOT NULL,
RoundOfPlay  NUMBER NOT NULL,
Player1_card  TEXT NOT NULL,
Round_winner TEXT NOT NULL,
War_hands_idx  INTEGER  PRIMARY KEY ON CONFLICT ABORT AUTOINCREMENT
);