import random
import csv
import tkinter as tk
from quiz import TrueFalseQuestions
import sys

# Global values
rand_generated_numbers = []
sub_root = tk.Tk()
sub_root.withdraw()
position = 0

def array_with_points():
    # Initialize the two-dimensional array with 240 rows and 6 columns
    global vargu_ID
    vargu_ID = []

    with open('./src/Data_dump.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                vargu_ID.append(row)
        for row in vargu_ID:
            row.append(1)

array_with_points()


def generate_random(number):
    global total
    global position
    randNumber = 0
    total = 0
    if (number == -1):
        position -= 1
        rand = rand_generated_numbers[position]
        return rand
    else:
        # Generate a random number
        for row in vargu_ID:
            total += int(row[7])
        upto = 0
        num = random.uniform(0, total)
        for row in vargu_ID:
            if upto + row[7] >= num:
                randNumber = row[0]
                break
            upto += row[7]
        rand = int(randNumber) - 362
        if (rand not in rand_generated_numbers):
            position = len(rand_generated_numbers) - 1
            rand_generated_numbers.append(rand)
            position += 1
        return rand


def get_question(flag):
    # Get a random number
    global rand, question, option_a, option_b, option_c, option_d, answerColumn
    rand = generate_random(flag)

    # Get all the questions and options from the database
    question = str(vargu_ID[rand][1])

    option_a = str(vargu_ID[rand][2])

    option_b = str(vargu_ID[rand][3])

    option_c = str(vargu_ID[rand][4])

    option_d = str(vargu_ID[rand][5])

    answerColumn = str(vargu_ID[rand][6])


def previous_question(result_label):
    def on_click():
        get_question(-1)
        question_label.config(text=question)
        option_a_button.config(
            text=option_a, command=check_answer(option_a, result_label))
        option_b_button.config(
            text=option_b, command=check_answer(option_b, result_label))
        option_c_button.config(
            text=option_c, command=check_answer(option_c, result_label))
        option_d_button.config(
            text=option_d, command=check_answer(option_d, result_label))
        result_label.config(text="")
    return on_click


def next_question(result_label):
    def on_click():
        get_question(0)
        question_label.config(text=question)
        option_a_button.config(
            text=option_a, command=check_answer(option_a, result_label))
        option_b_button.config(
            text=option_b, command=check_answer(option_b, result_label))
        option_c_button.config(
            text=option_c, command=check_answer(option_c, result_label))
        option_d_button.config(
            text=option_d, command=check_answer(option_d, result_label))
        result_label.config(text="")
    return on_click


def next_question_right(result_label):
    get_question(0)
    question_label.config(text=question)
    option_a_button.config(
        text=option_a, command=check_answer(option_a, result_label))
    option_b_button.config(
        text=option_b, command=check_answer(option_b, result_label))
    option_c_button.config(
        text=option_c, command=check_answer(option_c, result_label))
    option_d_button.config(
        text=option_d, command=check_answer(option_d, result_label))
    result_label.config(text="")


def previous_question_left(result_label):
    get_question(-1)
    question_label.config(text=question)
    option_a_button.config(
        text=option_a, command=check_answer(option_a, result_label))
    option_b_button.config(
        text=option_b, command=check_answer(option_b, result_label))
    option_c_button.config(
        text=option_c, command=check_answer(option_c, result_label))
    option_d_button.config(
        text=option_d, command=check_answer(option_d, result_label))
    result_label.config(text="")


def check_answer(option, result_label):
    def on_click():
        if str(option).lower().replace(".,", "").strip() == str(answerColumn).lower().replace(".,", "").strip():
            result_label.config(text="Correct!", fg="green")
            if (vargu_ID[rand][1] > 0.1):
                vargu_ID[rand][1] -= 0.1
        else:
            result_label.config(text="Incorrect!", fg="red")
            if (vargu_ID[rand][1] < 1):
                vargu_ID[rand][1] += 0.1
    return on_click


def options_questions(root, sub_root):
    def on_click():
        global question_label, option_a_button, option_b_button, option_c_button, option_d_button, result_label

        root.withdraw()

        sub_root.title("Questions with options")
        sub_root.geometry("900x300")
        sub_root.deiconify()
        sub_root.protocol("WM_DELETE_WINDOW", on_closing())
        sub_root.bind("<Key>", handle_key)
        sub_root.overrideredirect(True)

        # get the screen width and height
        screen_width = sub_root.winfo_screenwidth()
        screen_height = sub_root.winfo_screenheight()

        # calculate the x and y coordinates for the window to be centered
        x = int((screen_width / 2) - (900 / 2))
        y = int((screen_height / 2) - (280 / 2) - 20)

        # set the position of the window to the center of the screen
        sub_root.geometry("+{}+{}".format(x, y))

        get_question(0)

        back_button = tk.Button(sub_root, text="Back",
                                width=10, command=back_fun(root, sub_root))
        back_button.pack(side=tk.LEFT, anchor=tk.NW, padx=15, pady=15)

        question_frame = tk.Frame(sub_root, width=700, height=70)
        question_frame.pack_propagate(False)
        question_frame.pack(padx=5, pady=15)

        question_label = tk.Label(question_frame, text=question, font=(
            "TkDefaultFont", 16), wraplength=700)
        question_label.pack(anchor="w")

        answer_frame = tk.Frame(sub_root, width=700, height=70)
        answer_frame.pack_propagate(False)
        answer_frame.pack(pady=5)

        result_label = tk.Label(sub_root, text="", font=("TkDefaultFont", 14))

        previous_button = tk.Button(
            sub_root, text="Previous", width=10, command=previous_question(result_label))
        previous_button.pack(side=tk.LEFT, anchor=tk.SW, padx=10, pady=15)

        next_button = tk.Button(
            sub_root, text="Next", width=10, command=next_question(result_label))
        next_button.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=15)

        result_label.pack()

        option_a_button = tk.Button(answer_frame, text=option_a,
                                    wraplength=300, command=check_answer(option_a, result_label))
        option_a_button.grid(row=0, column=1, padx=10, pady=10)

        option_b_button = tk.Button(answer_frame, text=option_b,
                                    wraplength=300, command=check_answer(option_b, result_label))
        option_b_button.grid(row=0, column=2, padx=10, pady=10)

        option_c_button = tk.Button(answer_frame, text=option_c,
                                    wraplength=300, command=check_answer(option_c, result_label))
        option_c_button.grid(row=1, column=1, padx=10, pady=10)

        option_d_button = tk.Button(answer_frame, text=option_d,
                                    wraplength=300, command=check_answer(option_d, result_label))
        option_d_button.grid(row=1, column=2, padx=10, pady=10)

    return on_click


