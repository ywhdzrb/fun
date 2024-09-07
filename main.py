from tkinter import *
import os
import core
import subprocess as sb

def exit():
    global win
    if os.path.exists(".\\temp\\api.exe"):
        os.system("ren .\\temp\\api.exe api.dll")
        win.destroy()
    else:
        win.destroy()
    

def downloadapi():
    global win2
    os.system("powershell curl -o .\\temp\\api.dll https://act-api-takumi.mihoyo.com/event/download_porter/link/hkrpg_cn/official/pc_default")
    core.game()
    win2.destroy()

# 警告
def warning():
    global win2
    win2 = Tk()
    win2.title("api未下载")
    win2.geometry("250x125")
    Label(win2, text="是否下载api").pack()
    Button(win2, text="下载", command=downloadapi).pack(side="left")
    Button(win2, text="取消", command=win2.destroy).pack(side="right")
    win2.mainloop()

def ifapi():
    if not os.path.exists(".\\temp"):
        os.system("md temp")
    if os.path.exists(".\\temp\\api.dll"):
        core.game()
        os.system("ren .\\temp\\api.dll api.exe")
        os.system(".\\temp\\api.exe")
    else:
        warning()



win = Tk()
win.title("好玩的")
win.geometry("250x125")

Label(win, text="是否启动“好玩的”").pack()
Button(win, text="启动", command=ifapi).pack(side="left")
Button(win, text="退出", command=exit).pack(side="right")
Button(win, text="设置", )

win.mainloop()
