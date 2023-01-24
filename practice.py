import random
secret_num = random.randrange(1,11)

is_game_over = False
attempts = 1

while is_game_over == False:
    
    print('Guess the number!')
    user_guess = int(input('Your Guess: '))

    if user_guess == secret_num:
        print('you got it!')
        print(f'your attempts : {attempts}')
        is_game_over = True

    if user_guess > secret_num:
        print('too much!')

    if user_guess < secret_num:
        print('too low!')

    attempts = attempts + 1