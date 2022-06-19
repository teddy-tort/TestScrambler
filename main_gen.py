import os
from load_tex import load, p8


working_directory = "D:\\GitHub\\TestWriter\\tex_files"
tex_file_primer = "exam_prime.tex"


def make_tex_files(number_of_students: int):
    global working_directory, tex_file_primer
    key_filename = os.path.join(working_directory, "key.txt")
    with open(key_filename, 'w') as f:
        f.write('')
    for ii in range(number_of_students):
        questions, key = load(latex_file=os.path.join(working_directory, tex_file_primer))
        with open(key_filename, 'a') as f:
            f.write(key + '\n')


if __name__ == "__main__":
    make_tex_files(5)
