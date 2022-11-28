import prompt
from brain_games.game_modules import calc_game
from brain_games.game_modules import is_even_game
from brain_games.game_modules import gcd_game
from brain_games.game_modules import progression_game
from brain_games.game_modules import is_prime_game


CYCLE = 3
GREETINGS = "Welcome to the Brain Games!"


def launch_the_script(flag):
    if flag == 'calc':
        game = calc_game
    if flag == 'is_even':
        game = is_even_game
    if flag == 'gcd':
        game = gcd_game
    if flag == 'progression':
        game = progression_game
    if flag == 'is_prime':
        game = is_prime_game
    else:
        pass

    print(GREETINGS)
    user_name = (prompt.string("May I have your name? "))
    print(f"Hello, {user_name}!")
    print(game.OBJECTIVE)
    index = 0

    while index < CYCLE:
        question, correct_answer = game.get_results()
        print(f'Question: {question}')
        user_answer = input('Answer:  ')
        if user_answer == correct_answer:
            print('Correct!')
            index = index + 1
            if index == CYCLE:
                print(f'Congratulations, {user_name}!')
            continue
        else:
            print(f"Unfortunately, '{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
        break
        return
