import tkinter as tk
from datetime import datetime, timedelta
import argparse

class ClockApp:
    def __init__(self, root, target_time):
        self.root = root
        self.target_time = target_time
        self.root.title(f"Countdown to {self.target_time.strftime('%I:%M %p')}")
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
        next_target_time = self.get_next_target_time(now)
        remaining_time = next_target_time - now
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_string = f"{remaining_time.days * 24 + hours:02}:{minutes:02}:{seconds:02}"
        self.label.config(text=time_string)
        self.root.after(1000, self.update_clock)

    def get_next_target_time(self, now):
        next_target_time = now.replace(hour=self.target_time.hour, minute=self.target_time.minute, second=0, microsecond=0)
        if now > next_target_time:
            next_target_time += timedelta(days=1)
        return next_target_time

def parse_args():
    parser = argparse.ArgumentParser(description="Countdown Timer")
    parser.add_argument('hour', type=int, help='Hour of the target time (24-hour format)')
    parser.add_argument('minute', type=int, help='Minute of the target time')
    args = parser.parse_args()
    now = datetime.now()
    return datetime(now.year, now.month, now.day, args.hour, args.minute)

if __name__ == "__main__":
    target_time = parse_args()
    root = tk.Tk()
    app = ClockApp(root, target_time)
    root.mainloop()
