from tkinter import ttk


class Display_style():
    def __init__(self):
        pass

    def label_total_style(self):
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure(
            'Total.TLabel',
            font=("Arial", 16),
            background='#F5F5F5',
            foreground='#25265E'
        )

    def label_current_style(self):
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure(
            'Current.TLabel',
            font=("Arial", 40, "bold"),
            background='#F5F5F5',
            foreground='#25265E')

    def button_digit_style(self):
        style = ttk.Style()
        style.theme_use('alt')
        style.configure(
            'Digit.TButton',
            font=("Arial", 24, "bold"),
            background="#7a7a7a",
            foreground="#fff",
            borderwidth=5)
        style.map(
            'Digit.TButton',
            background=[('active', '#4dd7fa'),
                        ('disabled', '#f0f0f0')])

    def button_operator_style(self):
        style = ttk.Style()
        style.theme_use('alt')
        style.configure(
            'Operator.TButton',
            font=("Arial", 28),
            background="#ffa834",
            foreground="#fff",
            borderwidth=5)
        style.map(
            'Operator.TButton',
            background=[('active', '#4dd7fa'),
                        ('disabled', '#f0f0f0')])

    def button_special_style(self):
        style = ttk.Style()
        style.theme_use('alt')
        style.configure(
            'Special.TButton',
            font=("Arial", 20),
            background="#c0c0c0",
            foreground="#000000",
            borderwidth=5)
        style.map(
            'Special.TButton',
            background=[('active', '#4dd7fa'),
                        ('disabled', '#f0f0f0')])


def main():
    pass


if __name__ == '__main__':
    main()
