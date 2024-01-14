from tkinter import *
from tkinter import messagebox

class ContactApp:
    def __init__(self, myroot):
        self.myroot = myroot
        self.myroot.title("Contact Manager")
        self.contacts = []
        # Background to gui
        myroot.configure(bg="purple")

        # Labels
        Label(self.myroot, text="Name:", font=("Times new Roman", 12, "bold")).grid(row=0, column=0,padx=10, pady=5)
        Label(self.myroot, text="Phone:", font=("Times new Roman", 12, "bold")).grid(row=1, column=0, padx=10, pady=5)
        Label(self.myroot, text="Email:", font=("Times new Roman", 12, "bold")).grid(row=2, column=0, padx=10, pady=5)
        Label(self.myroot, text="Birth Date:", font=("Times new Roman", 12, "bold")).grid(row=3, column=0, padx=10, pady=5)

        # Entry fields
        self.name_entry = Entry(self.myroot, bd=5, font=("Times new Roman", 10))
        self.phone_entry = Entry(self.myroot, bd=5, font=("Times new Roman", 10))
        self.email_entry = Entry(self.myroot, bd=5, font=("Times new Roman", 10))
        self.birthdate_entry = Entry(self.myroot, bd=5, font=("Times new Roman", 10))

        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        self.birthdate_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        Button(self.myroot, text="Add Contact", command=self.add_contact, bg="red", fg="white", font=("Times new Roman", 15,"bold"), bd=6, padx=43, pady=10).grid(row=4, column=0,columnspan=2, pady=10)
        Button(self.myroot, text="Search Contact", command=self.search_contact, bg="blue", fg="white", font=("Times new Roman", 15,"bold"), bd=6, padx=30, pady=10).grid(row=5, column=0, columnspan=2, pady=10)
        Button(self.myroot, text="Update Contact", command=self.update_contact, bg="green", fg="white",font=("Times new Roman", 15,"bold"), bd=6, padx=30, pady=10).grid(row=6, column=0, columnspan=2, pady=10)
        Button(self.myroot, text="Delete Contact", command=self.delete_contact, bg="yellow", fg="black", font=("Times new Roman", 15,"bold"), bd=6, padx=33, pady=10).grid(row=7, column=0, columnspan=2, pady=10)

        # Listbox to display sorted contacts
        self.sorted_listbox = Listbox(self.myroot, font=("Times new Roman", 14), bg="white", fg="black", bd=10, relief=SUNKEN)
        self.sorted_listbox.grid(row=8, column=0, columnspan=3, pady=20)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        birthdate = self.birthdate_entry.get()

        if name and phone and email and birthdate:
            contact = {"Name": name, "Phone": phone, "Email": email, "Birthdate": birthdate}
            self.contacts.append(contact)
            self.contacts.sort(key=lambda x: x["Name"])  # Sort contacts by name
            self.update_sorted_listbox()
            self.clear_input_fields()
        else:
            self.show_message("Error", "Please enter valid name, phone, email, and birth date.")

    def search_contact(self):
        name = self.name_entry.get()

        for contact in self.contacts:
            if contact["Name"] == name:
                self.show_message("Contact Found", f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nBirth Date: {contact['Birthdate']}")
                return

        self.show_message("Contact Not Found", f"No contact found with the name {name}.")

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        birthdate = self.birthdate_entry.get()

        for contact in self.contacts:
            if contact["Name"] == name:
                contact["Phone"] = phone
                contact["Email"] = email
                contact["Birthdate"] = birthdate
                self.contacts.sort(key=lambda x: x["Name"])  # Re-sort contacts after update
                self.update_sorted_listbox()
                self.clear_input_fields()
                return

        self.show_message("Contact Not Found", f"No contact found with the name {name}.")

    def delete_contact(self):
        name = self.name_entry.get()

        for contact in self.contacts:
            if contact["Name"] == name:
                self.contacts.remove(contact)
                self.update_sorted_listbox()
                self.clear_input_fields()
                return

        self.show_message("Contact Not Found", f"No contact found with the name {name}.")

    def update_sorted_listbox(self):
        self.sorted_listbox.delete(0, END) 
        for contact in self.contacts:
            self.sorted_listbox.insert(END, contact["Name"])

    def clear_input_fields(self):
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.birthdate_entry.delete(0, END)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)


myroot = Tk()
app = ContactApp(myroot)
myroot.mainloop()