import random

def monty_hall():
    winner = random.randint(0,2);
    first_choice = random.randint(0,2); 
    open_door = random.choice([0,1,2])


    #if Host opens winner
    if(open_door == winner):
        return 3

    #Host did not open winner
    if 2 not in (first_choice, open_door):
        final_choice = 2

    if 1 not in (first_choice, open_door):
        final_choice = 1

    if 0 not in (first_choice, open_door):
        final_choice = 0

    if (final_choice == winner):
        return 1; 
    return 0


def counter():
    num_games = 10000
    dead_ends = 0;
    wins = 0;
    for i in range (num_games):
        game = monty_hall()
        if(game == 3):
            dead_ends += 1
        elif(game == 1):
            wins += 1
    print("WINS:")
    print(wins/num_games)
    print("DEADS:")
    print(dead_ends/num_games)




counter()
