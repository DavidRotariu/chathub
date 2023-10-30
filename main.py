import tkinter as tk
import asyncio
import threading
from chat_app.chat_window import ChatWindow
from client.authentication import authenticate


def start_async_task():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(chat_app.chat_messages.connect_to_websocket_server_recv())


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Chat App")
    root.geometry("1050x550")
    root.configure(padx=20, pady=20)

    response_obj = authenticate()
    user_id = str(response_obj.get("id"))

    chat_app = ChatWindow(root, user_id)
    chat_app.create_widgets()

    thread = threading.Thread(target=start_async_task)
    thread.start()

    root.mainloop()
