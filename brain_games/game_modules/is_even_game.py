from random import randint


OBJECTIVE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_answer():
    random_number = randint(1, 100)
    question = random_number
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
