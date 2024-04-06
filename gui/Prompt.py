import tkinter as tk
from tkinter import messagebox
from loading import main_screen
import sys
import os
import subprocess
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from python_scripts import *
# Now you can import the module using relative import
entered_text = ''
current_dir = os.path.abspath(os.getcwd())
current_dir = current_dir.replace('\\', '/')
parent = current_dir
current_dir += '/gui'

def open_tkinter():
    global prompt
    root = tk.Tk()
    root.geometry("1000x500")  # Increased window height
    root.title("Prompt Window")

    # Load the background image
    background_image = tk.PhotoImage(file=current_dir+"/window_blur.png")

    # Create a Label widget to display the background image
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    entry_font_size = 14  # Increased font size for better readability
    text_box_width = 80  # Increased width of the Text widget
    text_box_height = 15  # Increased height of the Text widget

    text_box = tk.Text(root, width=text_box_width, height=text_box_height, font=("Arial", entry_font_size), bd=0, relief=tk.SOLID)
    text_box.insert(tk.END, "Enter your prompt here")  # Default input text
    text_box.pack(pady=20)  # Adjusted padding for the text box

    # Calculate the x-coordinate to center the text box
    x_coordinate = (root.winfo_width() - text_box_width * 8) / 2
    text_box.place(relx=0.5, rely=0.4, anchor="center")

    def submit():
        global entered_text
        entered_text = text_box.get("1.0", tk.END).strip()
        if entered_text == "":
            messagebox.showerror("Error", "Please enter a valid prompt.")
        else:
            print("Text entered:\n", entered_text)
            root.destroy()
            with open(parent+'/python_scripts/prompt.txt', 'w') as f:
                f.write(entered_text)
                f.close()
            subprocess.run('python ./python_scripts/story_gen.py')
            main_screen()
            

    submit_button = tk.Button(root, text="Generate", command=submit, bg="#9DD147", fg="black", relief=tk.FLAT, width=20, height=2)
      # Flat colors
    submit_button.pack(pady=10)  # Adjusted padding for the submit button
    submit_button.place(relx=0.5, rely=0.8, anchor="center")  # Placed below the text box

    root.mainloop()

# Test the function
# open_tkinter()
