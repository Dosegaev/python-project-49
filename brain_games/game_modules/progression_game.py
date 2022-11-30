from random import randint
from random import choice
from brain_games.games_logic import launch_the_script


OBJECTIVE = 'What number is missing in the progression?'
FIRST_NUMBER = 1
LAST_NUMBER = 100
STEP_START = 1
STEP_STOP = 21
LENGTH = 10


def generate_progression():
    start = randint(FIRST_NUMBER, LAST_NUMBER)
    step = randint(STEP_START, STEP_STOP)
    stop = start + (LENGTH * step)
    list = []

    for index in range(start, stop, step):
        list.append(index)
    return list


def get_results():
    list = generate_progression()
    correct_answer = choice(list)
    question = ' '.join([
        '..' if number == correct_answer else str(number) for number in list])
    return question, str(correct_answer)


def starting():
    launch_the_script(OBJECTIVE, get_results)
