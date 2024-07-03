import customtkinter as ctk
from tkinter import Listbox, messagebox

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("BorrowEase Login")
        self.root.geometry("800x600")
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
            self.open_dashboard()
        else:
            messagebox.showerror("Login Error", "Invalid username or password. Please try again.")

    def open_dashboard(self):
        self.root.destroy()
        dashboard_root = ctk.CTk()
        dashboard_app = DashboardWindow(dashboard_root)
        dashboard_root.mainloop()

class DashboardWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("BorrowEase Dashboard")
        self.root.geometry("1000x800")
        self.root.configure(fg_color="#27374D")  # Background color

        # Left Menu Frame
        menu_frame = ctk.CTkFrame(root, width=200, height=600, corner_radius=0, fg_color="#1E2D3A")
        menu_frame.pack(side="left", fill="y")

        menu_items = [("Booklist", self.show_booklist), ("Books Borrowed", self.show_books_borrowed),
                      ("Books Returned", self.show_books_returned), ("Book Lost", self.show_book_lost)]
        for i, (text, command) in enumerate(menu_items):
            button = ctk.CTkButton(menu_frame, text=text, fg_color="#1E2D3A", hover_color="#415A77", command=command)
            button.pack(pady=20, padx=25, anchor="w")

        self.logout_button = ctk.CTkButton(menu_frame, text="LOGOUT", fg_color="#1E2D3A", hover_color="#415A77", command=self.logout)
        self.logout_button.pack(side="bottom", pady=20)

        # Main Content Frame
        self.main_frame = ctk.CTkFrame(root, width=800, height=600, corner_radius=0, fg_color="#2A3B4C")
        self.main_frame.pack(side="right", fill="both", expand=True)

        self.show_booklist()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_booklist(self):
        self.clear_frame()
        
        # Container frame for both sections
        container_frame = ctk.CTkFrame(self.main_frame, fg_color="#2A3B4C")
        container_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Insert Book Section
        insert_book_frame = ctk.CTkFrame(container_frame, width=400, height=300, corner_radius=10, fg_color="#354B5E")
        insert_book_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        insert_book_label = ctk.CTkLabel(insert_book_frame, text="INSERT BOOK", font=("Arial", 16, "bold"), text_color="white")
        insert_book_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        book_title_label = ctk.CTkLabel(insert_book_frame, text="Book Title:", font=("Arial", 12), text_color="white")
        book_title_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.book_title_entry = ctk.CTkEntry(insert_book_frame, width=200, fg_color="white", text_color="black")
        self.book_title_entry.grid(row=1, column=1, padx=10, pady=5)

        isbn_label = ctk.CTkLabel(insert_book_frame, text="ISBN:", font=("Arial", 12), text_color="white")
        isbn_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.isbn_entry = ctk.CTkEntry(insert_book_frame, width=200, fg_color="white", text_color="black")
        self.isbn_entry.grid(row=2, column=1, padx=10, pady=5)

        author_label = ctk.CTkLabel(insert_book_frame, text="Author:", font=("Arial", 12), text_color="white")
        author_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.author_entry = ctk.CTkEntry(insert_book_frame, width=200, fg_color="white", text_color="black")
        self.author_entry.grid(row=3, column=1, padx=10, pady=5)

        pub_date_label = ctk.CTkLabel(insert_book_frame, text="Published Date:", font=("Arial", 12), text_color="white")
        pub_date_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.pub_date_entry = ctk.CTkEntry(insert_book_frame, width=200, fg_color="white", text_color="black")
        self.pub_date_entry.grid(row=4, column=1, padx=10, pady=5)

        insert_button = ctk.CTkButton(insert_book_frame, text="Insert", fg_color="#1E2D3A", hover_color="#415A77", command=self.insert_book)
        insert_button.grid(row=5, column=1, pady=10)

        view_book_frame = ctk.CTkFrame(container_frame, width=400, height=300, corner_radius=10, fg_color="#354B5E")
        view_book_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        view_book_label = ctk.CTkLabel(view_book_frame, text="VIEW BOOK", font=("Arial", 16, "bold"), text_color="white")
        view_book_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Placeholder for book image
        self.book_image_label = ctk.CTkLabel(view_book_frame, text="", width=100, height=100, fg_color="white")
        self.book_image_label.grid(row=1, column=0, rowspan=6, padx=10, pady=10, sticky="n")

