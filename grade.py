from ast import literal_eval
from file_path import CLUES_PATH
import json

if __name__ == '__main__':
    with open(CLUES_PATH) as fp:
        solution = literal_eval(json.load(fp))

    gt = dict()
    with open('input.txt') as fp:
        lines = [line.strip() for line in fp.readlines()]
        n = len(lines)
        for i in range(0, n, 3):
            clue = lines[i]
            answer = lines[i+2].lower()
            gt[clue] = answer

    score = 0
    for clue in solution:
        correct = gt[clue] in solution[clue]
        if correct:
            score += 1
            print(f"[O] {clue}")
        else:
            print(f"[X] {clue}: {solution[clue][:5]}")
    print(f'{score}/{len(gt)}')
