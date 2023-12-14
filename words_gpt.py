from file_path import CLUES_PATH
import json
from openai import OpenAI
from schema import make_crossword_grid

if __name__ == '__main__':
    grid = make_crossword_grid()

    client = OpenAI()

    solution = {}

    print('Sending requests...')
    for clue, clue_dict in grid.items():
        print(f'\tGuessing: {clue}')
        clue_length = clue_dict['length']

        # v0
        # content = f"""
        #     A crossword clue says: {clue}.
        #     The answer must be {clue_length} letters long.
        #     Output ten most likely answers.
        # """

        # v1
        content = f"""
            A crossword clue says: {clue}.
            The answer must be {clue_length} letters long.
            Output ten most likely answers.
            Do not output anything other than the answers.
            Make sure that the answers are of the same part-of-speech as the clue.
        """

        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{ 'role':'user', 'content':content }],
            max_tokens=50
        )
        output = response.choices[0].message.content
        guesses = [s.lower() for s in output.split() if s.isalpha() and len(s) == clue_length]
        solution[clue] = list(set(guesses))

    print('Storing solution...')
    with open(CLUES_PATH, 'w') as fp:
        json.dump(str(solution), fp)
