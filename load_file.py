class Question:
    def __init__(self, problem_statement: str, answers: list):
        self.problem_statement = problem_statement
        self.answers = answers


def open_tex(file):
    with open(file, 'r') as f:
        text = f.read()
    lines = text.split('\n')
    return lines


def get_questions(lines):
    questions = [None]
    q_on = False
    question = ''
    answers = []
    for line in lines:
        if "\\item" in line:
            if not q_on:
                question = line
            else:
                answers.append(line)
        if "\\begin{choices}" in line:
            q_on = True
        elif "\\end{choices}" in line:
            q_on = False
            questions.append(Question(question, answers))
    return questions


def load(file):
    lines = open_tex(file)
    question_list = get_questions(lines)
    return question_list


if __name__ == "__main__":
    file = "Exam 2 A.tex"
    lines = open_tex(file)
    q = get_questions(lines)
    print(q[6].problem_statement)
