from random import randint
from brain_games.games_logic import launch_the_script


OBJECTIVE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_results():
    question = randint(1, 100)
    if calc(question) is False:
        correct_answer = "no"
    if calc(question) is True:
        correct_answer = "yes"
    return question, correct_answer


def calc(question):
    if question <= 1:
        return False
    if question == 2:
        return True
    if question % 2 == 0:
        return False
    for item in range(3, int(question / 2) + 1, 2):
        if question % item == 0:
            return False
    return True


def starting():
    launch_the_script(OBJECTIVE, get_results)
