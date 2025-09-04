import tkinter as tk

# Button click function
# runs when we click any no/operator button
def press(key):
    entry_field.insert(tk.END, key)

# Clear function
# delete everything
def clear():
    entry_field.delete(0, tk.END)

# Evaluate expression
def equal():
    try:
        result = str(eval(entry_field.get()))
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, result)
    except:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")

# Create main window
root = tk.Tk()
root.title("Shivaas Calculator")
root.geometry("300x400") #for window size

# Entry field
entry_field = tk.Entry(root, font=("Arial", 20), bd=8, relief="ridge", justify="right")
entry_field.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Button layout
buttons =[
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create buttons dynamically
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        if btn == "=":
            b = tk.Button(frame, text=btn, font=("Arial", 18), command=equal)
        else:
            b = tk.Button(frame, text=btn, font=("Arial", 18),
                          command=lambda x=btn: press(x))
        b.pack(side="left", expand=True, fill="both")

# Clear button
clear_btn = tk.Button(root, text="C", font=("Arial", 18), command=clear)
clear_btn.pack(expand=True, fill="both")

# Run app
root.mainloop()
