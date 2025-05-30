import tkinter as tk

root=tk.Tk()
root.title("CALCULATOR")
root.geometry("400x500")

def click(event):
    button_text=event.widget.cget("text")
    if button_text=="=":
        try:
            result=eval(screen.get())
            screen.set(result)
        except:
            screen.set("ERROR")
    elif button_text=="CLEAR":
        screen.set("")
    else:
        screen.set(screen.get()+button_text)
        
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen,justify="right", bd=10, bg="white",font="Bold 24")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

buttons = [
    ["0","1","2","3"],
    ["4","5","6","7"],
    ["8","9","+","-"],
    ["*","/","CLEAR","="]
]
for row in buttons:
    frame = tk.Frame(root, bg="Gray")
    frame.pack(pady=5)

    for btn_text in row:
        button = tk.Button(
            frame, text=btn_text,
            font="Arial 20", width=5, height=2,
            fg="white", bg="black", activebackground="#666"
        )
        button.pack(side=tk.LEFT, padx=5)
        button.bind("<Button-1>", click)  

root.mainloop()
