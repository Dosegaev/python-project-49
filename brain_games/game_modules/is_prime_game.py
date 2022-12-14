from random import randint


OBJECTIVE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_answer():
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
