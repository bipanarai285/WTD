import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to connect to the database
def connect_db():
    try:
        conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Default MySQL username
    password="password",  # Leave blank if no password is set
    database="hospital_db"
)

        
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database connection error: {err}")
        return None

# Function to open the Register Page
def open_register():
    register_window = tk.Toplevel()
    register_window.title("Register")
    register_window.geometry("400x350")
    register_window.configure(bg="#F08080")  # Light coral background

    # Title label for the Register Page
    tk.Label(register_window, text="Register", font=('Helvetica', 18, 'bold'), bg="#F08080").pack(pady=20)

    # Phone number label and entry
    tk.Label(register_window, text="Phone Number", font=('Helvetica', 12), bg="#F08080").pack(pady=5)
    phone_entry = tk.Entry(register_window, width=30)
    phone_entry.pack(pady=5)

    # Name label and entry
    tk.Label(register_window, text="Name", font=('Helvetica', 12), bg="#F08080").pack(pady=5)
    name_entry = tk.Entry(register_window, width=30)
    name_entry.pack(pady=5)

    # Register button
    tk.Button(register_window, text="Submit", width=10, font=('Helvetica', 12), bg="green", fg="white",
              command=lambda: register_patient(name_entry.get(), phone_entry.get())).pack(pady=20)

    # Close button to go back to the login interface
    tk.Button(register_window, text="Close", command=register_window.destroy, width=10, font=('Helvetica', 12),
              bg="gray", fg="white").pack(pady=10)

# Function to register patient in the database
def register_patient(name, phone):
    if name and phone:
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()

                # Insert patient details into the patients table
                cursor.execute("INSERT INTO patients (name, phone) VALUES (%s, %s)", (name, phone))
                conn.commit()

                messagebox.showinfo("Success", "Patient Registered Successfully")
                open_login(name, phone)
                cursor.close()
                conn.close()

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}")
        else:
            messagebox.showerror("Error", "Failed to connect to the database.")
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields")

# Function to open the Login Page with patient details
def open_login(name, phone):
    login_window = tk.Toplevel()
    login_window.title("Login")
    login_window.geometry("400x300")
    login_window.configure(bg="#FFFFE0")  # Light yellow background

    # Title label for the Login Page
    tk.Label(login_window, text="Login", font=('Helvetica', 18, 'bold'), bg="#FFFFE0").pack(pady=20)

    # Display Patient Details
    tk.Label(login_window, text="Name of Patient:", font=('Helvetica', 12), bg="#FFFFE0").pack(pady=5)
    tk.Label(login_window, text=name, font=('Helvetica', 12), bg="#FFFFE0").pack(pady=5)

    tk.Label(login_window, text="Phone Number:", font=('Helvetica', 12), bg="#FFFFE0").pack(pady=5)
    tk.Label(login_window, text=phone, font=('Helvetica', 12), bg="#FFFFE0").pack(pady=5)

    # Login button
    tk.Button(login_window, text="Login", width=10, font=('Helvetica', 12), bg="blue", fg="white",
              command=lambda: open_home_page(name, phone)).pack(pady=20)

    # Close button
    tk.Button(login_window, text="Close", command=login_window.destroy, width=10, font=('Helvetica', 12), bg="gray",
              fg="white").pack(pady=10)

# Placeholder function for the home page
def open_home_page(name, phone):
    # Home page logic here
    pass

# Main Tkinter window setup
root = tk.Tk()
root.title("Hospital Management System")
root.geometry("300x200")

# Main window buttons
tk.Button(root, text="Register", command=open_register, width=15, font=('Helvetica', 12), bg="green", fg="white").pack(pady=20)
tk.Button(root, text="Exit", command=root.quit, width=15, font=('Helvetica', 12), bg="red", fg="white").pack(pady=20)

root.mainloop()
