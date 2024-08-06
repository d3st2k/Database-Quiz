import pandas as pd
import tkinter as tk
from quiz import TrueFalseQuestions
import sys

# Global values
sub_root = tk.Tk()
sub_root.withdraw()
questionIndex = 0

# Input dataset path
inputDatasetPath = "src/questions/Latest_Dataset.csv"

def getDataset():
    # Read the dataset that contains questions and options
    dataset = pd.read_csv(inputDatasetPath, delimiter=';', header=0)
    
    # Shuffle the rows in the DataFrame so that we get different questions each time we run this program
    dataset = dataset.sample(frac=1).reset_index(drop=True)
    return dataset

def get_question(flag, questionIndex):
    if flag == -1:
        questionIndex = max(0, questionIndex - 1)
        questionData = dataset.loc[questionIndex]
    else:
        questionIndex = min(240, questionIndex + 1)
        questionData = dataset.loc[questionIndex]
    return questionData

def config_labels(flag):
    question, option_a, option_b, option_c, option_d, answer, probability= get_question(flag, questionIndex)
    question_label.config(text=question)
    option_a_button.config(
        text=option_a, command=check_answer(option_a, answer))
    option_b_button.config(
        text=option_b, command=check_answer(option_b, answer))
    option_c_button.config(
        text=option_c, command=check_answer(option_c, answer))
    option_d_button.config(
        text=option_d, command=check_answer(option_d, answer))
    result_label.config(text="")

def previous_question():
    def on_click():
        config_labels(-1)
    return on_click

def next_question():
    def on_click():
        config_labels(0)
    return on_click

def next_question_right():
    config_labels(0)

def previous_question_left():
    config_labels(0)

def check_answer(option, answer):
    def on_click():
        if str(option).lower().replace(".,", "").strip() == str(answer).lower().replace(".,", "").strip():
            result_label.config(text="Correct!", fg="green")
        else:
            result_label.config(text="Incorrect!", fg="red")
    return on_click

def options_questions(root, sub_root):
    def on_click():
        global question_label, option_a_button, option_b_button, option_c_button, option_d_button, result_label
        root.withdraw()

        sub_root.title("Questions with options")
        sub_root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        sub_root.deiconify()
        sub_root.protocol("WM_DELETE_WINDOW", on_closing())
        sub_root.bind("<Key>", handle_key)
        sub_root.overrideredirect(True)
        
        widthSpace = root.winfo_screenwidth() // 2
        heightSpace = root.winfo_screenwidth() // 3

        question, option_a, option_b, option_c, option_d, answer, probability = get_question(0, questionIndex)
        
        back_button = tk.Button(sub_root, text="Back",
                                width=10, command=back_fun(root, sub_root))
        back_button.pack(side=tk.LEFT, anchor=tk.NW, padx=30, pady=30)

        question_frame = tk.Frame(sub_root, width=widthSpace, height=200)
        question_frame.pack_propagate(False)
        question_frame.pack(padx=5, pady=30)
        
        question_label = tk.Label(question_frame, text=question, font=(
            "TkDefaultFont", 16), wraplength=700)
        question_label.pack(anchor="w")
        answer_frame = tk.Frame(sub_root, width=widthSpace, height=heightSpace)
        answer_frame.pack_propagate(False)
        answer_frame.pack(pady=30)
        result_label = tk.Label(sub_root, text="", font=("TkDefaultFont", 14))
        previous_button = tk.Button(
            sub_root, text="Previous", width=10, command=previous_question())
        previous_button.pack(side=tk.LEFT, anchor=tk.SW, padx=10, pady=15)
        next_button = tk.Button(
            sub_root, text="Next", width=10, command=next_question())
        next_button.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=15)
        result_label.pack()
        option_a_button = tk.Button(answer_frame, text=option_a,
                                    wraplength=300, command=check_answer(option_a, answer))
        option_a_button.grid(row=0, column=1, padx=10, pady=10)
        option_b_button = tk.Button(answer_frame, text=option_b,
                                    wraplength=300, command=check_answer(option_b, answer))
        option_b_button.grid(row=0, column=2, padx=10, pady=10)
        option_c_button = tk.Button(answer_frame, text=option_c,
                                    wraplength=300, command=check_answer(option_c, answer))
        option_c_button.grid(row=1, column=1, padx=10, pady=10)
        option_d_button = tk.Button(answer_frame, text=option_d,
                                    wraplength=300, command=check_answer(option_d, answer))
        option_d_button.grid(row=1, column=2, padx=10, pady=10)

    return on_click


def handle_key(event):
    if event.keysym == "Right":
        next_question_right()
    elif event.keysym == "Left":
        previous_question_left()

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
    global dataset
    dataset = getDataset()
    
    global root, choice_frame, type_question_label, options_button, true_false_button
    root = tk.Tk()
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.title("Database - Quiz")
    root.protocol("WM_DELETE_WINDOW", on_closing())

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

# Run this program only from when this file is ran
if __name__ == "__main__":
    main(sub_root)