# Labels for book details
        book_label = ctk.CTkLabel(view_book_frame, text="Book:", font=("Arial", 12), text_color="white")
        book_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.book_detail_label = ctk.CTkLabel(view_book_frame, text="", font=("Arial", 12), text_color="white")
        self.book_detail_label.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        borrower_name_label = ctk.CTkLabel(view_book_frame, text="Borrower Name:", font=("Arial", 12), text_color="white")
        borrower_name_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.borrower_name_detail_label = ctk.CTkLabel(view_book_frame, text="", font=("Arial", 12), text_color="white")
        self.borrower_name_detail_label.grid(row=2, column=2, padx=10, pady=5, sticky="w")

        contact_number_label = ctk.CTkLabel(view_book_frame, text="Contact Number:", font=("Arial", 12), text_color="white")
        contact_number_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.contact_number_detail_label = ctk.CTkLabel(view_book_frame, text="", font=("Arial", 12), text_color="white")
        self.contact_number_detail_label.grid(row=3, column=2, padx=10, pady=5, sticky="w")

        email_label = ctk.CTkLabel(view_book_frame, text="Email:", font=("Arial", 12), text_color="white")
        email_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.email_detail_label = ctk.CTkLabel(view_book_frame, text="", font=("Arial", 12), text_color="white")
        self.email_detail_label.grid(row=4, column=2, padx=10, pady=5, sticky="w")

        date_label = ctk.CTkLabel(view_book_frame, text="Date:", font=("Arial", 12), text_color="white")
        date_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        self.date_detail_label = ctk.CTkLabel(view_book_frame, text="", font=("Arial", 12), text_color="white")
        self.date_detail_label.grid(row=5, column=2, padx=10, pady=5, sticky="w")

        time_label = ctk.CTkLabel(view_book_frame, text="Time:", font=("Arial", 12), text_color="white")
        time_label.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        self.time_detail_label = ctk.CTkLabel(view_book_frame, text="", font=("Arial", 12), text_color="white")
        self.time_detail_label.grid(row=6, column=2, padx=10, pady=5, sticky="w")

        # Add more widgets to populate the view book area...

        # Book List Section
        book_list_frame = ctk.CTkFrame(self.main_frame, width=800, height=300, corner_radius=10, fg_color="#354B5E")
        book_list_frame.pack(pady=20)

        book_list_label = ctk.CTkLabel(book_list_frame, text="BOOK LIST", font=("Arial", 16, "bold"), text_color="white")
        book_list_label.grid(row=0, column=0, padx=10, pady=10)

        # Using Tkinter Listbox
        self.book_listbox = Listbox(book_list_frame, width=115, height=15)
        self.book_listbox.grid(row=1, column=0, padx=10, pady=5, columnspan=4)

        borrow_button = ctk.CTkButton(book_list_frame, text="Borrow", fg_color="#1E2D3A", hover_color="#415A77", command=self.borrow_book)
        borrow_button.grid(row=2, column=0, padx=10, pady=10)

        edit_button = ctk.CTkButton(book_list_frame, text="Edit", fg_color="#1E2D3A", hover_color="#415A77", command=self.edit_book)
        edit_button.grid(row=2, column=1, padx=10, pady=10)

        delete_button = ctk.CTkButton(book_list_frame, text="Delete", fg_color="#1E2D3A", hover_color="#415A77", command=self.delete_book)
        delete_button.grid(row=2, column=2, padx=10, pady=10)

    def insert_book(self):
        title = self.book_title_entry.get()
        isbn = self.isbn_entry.get()
        author = self.author_entry.get()
        pub_date = self.pub_date_entry.get()

        if title and isbn and author and pub_date:
            book_info = f"Title: {title}, ISBN: {isbn}, Author: {author}, Published Date: {pub_date}"
            self.book_listbox.insert('end', book_info)

            # Clear the entries after insertion
            self.book_title_entry.delete(0, 'end')
            self.isbn_entry.delete(0, 'end')
            self.author_entry.delete(0, 'end')
            self.pub_date_entry.delete(0, 'end')
        else:
            messagebox.showerror("Error", "All fields must be filled")

    def borrow_book(self):
        # Add functionality to borrow book
        pass

    def edit_book(self):
        # Add functionality to edit book
        pass

    def delete_book(self):
        # Add functionality to delete book
        pass

    def show_books_borrowed(self):
        self.clear_frame()
        title = ctk.CTkLabel(self.main_frame, text="BOOKS BORROWED", font=("Arial", 24, "bold"), text_color="white")
        title.pack(pady=20)
        
        # Add more widgets to populate the books borrowed area...

    def show_books_returned(self):
        self.clear_frame()
        title = ctk.CTkLabel(self.main_frame, text="BOOKS RETURNED", font=("Arial", 24, "bold"), text_color="white")
        title.pack(pady=20)
        
        # Add more widgets to populate the books returned area...

    def show_book_lost(self):
        self.clear_frame()
        title = ctk.CTkLabel(self.main_frame, text="BOOK LOST", font=("Arial", 24, "bold"), text_color="white")
        title.pack(pady=20)
        
        # Add more widgets to populate the book lost area...

    def logout(self):
        self.root.destroy()
        login_root = ctk.CTk()
        login_app = LoginWindow(login_root)
        login_root.mainloop()

if __name__ == "__main__":
    root = ctk.CTk()
    app = LoginWindow(root)
    root.mainloop()