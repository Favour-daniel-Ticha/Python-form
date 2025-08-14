import tkinter as tk
from tkinter import messagebox
import csv

# Function to save contact info
def save_data():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    message = message_entry.get("1.0", tk.END)

    if not name or not email or not phone:
        messagebox.showwarning("Missing Info", "Please fill in all fields.")
        return

    with open("contacts.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone, message.strip()])

    messagebox.showinfo("Success", "Contact info saved successfully!")
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    message_entry.delete("1.0", tk.END)

# Creating the main window
window = tk.Tk()
window.title("Contact Form")
window.geometry("100x100")

# Labels and Entries
tk.Label(window, text="Name").pack()
name_entry = tk.Entry(window, width=50)
name_entry.pack()

tk.Label(window, text="Email").pack()
email_entry = tk.Entry(window, width=50)
email_entry.pack()

tk.Label(window, text="Phone").pack()
phone_entry = tk.Entry(window, width=50)
phone_entry.pack()

tk.Label(window, text="Message").pack()
message_entry = tk.Text(window, width=50, height=5)
message_entry.pack()

tk.Button(window, text="Submit", command=save_data).pack(pady=10)

# Start the app
window.mainloop()