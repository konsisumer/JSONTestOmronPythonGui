import tkinter as tk
from tkinter import messagebox
from utils.helpers import send_json_data
import random
import string

# Helper function to generate a random string
def generate_random_string(length=10):
    """Generate a random string of the specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Helper function to append status messages
def append_status_message(message):
    """Append a status message to the status text box."""
    status_text.insert(tk.END, message + "\n")
    status_text.see(tk.END)  # Scroll to the latest message

# Function to send data
def send_data():
    try:
        data = {
            # "JobID" : 1,
            "JobName" : entry_name.get(),
            "A" : float(entry_a.get()),
            "B" : float(entry_b.get()),
            "C" : float(entry_c.get()),
            "BoxType" : int(entry_type.get()),
            "Orientation" : bool(var_orientation.get()),
            "Smallbox" : bool(var_smallbox.get()),
            "La" : int(entry_la.get()),
            "Lb" : int(entry_lb.get()),
            "Lc" : int(entry_lc.get()),
            "Enable" : bool(var_braille.get()),
            "Chars" : int(entry_chars.get()),
            "Pos" : int(entry_braille_pos.get()),
            "Corner" : int(entry_corner.get()),
            "Flap" : int(entry_flap.get()),
            "DistanceStart" : int(entry_distance_start.get()),
            "DistanceHeight" : int(entry_distance_height.get()),
            "Lines" : int(entry_lines.get()),
            "EmptyLines" : int(entry_empty_lines.get()),
            "NumMatrices" : int(entry_num_matrices.get())
        }
        url = entry_url.get()
        response_message = send_json_data(url, data)
        append_status_message(response_message)
    except ValueError as e:
        append_status_message(f"Error: Invalid input - {e}")
    except Exception as e:
        append_status_message(f"Error: Request failed - {e}")

# Helper function to create labeled entry fields
def create_labeled_entry(parent, label_text, default_value, row, column, width=10):
    tk.Label(parent, text=label_text).grid(row=row, column=column, padx=5, pady=5)
    entry = tk.Entry(parent, width=width)
    entry.insert(0, default_value)
    entry.grid(row=row, column=column + 1, padx=5, pady=5)
    return entry

# Create GUI
root = tk.Tk()
root.title("JSON Data Viewer")
root.geometry("800x1000")

# URL Input
tk.Label(root, text="URL:").pack(pady=5)
entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)
entry_url.insert(0, "http://192.168.250.1:8090/")

# Input fields for sending data
tk.Label(root, text="Send Data:").pack(pady=5)
input_frame = tk.Frame(root)
input_frame.pack(pady=5)

# Input fields
entry_a = create_labeled_entry(input_frame, "A:", "80.0", 0, 0)
entry_b = create_labeled_entry(input_frame, "B:", "25.0", 1, 0)
entry_c = create_labeled_entry(input_frame, "C:", "15.0", 2, 0)
entry_type = create_labeled_entry(input_frame, "TYPE:", "1", 3, 0)

tk.Label(input_frame, text="ORIENTATION:").grid(row=4, column=0, padx=5, pady=5)
var_orientation = tk.IntVar(value=0)
checkbox_orientation = tk.Checkbutton(input_frame, variable=var_orientation)
checkbox_orientation.grid(row=4, column=1, padx=5, pady=5)

tk.Label(input_frame, text="SMALLBOX:").grid(row=5, column=0, padx=5, pady=5)
var_smallbox = tk.IntVar(value=0)
checkbox_smallbox = tk.Checkbutton(input_frame, variable=var_smallbox)
checkbox_smallbox.grid(row=5, column=1, padx=5, pady=5)

entry_la = create_labeled_entry(input_frame, "La:", "190", 6, 0)
entry_lb = create_labeled_entry(input_frame, "Lb:", "150", 7, 0)
entry_lc = create_labeled_entry(input_frame, "Lc:", "110", 8, 0)

# Generate a random default value for NAME
entry_name = create_labeled_entry(input_frame, "NAME:", generate_random_string(), 9, 0, width=30)

# Additional fields
tk.Label(input_frame, text="Braille:").grid(row=10, column=0, padx=5, pady=5)
var_braille = tk.IntVar(value=0)
checkbox_braille = tk.Checkbutton(input_frame, variable=var_braille)
checkbox_braille.grid(row=10, column=1, padx=5, pady=5)

entry_chars = create_labeled_entry(input_frame, "Chars:", "16", 11, 0)
entry_braille_pos = create_labeled_entry(input_frame, "BraillePos:", "1", 12, 0)
entry_corner = create_labeled_entry(input_frame, "Corner:", "1", 13, 0)
entry_flap = create_labeled_entry(input_frame, "Flap:", "1", 14, 0)
entry_distance_start = create_labeled_entry(input_frame, "DistanceStart:", "8", 15, 0)
entry_distance_height = create_labeled_entry(input_frame, "DistanceHeight:", "8", 16, 0)
entry_lines = create_labeled_entry(input_frame, "Lines:", "2", 17, 0)
entry_empty_lines = create_labeled_entry(input_frame, "EmptyLines:", "0", 18, 0)
entry_num_matrices = create_labeled_entry(input_frame, "NumMatrices:", "8", 19, 0)

# Send Data Button
tk.Button(root, text="Send Data", command=send_data).pack(pady=10)

# Status output field
tk.Label(root, text="Status Messages:").pack(pady=5)
status_text = tk.Text(root, wrap="word", height=10, width=80)
status_text.pack(padx=10, pady=10)

root.mainloop()