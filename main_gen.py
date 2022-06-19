import os
from load_tex import Primer
import pylatex


working_directory = "D:\\GitHub\\TestWriter\\tex_files"
tex_file_primer = "exam_prime.tex"


def write_tex_file(filename: str, lines: list):
    if filename[-4:] != ".tex":
        filename = filename.split('.')[0] + ".tex"
    with open(os.path.join(working_directory, filename), 'w') as f:
        for line in lines:
            f.write(f"{line}\n")


def make_tex_files(number_of_students: int):
    global working_directory, tex_file_primer

    # create file to store key for rearranging
    key_filename = os.path.join(working_directory, "key.txt")
    with open(key_filename, 'w') as f:
        f.write('')

    # create object instance for exam_prime.tex
    primer = Primer(os.path.join(working_directory, tex_file_primer))

    # create a tex file for the number of students in the class (primer counts as 1)
    for ii in range(number_of_students-1):
        filename_to_write = f"exam_ver{ii+2:03}"
        lines_to_write = primer.header

        # generate a unique set of answer arrangments for the questions
        questions = primer.gen_questions()

        # generate key for rearranging answers
        a_keys = ''
        for q in questions:
            a_keys += hex(q.key).lstrip('0')

        # rearrange test questions
        questions_s, q_key = primer.scramble(questions)

        # if the number of questions is less than 8, then they won't be chunked: this chunks them
        if not isinstance(questions_s[0], list):
            for jj, q in enumerate(questions_s):
                questions_s[ii] = [q]

        # iterate over the questions in chunks
        for chunk in questions_s:
            for q in chunk:
                # grab lines related to the question
                question_to_write = primer.lines[q.q_pos-2:(q.q_pos+q.length)]

                start_answers = False  # allows the code to skip the /item that is the problem statement

                a_ind = 0  # index for answer number

                # iterate over the lines of the question to write to rearrange the questions
                for jj, ll in enumerate(question_to_write):
                    if "\\item" in ll and not start_answers:
                        # this skips the problem statement
                        start_answers = True
                    elif "\\item" in ll:
                        # replace answer with another based on the arrangement
                        question_to_write[jj] = primer.lines[q.a_pos[a_ind]]
                        a_ind += 1
                lines_to_write.extend(question_to_write)
                lines_to_write.append('')
        lines_to_write.extend(primer.footer)

        # write key file for unscrambling
        key = f"{hex(q_key).lstrip('0')}{a_keys}"
        with open(key_filename, 'a') as f:
            f.write(key + '\n')

        # create tex file
        write_tex_file(filename_to_write, lines_to_write)


if __name__ == "__main__":
    import time
    start = time.time()
    make_tex_files(300)
    print(time.time()-start)