def handle_key(event):
    if event.keysym == "Right":
        next_question_right(result_label)
    elif event.keysym == "Left":
        previous_question_left(result_label)


def true_false_question():
    def on_click():
        root.withdraw()
        TrueFalseQuestions(root, true_false_button)
    return on_click


def on_closing():
    def on_click():
        sys.exit()
    return on_click

# Create a gui
def main(sub_root):
    global root, choice_frame, type_question_label, options_button, true_false_button
    root = tk.Tk()
    root.geometry("500x150")
    root.title("Database - Quiz")
    root.protocol("WM_DELETE_WINDOW", on_closing())

    # get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate the x and y coordinates for the window to be centered
    x = int((screen_width / 2) - (500 / 2))
    y = int((screen_height / 2) - (150 / 2) - 20)

    # set the position of the window to the center of the screen
    root.geometry("+{}+{}".format(x, y))

    type_question_label = tk.Label(
        root, text="What type of question's do you want?", font=("TkDefaultFont", 16))
    type_question_label.pack(pady=20)

    choice_frame = tk.Frame(root)
    choice_frame.pack(pady=10)

    true_false_button = tk.Button(
        choice_frame, text="True/False", width=10, command=true_false_question())
    true_false_button.pack(side=tk.LEFT, padx=10, pady=10, anchor="center")

    options_button = tk.Button(
        choice_frame, text="With options", width=10, command=options_questions(root, sub_root))
    options_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor="center")

    root.mainloop()

def back_fun(root, sub_root):
    def on_click():
        sub_root.withdraw()
        root.deiconify()
        options_button.config(command=check_frame(root, sub_root))
    return on_click

def check_frame(root, sub_root):
    def on_click():
        root.withdraw()
        sub_root.deiconify()
    return on_click

main(sub_root)
