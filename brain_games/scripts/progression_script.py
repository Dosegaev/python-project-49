#!/usr/bin/env python


from brain_games.games_logic import launch_the_game
from brain_games.game_modules.progression_game import OBJECTIVE as objective
from brain_games.game_modules.progression_game import get_question_answer


def main():
    launch_the_game(objective, get_question_answer)


if __name__ == '__main__':
    main()
