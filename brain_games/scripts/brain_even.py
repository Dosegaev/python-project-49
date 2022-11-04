from random import randint
import prompt


OBJECTIVE = 'Answer "yes" if the number is even, otherwise answer "no".'
CYCLE = 3


def game_function():
    print("Welcome to the Brain Games!")
    global user_name
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print(OBJECTIVE)
    index = 0

    while index < CYCLE:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = input('Answer: ')

        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if correct_answer == user_answer:
            print('Correct!')
            index = index + 1
            if index == CYCLE:
                print(f'Congratulations, {user_name}!')
            continue
        else:
            print(f"Unfortunately, '{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
        break
        return


def main():
    game_function()


if __name__ == "__main__":
    main()
