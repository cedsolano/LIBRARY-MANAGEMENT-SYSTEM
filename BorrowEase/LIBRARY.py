import customtkinter as ctk
from tkinter import Listbox, messagebox

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("BorrowEase Login")
        self.root.geometry("1500x800")
        self.root.configure(fg_color="#27374D")  # Background color

        self.users = {
            "admin": "admin123",
            "user1": "password1",
            "user2": "password2"
        }
        
        login_frame = ctk.CTkFrame(root, width=1200, height=500, corner_radius=10, fg_color="#526D82")
        login_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.title_label = ctk.CTkLabel(master=login_frame, text="BORROW EASE", font=("Arial", 24, "bold"), text_color="white")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        self.name_label = ctk.CTkLabel(master=login_frame, text="Name", font=("Arial", 14, "bold"), text_color="white")
        self.name_label.grid(row=1, column=0, pady=(10, 5), sticky="w", padx=(70, 10))

        self.name_entry = ctk.CTkEntry(master=login_frame, width=300, fg_color="white", text_color="black")
        self.name_entry.grid(row=1, column=1, pady=(10, 5), padx=(10, 70))

        self.password_label = ctk.CTkLabel(master=login_frame, text="Password", font=("Arial", 14, "bold"), text_color="white")
        self.password_label.grid(row=2, column=0, pady=(10, 5), sticky="w", padx=(70, 10))

        self.password_entry = ctk.CTkEntry(master=login_frame, width=300, fg_color="white", text_color="black", show="*")
        self.password_entry.grid(row=2, column=1, pady=(10, 5), padx=(10, 70))

        self.login_button = ctk.CTkButton(master=login_frame, text="Log in", fg_color="#1E2D3A", hover_color="#415A77", command=self.login)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=(30, 15))  # Increased pady for the login button

        self.register_label = ctk.CTkLabel(master=login_frame, text="CLICK HERE TO REGISTER", font=("Arial", 11), text_color="white")
        self.register_label.grid(row=4, column=0, columnspan=2, pady=(15, 20))  # Increased pady for the register label

    def login(self):
        username = self.name_entry.get()
        password = self.password_entry.get()

        if username in self.users and self.users[username] == password:
            messagebox.showinfo("Login Successful", "Welcome to BorrowEase Dashboard!")
        else:
            messagebox.showerror("Login Error", "Invalid username or password. Please try again.")

    def open_dashboard(self):
        self.root.destroy()  # Close the login window
        dashboard_root = ctk.CTk()
        dashboard_root.mainloop()

# Example usage
if __name__ == "__main__":
    root = ctk.CTk()
    app = LoginWindow(root)
    root.mainloop()
