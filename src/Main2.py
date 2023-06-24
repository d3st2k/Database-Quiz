import random
import csv
import tkinter as tk
from quiz import TrueFalseQuestions
from translate import Translator
import sys

# Global values
rand_generated_numbers = []
sub_root = tk.Tk()
sub_root.withdraw()
position = 0

# You can find a comprehensive list of language codes used in the ISO 639-1 standard on this Wikipedia page: List of ISO 639-1 codes. By referring to this list, you can easily find the language code shortcuts for various languages. Read READ-ME/Extra Stuff for more explanations.
target_language = "en"  # "sq" represents Albanian
translator = Translator(to_lang=target_language)


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
    global position
    randNumber = 0
    if (number == -1):
        if (position > 0):
            position -= 1
            rand = rand_generated_numbers[position]
        else:
            rand = -1
        return rand
    else:
        while (True):
            if (len(rand_generated_numbers) == 240):
                rand_generated_numbers.clear()
                rand = 240
                break
            # Generate a random number
            randNumber = random.randint(0, 239)
            if (randNumber not in rand_generated_numbers):
                position = len(rand_generated_numbers) - 1
                rand_generated_numbers.append(randNumber)
                position += 1
                rand = randNumber
                break
        return rand


def get_question(flag):
    # Get a random number
    global rand, question, option_a, option_b, option_c, option_d, answerColumn
    rand = generate_random(flag)
    options_available = [2, 3, 4, 5]

    if (rand > -1 and rand < 240):
        # Get all the questions and options from the database
        question = str(translator.translate(vargu_ID[rand][1]))

        option_a = str(
            vargu_ID[rand][options_available.pop(random.randint(0, 3))])

        option_b = str(
            vargu_ID[rand][options_available.pop(random.randint(0, 2))])

        option_c = str(
            vargu_ID[rand][options_available.pop(random.randint(0, 1))])

        option_d = str(vargu_ID[rand][options_available.pop(0)])

        options_available = [2, 3, 4, 5]

        answerColumn = str(vargu_ID[rand][6])
    return rand


def previous_question(result_label):
    def on_click():
        if (int(get_question(-1)) < 0):
            result_label.config(
                text="There are no more previous questions!", fg="red")
        else:
            if (target_language != "en"):
                question_label.config(text=question)
                option_a_button.config(
                    text=str(translator.translate(option_a)), command=check_answer(option_a, result_label))
                option_b_button.config(
                    text=str(translator.translate(option_b)), command=check_answer(option_b, result_label))
                option_c_button.config(
                    text=str(translator.translate(option_c)), command=check_answer(option_c, result_label))
                option_d_button.config(
                    text=str(translator.translate(option_d)), command=check_answer(option_d, result_label))
                result_label.config(text="")
            else:
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
        if (int(get_question(0)) == 240):
            result_label.config(
                text="You have completed all the questions!", fg="green")
        else:
            if (target_language != "en"):
                question_label.config(text=question)
                option_a_button.config(
                    text=str(translator.translate(option_a)), command=check_answer(option_a, result_label))
                option_b_button.config(
                    text=str(translator.translate(option_b)), command=check_answer(option_b, result_label))
                option_c_button.config(
                    text=str(translator.translate(option_c)), command=check_answer(option_c, result_label))
                option_d_button.config(
                    text=str(translator.translate(option_d)), command=check_answer(option_d, result_label))
                result_label.config(text="")
            else:
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
    if (target_language != "en"):
        question_label.config(text=question)
        option_a_button.config(
            text=str(translator.translate(option_a)), command=check_answer(option_a, result_label))
        option_b_button.config(
            text=str(translator.translate(option_b)), command=check_answer(option_b, result_label))
        option_c_button.config(
            text=str(translator.translate(option_c)), command=check_answer(option_c, result_label))
        option_d_button.config(
            text=str(translator.translate(option_d)), command=check_answer(option_d, result_label))
        result_label.config(text="")
    else:
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

    count = get_question(-1)
    if (target_language != "en"):
        question_label.config(text=question)
        option_a_button.config(
            text=str(translator.translate(option_a)), command=check_answer(option_a, result_label))
        option_b_button.config(
            text=str(translator.translate(option_b)), command=check_answer(option_b, result_label))
        option_c_button.config(
            text=str(translator.translate(option_c)), command=check_answer(option_c, result_label))
        option_d_button.config(
            text=str(translator.translate(option_d)), command=check_answer(option_d, result_label))
        result_label.config(text="")
    else:
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
            if (vargu_ID[rand][7] > 0.1):
                vargu_ID[rand][7] -= 0.1
        else:
            result_label.config(text="Incorrect!", fg="red")
            if (vargu_ID[rand][7] < 1):
                vargu_ID[rand][7] += 0.1
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

        if(target_language != "en"):
            option_a_button = tk.Button(answer_frame, text=str(translator.translate(option_a)),
                                        wraplength=300, command=check_answer(option_a, result_label))
            option_a_button.grid(row=0, column=1, padx=10, pady=10)
            option_b_button = tk.Button(answer_frame, text=str(translator.translate(option_b)),
                                        wraplength=300, command=check_answer(option_b, result_label))
            option_b_button.grid(row=0, column=2, padx=10, pady=10)
            option_c_button = tk.Button(answer_frame, text=str(translator.translate(option_c)),
                                        wraplength=300, command=check_answer(option_c, result_label))
            option_c_button.grid(row=1, column=1, padx=10, pady=10)
            option_d_button = tk.Button(answer_frame, text=str(translator.translate(option_d)),
                                        wraplength=300, command=check_answer(option_d, result_label))
            option_d_button.grid(row=1, column=2, padx=10, pady=10)
        else:
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
