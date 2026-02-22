import tkinter as tk
from tkinter import filedialog, messagebox
import pyautogui
import time
import threading

class BanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ban Script")

        self.usernames = []

        self.load_button = tk.Button(root, text="Upload file", command=self.load_file)
        self.load_button.pack(pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_ban)
        self.start_button.pack(pady=10)

        self.status_label = tk.Label(root, text="File not uploaded")
        self.status_label.pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                self.usernames = [line.strip() for line in f if line.strip()]
            self.status_label.config(text=f"Nicknames uploaded: {len(self.usernames)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def start_ban(self):
        if not self.usernames:
            messagebox.showwarning("Attention", "You need to upload file first")
            return

        thread = threading.Thread(target=self.ban_process)
        thread.start()

    def ban_process(self):
        self.status_label.config(text="Waiting 3 seconds...")
        time.sleep(3)

        for username in self.usernames:
            command = f"/ban {username}"
            pyautogui.write(command)
            pyautogui.press("enter")
            time.sleep(0.3)  # небольшая задержка между банами

        self.status_label.config(text="Done!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BanApp(root)

    root.mainloop()
