import tkinter as tk
from threading import Thread
from main import listen
from commands import process_command
from speech import speak
import datetime
import psutil
import random


# ---------- Window ----------
root = tk.Tk()
root.title("JARVIS AI")
root.geometry("600x600")
root.configure(bg="#0a0f1c")

left_frame = tk.Frame(root, bg="#0a0f1c")
left_frame.pack(side="left", fill="both", expand=True)

center_frame = tk.Frame(root, bg="#0a0f1c")
center_frame.pack(side="left", fill="both", expand=True)

right_frame = tk.Frame(root, bg="#0a0f1c")
right_frame.pack(side="right", fill="both", expand=True)


# ---------- Canvas (Iron Man Core) ----------
canvas = tk.Canvas(center_frame, width=250, height=250, bg="#0a0f1c", highlightthickness=0)
canvas.pack(pady=20)

wave_canvas = tk.Canvas(center_frame, width=250, height=100, bg="#0a0f1c", highlightthickness=0)
wave_canvas.pack(pady=10)

angle = 0

def draw_arc():
    global angle
    canvas.delete("all")

    # Outer circle
    canvas.create_oval(20, 20, 230, 230, outline="#00ffff", width=2)

    # Rotating arc
    canvas.create_arc(20, 20, 230, 230,
                      start=angle,
                      extent=60,
                      style="arc",
                      outline="#00ffff",
                      width=4)

    angle = (angle + 5) % 360
    root.after(50, draw_arc)

draw_arc()

circle = canvas.create_oval(20, 20, 180, 180, outline="cyan", width=3)


def animate_circle():
    current = canvas.itemcget(circle, "outline")
    new_color = "cyan" if current == "#00ffff" else "#00ffff"
    canvas.itemconfig(circle, outline=new_color)
    root.after(500, animate_circle)


animate_circle()


# ---------- Title ----------
title = tk.Label(center_frame, text="JARVIS",fg="#00ffff", bg="#0a0f1c")
title.pack()


# ---------- Status ----------
status_label = tk.Label(left_frame, text="SYSTEM IDLE",
                        fg="white", bg="#0a0f1c")
status_label.pack(pady=5)



info_label = tk.Label(left_frame, text="", fg="#00ffff", bg="#0a0f1c")
info_label.pack(pady=5)

def draw_wave(level=10):
    wave_canvas.delete("all")

    bars = 20
    width = 250 // bars

    for i in range(bars):
        height = random.randint(5, level)
        x0 = i * width
        y0 = 50 - height
        x1 = x0 + width - 2
        y1 = 50 + height

        wave_canvas.create_rectangle(x0, y0, x1, y1, fill="#00ffff")

    root.after(100, draw_wave, level)


def update_system_info():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    cpu = psutil.cpu_percent()

    info_label.config(text=f"TIME: {now}   |   CPU: {cpu}%")
    root.after(1000, update_system_info)


update_system_info()

wave_label = tk.Label(root, text="▁▂▃▄▅▆▇", fg="#00ffff", bg="#0a0f1c")
wave_label.pack()

def animate_wave():
    patterns = ["▁▂▃▄▅▆▇", "▇▆▅▄▃▂▁"]
    current = wave_label.cget("text")
    wave_label.config(text=patterns[1] if current == patterns[0] else patterns[0])
    root.after(300, animate_wave)

animate_wave()


# ---------- Chat Window ----------
chat_box = tk.Text(right_frame, height=12, width=60,
                   bg="#111827", fg="#00ffff",
                   insertbackground="white")
chat_box.pack(pady=10)


def update_chat(sender, message):
    chat_box.insert(tk.END, f"{sender}: {message}\n")
    chat_box.see(tk.END)


# ---------- Voice Handling ----------
def handle_voice():
    status_label.config(text="LISTENING...")
    draw_wave(30)
    command = listen()

    if command:
        update_chat("YOU", command)

        status_label.config(text="PROCESSING...")
        response = process_command(command)

        update_chat("JARVIS", response)
        speak(response)

        status_label.config(text="SYSTEM IDLE")
    else:
        status_label.config(text="SYSTEM IDLE")

    draw_wave(10)   
    status_label.config(text="SYSTEM IDLE")


def start_voice():
    Thread(target=handle_voice).start()

def wake_word_listener():
    while True:
        command = listen()

        if command and "jarvis" in command.lower():
            status_label.config(text="Wake word detected")
            speak("Yes?")
            
            command = listen()
            if command:
                update_chat("You", command)

                status_label.config(text="Processing...")
                response = process_command(command)

                update_chat("Jarvis", response)
                speak(response)

                status_label.config(text="Idle")

# ---------- Buttons ----------
mic_btn = tk.Button(center_frame, text="🎤 ACTIVATE",
                    command=start_voice,
                    bg="#00ffff", fg="black",
                    font=("Arial", 12, "bold"),
                    width=20)
mic_btn.pack(pady=10)


exit_btn = tk.Button(root, text="SHUTDOWN",
                     command=root.quit,
                     bg="red", fg="white",
                     width=20)
exit_btn.pack(pady=10)



Thread(target=wake_word_listener, daemon=True).start()

root.mainloop()