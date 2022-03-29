import tkinter as tk
from tkinter import messagebox
from math import sqrt, sin, cos, tan, exp, log, log10, pi, factorial, asin, acos, atan


class Calculadora(tk.Frame):

    # _MY_FONT = font.Font(family='Helvetica', size=10)
    _MATH = {"sqrt": sqrt, "sin": sin, "cos": cos, "tan": tan, "asin": asin, "acos": acos, "atan": atan,
             "e": exp, "ln": log, "log": log10, "pi": pi, "fact": factorial, "abs": abs}

    def __init__(self, tab):
        super().__init__()
        self._tab = tab
        # instance attr
        self._create_components()
        self.ans = ''

    def _create_components(self):
        # console
        input_frame = tk.Frame(self._tab, width=400, height=50, bg="#FFF3F3", relief=tk.SUNKEN)
        input_frame.pack(side=tk.TOP)
        self.input_box = tk.Entry(input_frame, font=("arial", 18, "bold"), width=30, justify=tk.RIGHT,
                                  exportselection=False)
        self.input_box.grid(row=0, column=0, ipady=10, pady=5)

        # Basic Operations Frame
        basic_frame = tk.Frame(self._tab, width=400, height=450, bg='#F58C8C')
        basic_frame.pack(side=tk.LEFT, padx=5)
        # row 0
        btn_c = tk.Button(basic_frame, text="AC", width=21, height=3,
                          bd=0, bg="#FFCBCB", cursor="hand2", command=self._clear)
        btn_c.grid(row=0, column=0, columnspan=2, padx=1, pady=1)

        btn_del = tk.Button(basic_frame, text="DEL", width=10, height=3,
                            bd=0, bg="#FFCBCB", cursor="hand2", command=self._delete_one)
        btn_del.grid(row=0, column=2, padx=1, pady=1)

        btn_div = tk.Button(basic_frame, text="/", width=10, height=3, bd=0, bg="#FFCBCB",
                            cursor="hand2", command=lambda: self._event_click("/"))
        btn_div.grid(row=0, column=3, padx=1, pady=1)
        # row 1
        tk.Button(basic_frame, text="7", width=10, height=3, bd=0,
                  bg="#fff", cursor="hand2", command=lambda: self._event_click("7")
                  ).grid(row=1, column=0, padx=1, pady=1)
        tk.Button(basic_frame, text="8", width=10, height=3, bd=0,
                  bg="#fff", cursor="hand2", command=lambda: self._event_click("8")
                  ).grid(row=1, column=1, padx=1, pady=1)
        tk.Button(basic_frame, text="9", width=10, height=3, bd=0,
                  bg="#fff", cursor="hand2", command=lambda: self._event_click("9")
                  ).grid(row=1, column=2, padx=1, pady=1)
        tk.Button(basic_frame, text="*", width=10, height=3, bd=0,
                  bg="#FFCBCB", cursor="hand2",
                  command=lambda: self._event_click("*")
                  ).grid(row=1, column=3, padx=1, pady=1)
        # row 2
        tk.Button(basic_frame, text="4", width=10, height=3, bd=0,
                  bg="#fff", cursor="hand2", command=lambda: self._event_click("4")
                  ).grid(row=2, column=0, padx=1, pady=1)
        tk.Button(basic_frame, text="5", width=10, height=3, bd=0,
                  bg="#fff", cursor="hand2", command=lambda: self._event_click("5")
                  ).grid(row=2, column=1, padx=1, pady=1)
        tk.Button(basic_frame, text="6", width=10, height=3, bd=0,
                  bg="#fff", cursor="hand2", command=lambda: self._event_click("6")
                  ).grid(row=2, column=2, padx=1, pady=1)
        tk.Button(basic_frame, text="-", width=10, height=3, bd=0,
                  bg="#FFCBCB", cursor="hand2",
                  command=lambda: self._event_click("-")
                  ).grid(row=2, column=3, padx=1, pady=1)
        # row3
        tk.Button(basic_frame, text="1", width=10, height=3, bd=0,
                  bg="#fff", cursor="hand2", command=lambda: self._event_click("1")
                  ).grid(row=3, column=0, padx=1, pady=1)
        tk.Button(basic_frame, text="2", width=10, height=3, bd=0,
                  bg="#fff", cursor="hand2", command=lambda: self._event_click("2")
                  ).grid(row=3, column=1, padx=1, pady=1)
        tk.Button(basic_frame, text="3", width=10, height=3, bd=0,
                  bg="#fff", cursor="hand2", command=lambda: self._event_click("3")
                  ).grid(row=3, column=2, padx=1, pady=1)
        tk.Button(basic_frame, text="+", width=10, height=3, bd=0,
                  bg="#FFCBCB", cursor="hand2",
                  command=lambda: self._event_click("+")
                  ).grid(row=3, column=3, padx=1, pady=1)
        # row4
        tk.Button(basic_frame, text="0", width=10, height=3, bd=0,
                  bg="#fff", cursor="hand2", command=lambda: self._event_click("0")
                  ).grid(row=4, column=0, padx=1, pady=1)
        tk.Button(basic_frame, text=".", width=10, height=3, bd=0,
                  bg="#fff", cursor="hand2", command=lambda: self._event_click(".")
                  ).grid(row=4, column=1, padx=1, pady=1)
        tk.Button(basic_frame, text="ANS", width=10, height=3, bd=0,
                  bg="#fff", cursor="hand2", command=self._retrieve_result
                  ).grid(row=4, column=2, padx=1, pady=1)
        tk.Button(basic_frame, text="=", width=10, height=3, bd=0,
                  bg="#FF7D7D", cursor="hand2", command=self._eval_expression
                  ).grid(row=4, column=3, padx=1, pady=1)

        # Advanced Operations Frame
        advanced_frame = tk.Frame(self._tab, width=300, height=450, bg="#FFCD76")
        advanced_frame.pack(side=tk.RIGHT, padx=5)
        # row 0
        tk.Button(advanced_frame, text="(", width=10, height=3, bd=0,
                  bg="#FFEAC4", cursor="hand2", command=lambda: self._event_click("(")
                  ).grid(row=0, column=0, padx=1, pady=1)
        tk.Button(advanced_frame, text=")", width=10, height=3, bd=0,
                  bg="#FFEAC4", cursor="hand2", command=lambda: self._event_click(")")
                  ).grid(row=0, column=1, padx=1, pady=1)
        tk.Button(advanced_frame, text="\u03C0", width=10, height=3, bd=0,
                  bg="#FFEAC4", cursor="hand2", command=lambda: self._event_click("pi")
                  ).grid(row=0, column=2, padx=1, pady=1)
        # row 1
        tk.Button(advanced_frame, text="sin(x)", width=10, height=3, bd=0,
                  bg="#FFEAC4", cursor="hand2", command=lambda: self._event_click("sin(")
                  ).grid(row=1, column=0, padx=1, pady=1)
        tk.Button(advanced_frame, text="cos(x)", width=10, height=3, bd=0,
                  bg="#FFEAC4", cursor="hand2", command=lambda: self._event_click("cos(")
                  ).grid(row=1, column=1, padx=1, pady=1)
        tk.Button(advanced_frame, text="tan(x)", width=10, height=3, bd=0,
                  bg="#FFEAC4", cursor="hand2", command=lambda: self._event_click("tan(")
                  ).grid(row=1, column=2, padx=1, pady=1)
        # row2
        tk.Button(advanced_frame, text="asin(x)", width=10, height=3, bd=0,
                  bg="#FFEAC4", cursor="hand2", command=lambda: self._event_click("asin(")
                  ).grid(row=2, column=0, padx=1, pady=1)
        tk.Button(advanced_frame, text="acos(x)", width=10, height=3, bd=0,
                  bg="#FFEAC4", cursor="hand2", command=lambda: self._event_click("acos(")
                  ).grid(row=2, column=1, padx=1, pady=1)
        tk.Button(advanced_frame, text="atan(x)", width=10, height=3, bd=0,
                  bg="#FFEAC4", cursor="hand2", command=lambda: self._event_click("atan(")
                  ).grid(row=2, column=2, padx=1, pady=1)
        # row 3
        tk.Button(advanced_frame, text="e^(x)", width=10, height=3, bd=0,
                  bg="#FFEAC4", cursor="hand2", command=lambda: self._event_click("e(")
                  ).grid(row=3, column=0, padx=1, pady=1)
        tk.Button(advanced_frame, text="ln(x)", width=10, height=3, bd=0,
                  bg="#FFEAC4", cursor="hand2", command=lambda: self._event_click("ln(")
                  ).grid(row=3, column=1, padx=1, pady=1)
        tk.Button(advanced_frame, text="log(x)", width=10, height=3, bd=0,
                  bg="#FFEAC4", cursor="hand2", command=lambda: self._event_click("log(")
                  ).grid(row=3, column=2, padx=1, pady=1)
        # row 4
        tk.Button(advanced_frame, text="\u221A(x)", width=10, height=3, bd=0,
                  bg="#FFEAC4", cursor="hand2", command=lambda: self._event_click("sqrt(")
                  ).grid(row=4, column=0, padx=1, pady=1)
        tk.Button(advanced_frame, text="x^y", width=10, height=3, bd=0,
                  bg="#FFEAC4", cursor="hand2", command=lambda: self._event_click("**")
                  ).grid(row=4, column=1, padx=1, pady=1)
        tk.Button(advanced_frame, text="fact(x)", width=10, height=3, bd=0,
                  bg="#FFEAC4", cursor="hand2", command=lambda: self._event_click("fact(")
                  ).grid(row=4, column=2, padx=1, pady=1)

    def _clear(self):
        self.input_box.delete(0, tk.END)

    def _delete_one(self):
        index = self._cursor_position()
        self.input_box.delete(index - 1, index)

    def _event_click(self, element):
        index = self._cursor_position()
        self.input_box.insert(index, element)

    def _retrieve_result(self):
        index = self._cursor_position()
        self.input_box.insert(index, self.ans)

    def _cursor_position(self):
        return self.input_box.index(tk.INSERT)

    def _eval_expression(self):
        calculation = self.input_box.get()
        try:
            if calculation:
                result = str(eval(calculation, {'__builtins__': None}, Calculadora._MATH))
                self.input_box.delete(0, tk.END)
                self.input_box.insert(0, result)
                self.ans = result
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")
            self._clear()
