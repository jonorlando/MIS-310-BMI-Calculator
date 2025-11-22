# Import the tkinter library for GUI development
import tkinter as tk


# ---------------------------------------------
# Function to calculate BMI when button is clicked
# ---------------------------------------------
def calculate_bmi():
    # Get the text entered by the user and convert it to float
    height = float(height_var.get())  # height in inches
    weight = float(weight_var.get())  # weight in pounds

    # Compute BMI using the formula for U.S. units
    bmi = weight / (height ** 2) * 703

    # Display the result in the Label by updating the StringVar
    result_var.set(f"Your BMI is {bmi:.2f}")


# ---------------------------------------------
# Create the main application window
# ---------------------------------------------
main_window = tk.Tk()  # Create a window object
main_window.title("BMI Calculator")  # Set the window title
main_window.geometry("400x250")  # Set the window size (width x height)

# ---------------------------------------------
# Create Tkinter variable objects (StringVar)
# These link the Entry boxes and Label text
# ---------------------------------------------
height_var = tk.StringVar()  # Variable to store height input
weight_var = tk.StringVar()  # Variable to store weight input
result_var = tk.StringVar()  # Variable to store and display result text

# ---------------------------------------------
# Create and position the height label and entry box
# ---------------------------------------------
tk.Label(main_window, text="Enter your height (inches):") \
    .grid(row=0, column=0, padx=10, pady=10, sticky="e")  # Label text on left
tk.Entry(main_window, textvariable=height_var) \
    .grid(row=0, column=1, padx=10, pady=10)  # Entry box on right

# ---------------------------------------------
# Create and position the weight label and entry box
# ---------------------------------------------
tk.Label(main_window, text="Enter your weight (pounds):") \
    .grid(row=1, column=0, padx=10, pady=10, sticky="e")  # Label text on left
tk.Entry(main_window, textvariable=weight_var) \
    .grid(row=1, column=1, padx=10, pady=10)  # Entry box on right

# ---------------------------------------------
# Create the button that calls calculate_bmi() when clicked
# ---------------------------------------------
tk.Button(main_window, text="Calculate BMI", command=calculate_bmi) \
    .grid(row=2, column=0, columnspan=2, pady=15)  # Centered button

# ---------------------------------------------
# Create a label to show the result stored in result_var
# ---------------------------------------------
tk.Label(main_window, textvariable=result_var, fg="blue", font=("Helvetica", 12, "bold")) \
    .grid(row=3, column=0, columnspan=2, pady=10)

# ---------------------------------------------
# Start the Tkinter event loop (keeps window open)
# ---------------------------------------------
main_window.mainloop()
