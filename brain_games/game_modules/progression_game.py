from random import randint
from random import choice


OBJECTIVE = 'What number is missing in the progression?'
FIRST_NUMBER = 1
LAST_NUMBER = 1000
STEP_START = 1
STEP_STOP = 100
LENGTH = 10


def progression():
    start = randint(FIRST_NUMBER, LAST_NUMBER)
    step = randint(STEP_START, STEP_STOP)
    stop = start + (LENGTH * step)
    list = []

    for index in range(start, stop, step):
        list.append(index)
    return list


def calculations():
    question = progression()
    x_number = choice(question)
    correct_index = question.index(x_number)
    question[correct_index] = ".."
    correct_answer = str(x_number)
    return question, correct_answer
