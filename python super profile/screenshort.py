import pyautogui
import time
import tkinter as tk

def screenshort():
    # time.sleep(5)
    name = time.time()
    name= f"C:/Users/HP/Desktop/E playlist/python super profile/screenshorts/{name}.png"
    img = pyautogui.screenshot()
    img.save(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame , text = "take screenshort", command = screenshort)
button.pack(side=tk.LEFT)

close= tk.Button(frame , text = "quit ", command = quit)
close.pack(side=tk.LEFT)

root.mainloop()
