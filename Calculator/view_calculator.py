import tkinter as tk
from tkinter import ttk
from math import sqrt
from style_calculator import Display_style
from model_calculator import Specials


class View():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("450x600")
        self.root.title("Calculator")
        self.root.resizable(0, 0)

        self.display_style()

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_label()

        # Digit
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 1), '.': (4, 2)
        }

        # Operation
        self.operations = {
            "/": "\u00F7",
            "*": "\u00D7",
            "-": "-",
            "+": "+"
        }

        self.button_frame = self.create_frame()
        self.button_frame.rowconfigure(0, weight=1)
        for i in range(1, 5):
            self.button_frame.rowconfigure(i, weight=1)
            self.button_frame.columnconfigure(i, weight=1)

        self.digit_buttons()
        self.operator_buttons()
        self.special_buttons()

    # Import class Display_style to get functions
    def display_style(self):
        self.d_style = Display_style()
        self.d_style.label_total_style()
        self.d_style.label_current_style()
        self.d_style.button_digit_style()
        self.d_style.button_operator_style()
        self.d_style.button_special_style()

    # Create display frame
    def create_display_frame(self):
        frame = ttk.Frame(self.root, height=221)
        frame.pack(expand=True, fill="both")
        return frame

    # Create display label
    def create_display_label(self):
        total_label = ttk.Label(self.display_frame, text=self.total_expression,
                                anchor=tk.E, style='Total.TLabel')
        total_label.pack(expand=True, fill='both')

        label = ttk.Label(self.display_frame,
                          text=self.current_expression, anchor=tk.E, style='Current.TLabel')
        label.pack(expand=True, fill="both")

        return total_label, label

    # Create frame
    def create_frame(self):
        frame = ttk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame

    # Create digit buttons
    def digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = ttk.Button(self.button_frame, text=str(
                digit), style='Digit.TButton', command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0],
                        column=grid_value[1], sticky=tk.NSEW)

    # Create operator buttons
    def operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = ttk.Button(self.button_frame,
                                text=symbol, style='Operator.TButton', command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i = i + 1

    # Create special buttons
    def special_buttons(self):
        self.clear_button()
        self.equals_button()
        self.square_button()
        self.sqrt_button()

    # Create equal button
    def equals_button(self):
        button = ttk.Button(self.button_frame, text="=",
                            style='Special.TButton', command=self.equals)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    # Create clear button
    def clear_button(self):
        button = ttk.Button(self.button_frame, text="AC",
                            style='Special.TButton', command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    # Create square button
    def square_button(self):
        button = ttk.Button(self.button_frame, text="x\u00b2",
                            style='Special.TButton', command=self.square)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    # Create sqrt button
    def sqrt_button(self):
        button = ttk.Button(self.button_frame, text="\u221ax",
                            style='Special.TButton', command=self.sqrts)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def update_label(self):
        self.label.config(text=self.current_expression[:10])

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def equals(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def clear(self):
        self.sp = Specials()
        self.current_expression, self.total_expression = self.sp.Clear()
        self.update_label()
        self.update_total_label()

    def square(self):
        e_square = self.total_expression
        e_square = "sqr(" + self.current_expression + ")"
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()
        self.total_label.config(text=e_square)

    def sqrts(self):
        e_sqrt = self.total_expression
        e_sqrt = "sqrt(" + self.current_expression + ")"
        self.current_expression = str(eval(f"sqrt({self.current_expression})"))
        self.update_label()
        self.total_label.config(text=e_sqrt)

    def run(self):
        self.root.mainloop()


def main():
    view = View()
    view.run()


if __name__ == '__main__':
    main()
