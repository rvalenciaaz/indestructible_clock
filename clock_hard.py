import tkinter as tk
from datetime import datetime, timedelta

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown to 8 AM")
        self.root.geometry("300x70")
        self.root.resizable(False, False)
        self.root.overrideredirect(True)  # Remove window decorations
        self.create_widgets()
        self.update_clock()

    def create_widgets(self):
        self.label = tk.Label(self.root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
        self.label.pack(anchor='center')

    def disable_event(self):
        pass  # Override the close event and do nothing

    def update_clock(self):
        now = datetime.now()
        next_8am = self.get_next_8am(now)
        remaining_time = next_8am - now
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_string = f"{remaining_time.days * 24 + hours:02}:{minutes:02}:{seconds:02}"
        self.label.config(text=time_string)
        self.root.after(1000, self.update_clock)

    @staticmethod
    def get_next_8am(now):
        next_8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
        if now.hour >= 8:
            next_8am += timedelta(days=1)
        return next_8am

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()
