from random import randint
from brain_games.games_logic import launch_the_script


OBJECTIVE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_results():
    random_number = randint(1, 100)
    question = random_number
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def starting():
    launch_the_script(OBJECTIVE, get_results)
