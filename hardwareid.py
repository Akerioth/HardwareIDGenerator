import tkinter as tk
from tkinter import messagebox
import wmi
import hashlib

def get_hardware_id():
    c = wmi.WMI()
    identifiers = []

    try:
        cpu = c.Win32_Processor()[0]
        identifiers.append(cpu.ProcessorId.strip())
    except:
        identifiers.append("CPUNone")

    try:
        board = c.Win32_BaseBoard()[0]
        identifiers.append(board.SerialNumber.strip())
    except:
        identifiers.append("MBNone")

    try:
        disk = c.Win32_DiskDrive()[0]
        identifiers.append(disk.SerialNumber.strip())
    except:
        identifiers.append("DiskNone")

    try:
        bios = c.Win32_BIOS()[0]
        identifiers.append(bios.SerialNumber.strip())
    except:
        identifiers.append("BIOSNone")

    combined = "".join(identifiers).encode()
    return hashlib.sha256(combined).hexdigest()

# GUI Part
def generate_hw_id():
    try:
        hwid = get_hardware_id()
        result_label.config(text=f"Hardware ID:\n{hwid}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get Hardware ID:\n{e}")

# Create the window
root = tk.Tk()
root.title("Hardware ID Generator")
root.geometry("500x200")

# Button
generate_button = tk.Button(root, text="Generate", command=generate_hw_id, font=("Arial", 12))
generate_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Click 'Generate' to get your Hardware ID", wraplength=480, font=("Arial", 10))
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
