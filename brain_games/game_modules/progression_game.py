from random import randint
from random import choice


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
    progression = []

    for index in range(start, stop, step):
        progression.append(index)
    return progression


def get_question_answer():
    progression = generate_progression()
    correct_answer = choice(progression)
    question = ' '.join([
        '..' if x == correct_answer else str(x) for x in progression
    ])
    return question, str(correct_answer)
