import tkinter as tk

def on_click(event):
    current_text = result_entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            result_entry.delete(0, tk.END)
            result_entry.insert(tk.END, str(result))
        except Exception as e:
            result_entry.delete(0, tk.END)
            result_entry.insert(tk.END, "Error")

    elif button_text == "C":
        result_entry.delete(0, tk.END)

    else:
        result_entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

result_entry = tk.Entry(root, font=("Helvetica", 20), bd=0, justify=tk.RIGHT)
result_entry.pack(padx=20, pady=20, fill=tk.X)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
    ("C",)
]

for row in buttons:
    button_row = tk.Frame(button_frame)
    button_row.pack()

    for button_text in row:
        button = tk.Button(button_row, text=button_text, font=("Helvetica", 18), relief=tk.GROOVE, width=5, height=2)
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button.bind("<Button-1>", on_click)

root.mainloop()
