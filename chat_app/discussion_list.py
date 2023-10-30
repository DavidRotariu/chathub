import tkinter as tk
from tkinter import ttk
import customtkinter

from chat_app.settings import USER_NAME
from client.contacts import get_contacts
from client.discussions import create_new_discussion, get_discussions


class DiscussionList(tk.Frame):
    def __init__(self, master=None, user_id=None):
        super().__init__(master)
        self.listbox_discussions = None
        self.button_discussions = None
        master.grid(row=0, column=0, sticky="ns")

        self.user_id = user_id
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text=f"Hello {USER_NAME}")
        label.pack()

        discussions = get_discussions(self.user_id)
        self.button_discussions = customtkinter.CTkButton(self, text="New Chat",
                                                          width=150,
                                                          height=55,
                                                          corner_radius=8,
                                                          fg_color="#5c8efc",
                                                          border_color="#4B73C9",
                                                          border_width=2,
                                                          hover_color="#4B73C9",
                                                          text_color="white",
                                                          font=("Helvetica", 18, "bold"),
                                                          command=self.contact_window)
        self.button_discussions.pack(fill=tk.X)

        self.listbox_discussions = ttk.Treeview(self, selectmode="browse")
        self.listbox_discussions.pack(fill=tk.BOTH, expand=True, pady=10, ipadx=20)
        self.listbox_discussions.heading("#0", text="Chats")

        for discussion in discussions:
            self.listbox_discussions.insert('', 'end', text=discussion["name"], value=discussion["id"])

    def contact_window(self):
        contact_popup = tk.Toplevel(self)
        contact_popup.title("Contacts")
        contact_popup.configure(height=300, width=500)
        contact_popup.geometry("280x400")
        contact_popup.transient(self)

        contacts_listbox = ttk.Treeview(contact_popup, selectmode="browse")
        contacts_listbox.heading("#0", text="Contacts:")
        contacts_listbox.pack(fill=tk.BOTH, expan=True, padx=30, pady=30)

        contacts = get_contacts()
        for contact in contacts:
            contacts_listbox.insert('', 'end', text=contact["name"], value=contact["id"])

        def add_selected_contact():
            selected_index = contacts_listbox.selection()[0]
            if selected_index:
                selected_item = contacts_listbox.selection()[0]
                selected_discussion = contacts_listbox.item(selected_item)

                selected_contact_id = str(selected_discussion["values"][0])
                text = selected_discussion["text"]

                discussion = create_new_discussion(self.user_id, selected_contact_id)
                if discussion:
                    self.listbox_discussions.insert('', 'end', text=text, values=(discussion["id"]))

                contact_popup.destroy()

        button_select = customtkinter.CTkButton(contact_popup, text="Submit",
                                                width=100,
                                                height=35,
                                                corner_radius=8,
                                                fg_color="#5c8efc",
                                                border_color="#4B73C9",
                                                border_width=2,
                                                hover_color="#4B73C9",
                                                text_color="white",
                                                font=("Helvetica", 18, "bold"),
                                                command=add_selected_contact)
        button_select.pack(fill=tk.X, padx=10, pady=10)