import tkinter as tk
import matplotlib.pyplot as plt

# Create main window
root = tk.Tk()
root.title("Simple Calculator with History Plot")
root.geometry("400x500")

# Display variable for calculator screen
display_text = tk.StringVar()
display_text.set("")  # Start with an empty display

# Display for calculator
display = tk.Entry(root, textvariable=display_text, font=("Arial", 18), justify="right")
display.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

# Buttons and layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# History list to store calculations
history = []

# Function to update display with button text
def button_click(value):
    current = display_text.get()
    display_text.set(current + value)

# Clear function
def clear():
    display_text.set("")

# Calculate function
def calculate(operation):
    if operation == "=":
        try:
            expression = display_text.get()  # Get full expression
            result = eval(expression)  # Calculate result
            display_text.set(str(result))

            # Append the expression and result to history
            history.append((expression, result))
        except:
            display_text.set("Error")
    elif operation == "C":
        clear()

# Add buttons to grid
row_val = 1
col_val = 0
for button in buttons:
    action = lambda x=button: button_click(x) if x not in ['=', 'C'] else None
    btn = tk.Button(root, text=button, width=5, height=2, command=action if action else lambda x=button: calculate(x))
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Assign functions to `=` and `C` buttons
for widget in root.grid_slaves():
    if widget.cget("text") == "=":
        widget.config(command=lambda: calculate("="))
    elif widget.cget("text") == "C":
        widget.config(command=clear)

# Plot history function
def plot_history():
    if not history:
        print("No history to plot.")
        return
    
    # Extract expressions and results for plotting
    expressions = [item[0] for item in history[-10:]]  # Get last 10 expressions
    results = [item[1] for item in history[-10:]]  # Get last 10 results

    # Plot bar chart with expressions as labels
    plt.figure(figsize=(10, 5))
    bars = plt.bar(expressions, results, color="skyblue", label="Resulting Value of the Expression")
    plt.xlabel("Expressions")
    plt.ylabel("Results")
    plt.title("Calculation History with Expressions")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Add legend
    plt.legend()

    plt.show()

# Button for plotting history
plot_button = tk.Button(root, text="Plot History", command=plot_history, width=20, height=2)
plot_button.grid(row=row_val, column=0, columnspan=4, padx=5, pady=5)

# Mainloop
root.mainloop()
