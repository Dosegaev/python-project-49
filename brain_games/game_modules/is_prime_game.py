from random import randint


OBJECTIVE = 'Answer "yes" if given number is prime. Otherwise answer "no"..'


def calculations():
    question = randint(1, 100)
    prime_number = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    if question in prime_number:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
