from random import randint
import math


OBJECTIVE = 'Find the greatest common divisor of given numbers.'


def get_question_answer():
    first_value = randint(1, 100)
    second_value = randint(1, 100)
    question = (f'{first_value} {second_value}')
    correct_answer = str(math.gcd(first_value, second_value))
    return question, correct_answer
