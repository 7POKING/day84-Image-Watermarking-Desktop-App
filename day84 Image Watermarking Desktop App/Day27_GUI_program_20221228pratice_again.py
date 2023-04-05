from tkinter import * #從tkinter匯入 所有的class
#這使所有關於tkinter module的 class不需要特別寫成 tkinter.Label() 可直接寫成Label()
window = Tk()  # 產生新的視窗
window.title("浮水印產生器")
# window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

#tkinter module 中的 Label class
my_label = Label(text="I am a label", font=("Arial", 20, "bold"))
# my_label.pack()　#原建pack(), place(), grid()
my_label.grid(row=0, column=0)


#變更參數的方法
#方法1: kwarg字典變更
my_label["text"] = "New Text 方法1"
#方法2: 用config() method變更
my_label.config(text="New Text 方法2")

def button_clicked():
    #Challenge1 解答
    my_label.config(text="Button Got Clicked") #方法2
    my_label["text"] ="Button Got Clicked" #方法1
    # TODO Challenge2: 如何將輸入的文字置換掉Label
    #Challenge2 解答
    newtext =Input.get()
    my_label["text"]= newtext #方法1
    my_label.config(text=newtext) #方法2


    print("I got clicked \nI got entry %s" %(my_label["text"]))

#TODO Challenge1: Show "Button Got Clicked" on my_label when the button get's clicked
#tkinter module 中的 Button class
click_me =Button(text="click!", font=("Arial", 20, "bold"),
                 width=10, command=button_clicked) #輸入function name 不是 呼叫function
# click_me.pack()
click_me.grid(row=1, column=1)

new_button =Button(text="click!", font=("Arial", 20, "bold"),
                 width=10)
new_button.grid(row=0, column=2)


#tkinter module 中的 Entry class
Input = Entry(width=10)
# Input.pack()
print(Input.get()) # 用get() method獲得輸入文字 https://tcl.tk/man/tcl8.6/TkCmd/entry.htm#M45
Input.grid(row=2, column=3)

#TODO　測試２個視窗輸入值

# window2 = Tk()  # 產生新的視窗
# window2.title("測試視窗")
# window2.minsize(width=500, height=500)
# window2.config(padx=20, pady=20)

#TODO Cahllenge3: 使用grid()調整位置

#TODO **kwarg 練習









mainloop()