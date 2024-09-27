import ast
from tkinter import *

root = Tk()
root.title("Apple-like Calculator")
root.geometry("400x600")
root.configure(bg="#F2F2F7")  # Light background

i = 0

# Custom fonts and padding for Apple-like design
display_font = ('Helvetica', 24)
button_font = ('Helvetica', 20)
button_padx = 10
button_pady = 10

# Styling for the Entry display (input field)
display = Entry(root, bg='#333333', fg='white', font=display_font, bd=0, justify=RIGHT)
display.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky=W + E)


# Define the button functionality
def get_num(num):
    global i
    display.insert(i, num)
    i = i + 1


def get_operator(op):
    global i
    display.insert(i, op)
    i = i + len(op)


def clear_all():
    display.delete(0, END)


def undo():
    entire_string = display.get()
    if len(entire_string):
        new_text = entire_string[:-1]
        clear_all()
        display.insert(0, new_text)
    else:
        clear_all()


def calculate():
    entire_text = display.get()
    try:
        node = ast.parse(entire_text, mode="eval")
        result = eval(compile(node, '<string>', 'eval'))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")


# Custom button generator
def create_button(text, row, col, command, bg="#F2F2F7", fg="#007AFF", width=4, height=2):
    button = Button(root, text=text, bg=bg, fg=fg, font=button_font, relief=FLAT,
                    command=command, width=width, height=height)
    button.grid(row=row, column=col, padx=button_padx, pady=button_pady, sticky=NSEW)


# Adding buttons for numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        create_button(button_text, x + 2, y, command=lambda text=button_text: get_num(text))
        counter += 1

# Adding zero
create_button("0", 5, 1, command=lambda: get_num(0))

# Adding clear and equals button
create_button("AC", 5, 0, command=lambda: clear_all(), bg="#FF3B30", fg="white")
create_button("=", 5, 2, command=lambda: calculate(), bg="green", fg="white")

# Adding undo button
create_button("⌫", 1, 3, command=lambda: undo(), bg="#FF9500", fg="white")

# Adding operation buttons
operations = ['+', '-', '*', '/', '(', ')', '%']
for idx, operator in enumerate(operations):
    row = idx // 2 + 2
    col = 3 if idx % 2 == 0 else 2
    create_button(operator, row, col, command=lambda op=operator: get_operator(op), fg="#007AFF")

# Add exponentiation separately
create_button("^", 1, 2, command=lambda: get_operator('**'), fg="#007AFF")


# Add grid resizing for better layout
root.grid_columnconfigure((0, 1, 2, 3), weight=1)
root.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

root.mainloop()
