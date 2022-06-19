# TestScrambler
 Scrambles tests to help counteract cheating

# How to format the tex file
Do not use \vfill or \newpage between questions.

Make sure all questions are on no blank lines between lines of a given problem

Separate questions by at least one blank line

Wrap all questions and anything associated with them in \begin{minipage}[t]{\lw} ... \end{minipage}

# How to Use
Place tex file you wish to use as a primer into a known directory and name it "exam_prime.tex".

Open main_gen.py and replace the string working_directory with the path to "exam_prime.tex" and replace unique_exam_number with the number of unique exams you would like to have.

Run main_gen.py (double click file from file explorer, "python main_gen.py" in console, or use your favorite IDE).

# dependancies
numpy: https://numpy.org/doc/stable/

Built In:
random: https://docs.python.org/3/library/random.html
itertools: https://docs.python.org/3/library/itertools.html
os: https://docs.python.org/3/library/os.html
