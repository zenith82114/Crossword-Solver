
# Crossword-Solver (extended with GPT)

This document only contains work done by me. Refer to `default_readme.md` (or `README.md` in the upstream repo) for more information.

## Automation and Grading

For convenience, a crossword puzzle is now read and parsed from a plain text, `input.txt`, rather than hard-coded as a Python dict in `schema.py`.

`input.txt` has three lines per clue, whose format is as follows:

```text
{clue} # first letter capitalized
{beginning_row_index} {beginning_column_index} {direction as [aAdD]} {answer_length}
{answer}
```

Here is an example output of `grade.py`:

```text
[O] __ of bad news
[O] Posture problem
[X] Loads: ['mounts', 'scores', 'masses', 'stacks', 'oceans']
[X] Laundry appliance: []
[O] Lectured
[O] One who weeps
[X] Grassy clump: ['wad']
[O] Pie chart portion
[X] "Scary Movie," e.g.: ['thrill', 'terror', 'horror', 'shiver', 'fright']
[X] Maryland's state bird: []
[X] Something worth saving: ['secret', 'morale', 'beauty', 'memory', 'trophy']
[O] "To __ is human"
6/12
```

## `words_gpt.py`

This code prepares `clues.json` by querying gpt-3.5-turbo for answers.

Two prompts are experimented:

```python
# v0
content = f"""
    A crossword clue says: {clue}.
    The answer must be {ans_length} letters long.
    Output ten most likely answers.
"""

# v1
content = f"""
    A crossword clue says: {clue}.
    The answer must be {ans_length} letters long.
    Output ten most likely answers.
    Do not output anything other than the answers.
    Make sure that the answers are of the same part-of-speech as the clue.
"""
```
