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


class Primer:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            text = f.read()
        self.lines = text.split('\n')
        self.q_start_ind = self.lines.index("\\begin{enumerate}") + 1
        self.q_end_ind = self.lines.index("\\end{enumerate}")
        self.header = self.lines[0:self.q_start_ind]
        self.header.extend(['', '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', ''])
        self.footer = ['', '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', '']
        self.footer.extend(self.lines[self.q_end_ind:])

        self.q_num = self.find_number_of_questions()

    def find_number_of_questions(self) -> int:
        q_lines = self.lines[self.q_start_ind:self.q_end_ind]
        q_num = 0
        on_q = False
        for line in q_lines:
            if not on_q and "\\item" in line:
                on_q = True
                q_num += 1
            if on_q and line == "":
                on_q = False
        return q_num

    def gen_questions(self) -> list:
        questions = [None] * self.q_num
        on_q = False
        answers = []
        a_pos = []
        q_num = 0
        for ii, line in enumerate(self.lines[self.q_start_ind:self.q_end_ind]):
            if "\\item" in line:
                if on_q:
                    a_pos.append(ii + self.q_start_ind)
                    answers.append(line)
                else:
                    q_pos = ii + self.q_start_ind
                    question = line
            if "\\begin{choices}" in line:
                on_q = True
                a_pos = []
                answers = []
            elif not line and on_q:
                on_q = False
                questions[q_num] = Question(question, answers, q_pos, a_pos, ii + self.q_start_ind - q_pos)
                q_num += 1
        return questions

    def scramble(self, questions: list) -> (list, int):
        q_key = p8.random()
        scrambled_questions = p8.scramble(q_key, questions)
        return scrambled_questions, q_key


if __name__ == "__main__":
    file = "tex_files\\exam_prime.tex"
    prime = Primer(file)
    print(prime.gen_questions()[-1].problem_statement)
