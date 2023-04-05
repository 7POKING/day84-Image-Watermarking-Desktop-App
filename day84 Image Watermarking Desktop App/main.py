# TODO 產生GUI介面　利用Tkinter產生桌面應用程式，
# 可將照片增加浮水印(logo或文字)
# TODO Using what you have learnt about Tkinter
# , you will create a desktop application with
# a Graphical User Interface (GUI) where you can
# upload an image and use Python
# to add a watermark logo/text.
# TODO 1　產生頁面，標題浮水印產生器
# TODO 2 按鈕１　選擇照片用按鈕　按鈕２跳出可編輯或上傳logo的視窗
# 按鈕3 在編輯視窗中按下確定
# TODO 3　按鈕3按下確定後變為預設觀看的圖
# TODO 4 用選擇或輸入欄位調整浮水印的角度或透明度
# TODO 5 儲存圖片，並可選擇位置


import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
import math
photofile = "no photofile"

window = Tk()  # 產生新的視窗
window.title("浮水印產生器")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)


# 產生標示文字
# label = Label(text="選擇圖檔")
# label.grid(row=0, column=0)


def showphoto(root, filename):
    '''圖片預覽用'''
    Label(root, text=filename).grid(row=2, column=1)
    photo = ImageTk.PhotoImage(Image.open(filename))
    imagelabel = Label(root, image=photo)
    imagelabel.image = photo
    imagelabel.grid(row=3, column=1)


def openImage(filename):
    img = Image.open(filename)
    return img


def showsmallphoto(root, filename):
    '''在編輯視窗產生預覽用圖片，將圖片縮小，並放編輯視窗'''
    global photofile
    print(photofile)
    Label(root, text=filename).grid()
    photofile = filename
    print(photofile)
    # img = (Image.open(filename)).thumbnail((10, 10)) #這樣不行 因為這會認為時open類別的方法
    img = Image.open(filename)  # 產生物件
    img.thumbnail((400, 100))
    img.save("test_thumbnail.jpg")
    photo = ImageTk.PhotoImage(Image.open("test_thumbnail.jpg"))
    imagelabel = Label(root, image=photo)
    imagelabel.image = photo
    imagelabel.grid(row=0, column=1)
    return photofile


def loadphoto():
    '''lod and return photo filename'''
    file = filedialog.askopenfilename(
        title='Open a file',
        initialdir='Users\妻寶王',
        filetypes=(("jpg files", "*.jpg"), ("png files", "*png"), ("all files", "*.*"))
    )
    # print(filename)
    return file


# button1 選擇照片用按鈕
def button1_action():
    '''按鈕1用於選擇照片'''
    showphoto(window, loadphoto())
    # print(loadphoto())


