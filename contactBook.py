import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Set the DISPLAY environment variable
os.environ['DISPLAY'] = ':0'

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.configure(bg='black')  # Set background color to black


        # Add a new attribute to store the selected contact
        self.selected_contact = None

        self.contacts = []

        # Create GUI setup
        self.name_label = tk.Label(root, text="Name:", bg='black', fg='white')  # Set label color to white
        self.name_entry = tk.Entry(root, width=20)  # Adjust width for better appearance

        self.phone_label = tk.Label(root, text="Phone:", bg='black', fg='white')
        self.phone_entry = tk.Entry(root)

        self.email_label = tk.Label(root, text="Email:", bg='black', fg='white')
        self.email_entry = tk.Entry(root)

        #Add address_entry
        self.address_label = tk.Label(root, text="Address:", bg='black', fg='white')
        self.address_entry = tk.Entry(root)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact, bg='green', fg='white')  # Set button color to green

        # Grid layout setup
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Create a display frame
        self.display_frame = tk.Frame(root, bg='black')
        self.display_frame.grid(row=0, column=2, rowspan=5, columnspan=3, padx=10, pady=5, sticky='nsew')

        # widget for displaying contacts
        self.tree = ttk.Treeview(self.display_frame, columns=("Name", "Phone", "Email", "Address"), show='headings', height=10)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")

        self.tree.column("Name", width=100)
        self.tree.column("Phone", width=100)
        self.tree.column("Email", width=100)
        self.tree.column("Address", width=150)

        self.tree.pack(expand=True, fill='both')

        # Buttons frame
        self.buttons_frame = tk.Frame(root, bg='black')
        self.buttons_frame.grid(row=5, column=2, columnspan=3, pady=5, sticky='nsew')

        # Buttons under the display frame
        self.view_button = tk.Button(self.buttons_frame, text="View Contacts", command=self.view_contacts, bg='green', fg='white')
        self.update_button = tk.Button(self.buttons_frame, text="Update Contact", command=self.update_contact, bg='green', fg='white')
        self.delete_button = tk.Button(self.buttons_frame, text="Delete Contact", command=self.delete_contact, bg='green', fg='white')

        self.view_button.grid(row=0, column=0, padx=5, pady=5)
        self.update_button.grid(row=0, column=1, padx=5, pady=5)
        self.delete_button.grid(row=0, column=2, padx=5, pady=5)

        # Search entry and button
        self.search_entry = tk.Entry(root, width=65)
        self.search_button = tk.Button(root, text="Search", command=self.search_contact, bg='green', fg='white', width=7)  # Set width to 7
        self.search_entry.grid(row=8, column=2, pady=5, padx=(0, 10), sticky='w')
        self.search_button.grid(row=8, column=2, pady=5, padx=(140, 10), sticky='e')  # Adjusted row to 8


    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and phone number are required fields.")


    def view_contacts(self):
        self.update_treeview()
        if self.contacts:
            self.root.lift()
        else:
            messagebox.showinfo("Contact List", "No contacts available.")

    def search_contact(self):
        search_term = self.search_entry.get()
        if search_term:
            results = [contact for contact in self.contacts if
                       search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']]
            self.update_treeview(results)
            if not results:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showinfo("Search Results", "Please enter a search term.")

    def update_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = selected_item[0]
            contact_info = self.tree.item(item, 'values')
            self.selected_contact = {
                "Name": contact_info[0],
                "Phone": contact_info[1],
                "Email": contact_info[2],
                "Address": contact_info[3]
            }
            self.open_update_dialog(self.selected_contact)

    def delete_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = selected_item[0]
            contact_info = self.tree.item(item, 'values')
            selected_contact = {
                "Name": contact_info[0],
                "Phone": contact_info[1],
                "Email": contact_info[2],
                "Address": contact_info[3]
            }

            # Ask for confirmation before deleting
            confirmation = messagebox.askyesno("Delete Contact", f"Do you want to delete {selected_contact['Name']}?")

            if confirmation:
                self.contacts.remove(selected_contact)
                self.update_treeview()
                messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showinfo("Delete Contact", "Please select a contact to delete.")

    def open_update_dialog(self, contact):
        # Open a dialog box for updating the contact
        update_dialog = tk.Toplevel(self.root)
        update_dialog.title("Update Contact")

        name_label = tk.Label(update_dialog, text="Name:")
        name_entry = tk.Entry(update_dialog, width=20)
        name_entry.insert(0, contact["Name"])

        phone_label = tk.Label(update_dialog, text="Phone:")
        phone_entry = tk.Entry(update_dialog)
        phone_entry.insert(0, contact["Phone"])

        email_label = tk.Label(update_dialog, text="Email:")
        email_entry = tk.Entry(update_dialog)
        email_entry.insert(0, contact.get("Email", ""))

        address_label = tk.Label(update_dialog, text="Address:")
        address_entry = tk.Entry(update_dialog)
        address_entry.insert(0, contact.get("Address", ""))

        update_button = tk.Button(update_dialog, text="Update", command=lambda: self.update_contact_info(
            name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get(), update_dialog
        ))

        name_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        phone_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        phone_entry.grid(row=1, column=1, padx=10, pady=5)

        email_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        email_entry.grid(row=2, column=1, padx=10, pady=5)

        address_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        address_entry.grid(row=3, column=1, padx=10, pady=5)

        update_button.grid(row=4, column=0, columnspan=2, pady=10)

    def update_contact_info(self, name, phone, email, address, update_dialog):
        # Update contact information in the dialog box
        updated_contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        update_dialog.destroy()  # Close the dialog box
        self.contacts.remove(self.selected_contact)  # Remove the old contact
        self.contacts.append(updated_contact)  # Add the updated contact
        self.update_treeview()  # Update the Treeview with the modified contact


    def select_contact(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item = selected_item[0]
            contact_info = self.tree.item(item, 'values')
            self.selected_contact = {
                "Name": contact_info[0],
                "Phone": contact_info[1],
                "Email": contact_info[2],
                "Address": contact_info[3]
            }

    def clear_entries(self):
     # Clear all entry fields
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


    def update_treeview(self, contacts=None):
      # Update Treeview with the latest contacts
        self.tree.delete(*self.tree.get_children())
        contacts = contacts or self.contacts
        for contact in contacts:
            self.tree.insert("", "end", values=(contact["Name"], contact["Phone"], contact["Email"], contact["Address"]))


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
