import random

def monty_hall():
    winner = random.randint(0,2);
    first_choice = random.randint(0,2); 
    if(first_choice == winner):
        if first_choice == 1:
                open_door = random.choice([0,2])
        elif first_choice == 2:
                open_door = random.choice([0,1])
        else:
            open_door = random.choice([1,2])
    else:
        if (first_choice + winner == 1):
            open_door = 2
        elif first_choice + winner == 2:
            open_door = 1;
        else:
            open_door = 0; 

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
    wins = 0;
    for i in range (num_games):
        wins += monty_hall();
    print(wins/num_games)




counter()
