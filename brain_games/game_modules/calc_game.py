from random import choice
from random import randint


OBJECTIVE = 'What is the result of the expression?'


def get_results():
    first_value = randint(1, 10)
    second_value = randint(1, 10)
    operator = choice(['-', '+', '/', '*', ])
    question = (f'{first_value} {operator} {second_value}')
    correct_answer = str(calc(first_value, second_value, operator))
    return question, correct_answer


def calc(first_value, second_value, operator):
    if operator == '-':
        result = (first_value - second_value)
    elif operator == '+':
        result = (first_value + second_value)
    elif operator == '/':
        result = int(first_value / second_value)
    elif operator == '*':
        result = int(first_value * second_value)
    return result
