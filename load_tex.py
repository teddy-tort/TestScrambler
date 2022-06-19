import numpy as np

from random import random
from permutations import Generate


p8 = Generate(8)


class Question:
    def __init__(self, problem_statement: str, answers: list, q_pos: int, a_pos: list, length: int):
        if len(answers) != len(a_pos):
            raise ValueError("lengths of answers and a_pos lists should be equal")
        self.problem_statement = problem_statement
        self.answers = answers
        self.q_pos = q_pos
        self.a_pos = a_pos
        self.length = length    # number of lines in the question
        self.key = int(random() * np.math.factorial(len(answers)))
        self.a_pos = p8.scramble(self.key, self.a_pos)

    def get_a_pos(self) -> list:
        if isinstance(self.a_pos[0], list):
            list_to_return = []
            for ll in self.a_pos:
                list_to_return.extend(ll)
        else:
            list_to_return = self.a_pos
        return list_to_return


def open_tex(file):
    with open(file, 'r') as f:
        text = f.read()
    lines = text.split('\n')
    return lines


def get_questions(lines):
    questions = []
    q_on = False
    question = ''
    answers = []
    q_pos = 0
    a_pos = []
    start = False
    for ii, line in enumerate(lines):
        if "\\begin{enumerate}" in line:
            start = True
        elif "\\end{enumerate}" in line:
            start = False
        if start:
            if "\\item" in line:
                if not q_on:
                    q_pos = ii
                    question = line
                else:
                    a_pos.append(ii)
                    answers.append(line)
            if "\\begin{choices}" in line:
                q_on = True
                a_pos = []
                answers = []
            elif not line and q_on:
                q_on = False
                questions.append(Question(question, answers, q_pos, a_pos, ii - q_pos))
    return questions


def scramble_questions(questions: list) -> (list, int):
    q_key = p8.random()
    scrambled_questions = p8.scramble(q_key, questions)
    return scrambled_questions, q_key


def load(latex_file: str) -> (list, str):
    lines = open_tex(latex_file)
    question_list = get_questions(lines)
    a_keys = ''
    for q in question_list:
        a_keys += hex(q.key).lstrip('0')
    scrambled_q, q_key = scramble_questions(question_list)
    return scrambled_q, hex(q_key).lstrip('0') + a_keys


if __name__ == "__main__":
    file = "tex_files\\exam_prime.tex"
    questions, _ = load(file)
    print(len(questions))
    for ii, q in enumerate(questions):
        print(f"{q.q_pos}: {q.problem_statement}")
    print(questions[0].length)
    print(questions[1].length)
