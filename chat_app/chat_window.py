import tkinter as tk
from chat_app.chat_messages import ChatMessages
from chat_app.discussion_list import DiscussionList


class ChatWindow:
    def __init__(self, root=None, user_id=None):
        self.root = root
        self.discussion_list = None
        self.chat_messages = None
        self.user_id = user_id

    def create_widgets(self):
        discussion_frame = tk.Frame(self.root, bg="lightgray")
        self.discussion_list = DiscussionList(discussion_frame, self.user_id)
        self.discussion_list.pack(side="left", fill="both", expand=True)

        chat_frame = tk.Frame(self.root, bg="lightgray")

        self.chat_messages = ChatMessages(chat_frame, self.discussion_list)
        self.chat_messages.pack(side="right", fill="both", expand=True)