def editbutton_action():
    '''跳出編輯畫面，編輯畫面包含 1.輸入文字 2.匯入LOGO 3.透明度調整
     4.調整大小 5.旋轉浮水印 6.確認上傳編輯後浮水印 7.重複出現 8.出現間距'''
    editwindow = Toplevel()
    editwindow.title("調整介面")
    editwindow.minsize(width=10, height=10)
    # TODO 設定頁面的滾動條 步驟
    # Creaste A Main Frame
    main_frame = Frame(editwindow)
    main_frame.pack(fill=BOTH, expand=1)  # fill內容如何填充視窗 expand 為1或True 內容是否全部展開
    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    # Add A Scrollbar To The Canvas
    my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas)
    # Add that New frame To a Window In the Canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    # 1.輸入文字
    Label(second_frame, text="Text for watermark").grid()
    entrytext = Entry(second_frame, width=10)  # 這裡有輸入的介面
    entrytext.insert(END, "key in Text")  # 可以輸入END和INSERT但不知道差別在哪
    entrytext.grid()

    def logobutton_action():
        showsmallphoto(second_frame, loadphoto())  # 用另一個function
        # 這裡會跳異常 "_tkinter.TclError: image "pyimage1" doesn't exist" ， 因為在一個程式中只能存在一個根視窗，也就是說只能存在一個Tk()，其他的視窗只能以頂層視窗（Toplevel()）的形式存在。於是將qudian類下的Tk()改成Toplevel()後，問題完全解決。
        # 參考網址: https://www.itread01.com/content/1550112337.html

    # 2.匯入LOGO
    Label(second_frame, text="Import Logo").grid()
    logobutton = Button(second_frame, text="Import Logo", command=logobutton_action).grid()
    # print(logobutton.get())

    # 3.透明度調整，控制方法用scale bar
    Label(second_frame, text="Transparency").grid()

    # Called with current scale value.
    def scale_used():
        # modifphoto.putalpha((int(value) / 255) * 255)
        alphavalue = (int(scalbar.get()) / 255) * 255
        print(alphavalue)
        return alphavalue

    scalbar = Scale(second_frame, from_=0, to=100, command=scale_used, orient="horizontal", troughcolor="green",
                    width="20")
    scalbar.grid(column=1)

    # 4.調整大小，控制方法用輸入値，輸入等比例縮小値
    Label(second_frame, text="Size").grid()

    def spinbox_used():
        print(spinbox.get())
        return spinbox.get()
        # print(value)

    spinbox = Spinbox(second_frame, from_=0, to=100, increment=10, width=5, command=spinbox_used)
    spinbox.grid()

    # 5.旋轉，控制方法用radio，可以選擇傾斜15、30、45度
    Label(second_frame, text="Rotation").grid()

    def radio_used():
        print(radio_state.get())
        return (radio_state.get())
        # print(value)

    # Variable to hold on to which radio button value is checked.
    radio_state = IntVar()
    radio_state.set(0)
    for degree in (range(15, 46, 15)):
        Radiobutton(second_frame, text=str(f"{degree}°"), value=degree, variable=radio_state, command=radio_used).grid()

    # 6.分佈位置，用list選項，出現在四角或重複出現
    Label(second_frame, text="Position").grid()

    # Listbox
    def listbox_used(event):
        # Gets current selection from listbox
        print(listbox.get(listbox.curselection()))

    listbox = Listbox(second_frame, height=5, selectmode="browse", selectforeground="red")
    image_positon = ["Upper left", "Upper right", "Lower left", "Lower right", "Repeated permutation"]
    for item in image_positon:
        listbox.insert(image_positon.index(item), item)
    listbox.bind("<<ListboxSelect>>", listbox_used)
    listbox.grid()

    def confirm(file, **kwargs):
        print(file)
        photo = Image.open(file)
        editlogo = photo.copy()
        width, height = editlogo.size
        rewidth = int(round(width * kwargs.get("size") * 0.1))
        rehight = int(round(height * float(kwargs.get("size") * 0.1)))
        print(f"這個是width{width}")
        # file.putalpha(kwargs["transparent"]) 方法為字典類型，想像kwargs字典key，會帶出的值
        # 參考 https://www.udemy.com/course/100-days-of-code/learn/lecture/20804136#notes
        newimage = editlogo \
            .putalpha(int(round(kwargs.get("transparent")))) \
            .resize((rewidth, rehight)) \
            .rotate(int(kwargs.get("rotate"))).save('editlogo.png')
        Image.open('editlogo.png')
        showsmallphoto(second_frame, newimage)
        print("have photo")

    #     ❶ >> > width, height = catIm.size
    #     ❷ >> > quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
    #     >> > quartersizedIm.save('quartersized.png')
    #
    # ❸ >> > svelteIm = catIm.resize((width, height + 300))
    # >> > svelteIm.save('svelte.png')

    # 7.確認
    def confirmbutton():
        confirm(photofile, transparent=scale_used(), size=spinbox_used(), rotate=radio_used())
        print("check")

    edit_finish_button = Button(second_frame, text="DONE", command=confirmbutton)  # 注意command的function都不能有()，會變成布須觸發就執行
    edit_finish_button.grid()

    # print(editwindow)
    # return editwindow
    # editwindow.mainloop() 不用維持? 不知道為什麼


Button(text="選擇圖檔", command=button1_action).grid(row=0, column=1)

Button(text='編輯浮水印', command=editbutton_action).grid(row=1, column=1)

window.mainloop()  # 維持視窗不關，
