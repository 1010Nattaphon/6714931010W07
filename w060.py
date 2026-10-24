import tkinter as tk
root = tk.Tk()
root.title("Hello World")
root.geometry("400x300")

tk.Label(root, text="9012071", font=("Arial", 16)).pack(side ="bottom")
tk.Label(root, text="Programming 2", font=("Arial", 16)).pack(side ="ledt")
tk.Label(root, text="Computer Science and onformation Technology", font=("Arial", 16)).pack(side ="rig")
tk.Label(root, text="CSTI", font=("Arial", 16)).pack(side = "bottom")

tk.Label(root, text="9012071", font=("Arial", 16)).grid(row=0, column=0)
tk.Label(root, text="Programming 2", font=("Arial", 16)).grid(row=0, column=1)
tk.Label(root, text="Computer Science and Information Technology", font=("Arial", 16)).grid(row=1, column=0)
tk.Label(root, text="CSTI", font=("Arial", 16)).grid(row=1, column=1)

root.mainloop()