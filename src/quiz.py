import tkinter as tk
import random


class TrueFalseQuestions:
    def __init__(self, root, button):
        self.false_list = []
        with open('./src/questions/false_ans.txt', encoding="utf8") as f:
            line = f.readline()
            while line:
                self.false_list.append(line)
                line = f.readline()

        self.true_list = []
        with open('./src/questions/true_ans.txt', encoding="utf8") as f:
            line = f.readline()
            while line:
                self.true_list.append(line)
                line = f.readline()

        self.false_map = {key: "false" for key in self.false_list}
        self.true_map = {key: "true" for key in self.true_list}
        self.questions = {**self.false_map, **self.true_map}

        self.questions_list = random.sample(
            list(self.questions.keys()), len(self.questions.keys()))
        self.question_index = 0

        self.root = root
        self.button = button

        self.run()

    def run(self):

        global question

        def back_fun():
            def on_click():
                true_false_root.withdraw()
                self.button.config(
                    command= check_frame(self.root, true_false_root))
                self.root.deiconify()
            return on_click

        def check_frame(root, true_false_root):
            def on_click():
                root.withdraw()
                true_false_root.deiconify()
            return on_click

        def get_question(flag):
            global questions_list
            global question_index

            if flag == 0:
                question = self.questions_list[0]

            elif flag == 1:
                self.question_index += 1
                if (self.question_index == len(self.questions_list)):
                    self.question_index = 0
                    print("All questions answered!")
                question = self.questions_list[self.question_index]

            elif self.question_index == 0:
                question = self.questions_list[0]

            else:
                self.question_index -= 1
                question = self.questions_list[self.question_index]

            return question

        question = get_question(0)

        def check_answer(answer, result_label):
            def on_click():
                global question
                if self.questions[question].lower() == answer.lower():
                    result_label.config(text="Correct!", fg="green")
                else:
                    result_label.config(text="Incorrect!", fg="red")
            return on_click

        def next_question(result_label):
            def on_click():
                global question
                question = get_question(1)
                self.question_label.config(text=question)
                result_label.config(text="")
            return on_click

        def next_question_right(result_label):
            global question
            question = get_question(1)
            self.question_label.config(text=question)
            result_label.config(text="")

        def previous_question(result_label):
            def on_click():
                global question
                question = get_question(-1)
                self.question_label.config(text=question)
                result_label.config(text="")
            return on_click

        def previous_question_left(result_label):
            global question
            question = get_question(-1)
            self.question_label.config(text=question)
            result_label.config(text="")

        def handle_key(event):
            if event.keysym == "Right":
                next_question_right(self.result_label)
            elif event.keysym == "Left":
                previous_question_left(self.result_label)

        true_false_root = tk.Tk()
        true_false_root.geometry("750x250")
        true_false_root.title("True/False Questions")
        true_false_root.bind("<Key>", handle_key)
        true_false_root.overrideredirect(True)

        # get the screen width and height
        self.screen_width = true_false_root.winfo_screenwidth()
        self.screen_height = true_false_root.winfo_screenheight()

        # calculate the x and y coordinates for the window to be centered
        x = int((self.screen_width / 2) - (750 / 2))
        y = int((self.screen_height / 2) - (220 / 2) - 20)

        # set the position of the window to the center of the screen
        true_false_root.geometry("+{}+{}".format(x, y))

        self.back_button = tk.Button(true_false_root, text="Back", width=10, command=back_fun())
        self.back_button.pack(side=tk.LEFT, anchor=tk.NW, padx=15, pady=15)

        self.question_frame = tk.Frame(true_false_root, width=650, height=120)
        self.question_frame.pack_propagate(False)
        self.question_frame.pack(padx=10, pady=15)

        self.question_label = tk.Label(self.question_frame, text=question, font=(
            "TkDefaultFont", 16), wraplength=600)
        self.question_label.pack(anchor='w')

        self.answer_frame = tk.Frame(true_false_root)
        self.answer_frame.pack(pady=5)

        self.result_label = tk.Label(true_false_root, text="", font=("TkDefaultFont", 14))
        self.result_label.pack()

        self.previous_button = tk.Button(
            self.answer_frame, text="Previous", width=10, command=previous_question(self.result_label))
        self.previous_button.grid(row=0, column=0, padx=10, pady=10)

        self.true_button = tk.Button(self.answer_frame, text="True",
                                width=10, command=check_answer("true", self.result_label))
        self.true_button.grid(row=0, column=1, padx=5, pady=10)

        self.false_button = tk.Button(self.answer_frame, text="False",
                                width=10, command=check_answer("false", self.result_label))
        self.false_button.grid(row=0, column=2, padx=5, pady=10)

        self.next_button = tk.Button(self.answer_frame, text="Next",
                                width=10, command=next_question(self.result_label))
        self.next_button.grid(row=0, column=3, padx=10, pady=10)

        true_false_root.mainloop()

        return true_false_root
