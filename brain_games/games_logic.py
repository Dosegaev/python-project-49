import prompt


CYCLE = 3
GREETINGS = "Welcome to the Brain Games!"


def launch_the_game(objective: str, get_question_answer: callable):
    print(GREETINGS)
    user_name = (prompt.string("May I have your name? "))
    print(f"Hello, {user_name}!")
    print(objective)
    index = 0

    while index < CYCLE:
        question, correct_answer = get_question_answer()
        print(f'Question: {question}')
        user_answer = input('Answer:  ')
        if user_answer == correct_answer:
            print('Correct!')
            index = index + 1
            if index == CYCLE:
                print(f'Congratulations, {user_name}!')
        else:
            print(f"Unfortunately, '{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
