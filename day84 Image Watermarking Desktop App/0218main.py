# TODO 產生GUI介面　利用Tkinter產生桌面應用程式，
# 可將照片增加浮水印(logo或文字)
# TODO Using what you have learnt about Tkinter
# , you will create a desktop application with
# a Graphical User Interface (GUI) where you can
# upload an image and use Python
# to add a watermark logo/text.
# TODO 1　產生頁面，標題浮水印產生器
# TODO 2 按鈕１：選擇照片用按鈕，可在視窗顯示選擇的照片，並且選擇後所執行的編輯的照片為複製照片
#  按鈕２：跳出可編輯或上傳logo的視窗　
#  按鈕3：在編輯視窗中按下確定
# TODO 3　按鈕3按下確定後變為預設觀看的圖
# TODO 4 用選擇或輸入欄位調整浮水印的角度或透明度
# TODO 5 儲存圖片，並可選擇位置
# TODO 6 可選擇在照片上壓入時間戳記，並餘右下角壓入時間
# TODO 7 按鈕4: 儲存加入浮水印的照片

import math
import os
#這使所有關於tkinter module的 class不需要特別寫成 tkinter.Label() 可直接寫成Label()
#---------CONSTANT-----------------------------------------------------------------------------------------------------------
#匯入module和class
from tkinter import *  # 從tkinter匯入 所有的class
from tkinter import filedialog

# Image 匯圖檔
# ImageColor module圖檔顏色
# ImageDraw 繪製圖案，在圖片中加入文字圖案，需要用這個模組
# ImageFont 變更字型
from PIL import Image, ImageColor, ImageDraw, ImageFont, ImageTk

photofile = "no photofile"

#---------Window-----------------------------------------------------------------------------------------------------------
window = Tk()  # 產生新的視窗
window.title("浮水印產生器")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20) #.config()用於產生物件後調整參數，例: 用config(padx= , pady= )調整按鈕離視窗(20 pixel)的距離

#---------第1層畫面-----------------------------------------------------------------------------------------------------------

#顯示選項1.選照片 text顯示文字使用ljst()調整 參考: https://www.delftstack.com/zh-tw/howto/python/python-pad-string-with-spaces/
choicefilelabel = Label(text="STEP1. 選擇圖檔".ljust(14), font=("Arial", 24, 'bold'))# 標示按鈕功能
choicefilelabel.grid(row=0, column=0)#標示按鈕位置 choicefilelabel.grid(row=0, column=0)#標示按鈕位置
markoptionlabel = Label(text="STEP2. 編輯浮水印".ljust(8), font=("Arial", 24, 'bold'))
markoptionlabel.grid(row=1, column=0)
# 狀態顯示
status_label = Label(window, text="STATUS")
status_label.grid()


#---------CONSTANT-----------------------------------------------------------------------------------------------------------
baseImage = "None Photo　底圖檔案"
baseImage_filename = "None Photoname　底圖檔案名稱"
#window的path
fontsFolder = 'FONT_FOLDER'
Font = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)#Window系統路徑
# textImag = "None photo"
# Font = ImageFont.load_default() # 可以使用的預設字型

#mac的path
#path= os.path.dirname(__file__)+'/'#Unix 找不到自行路徑，參考 https://stackoverflow.com/a/72770643/19331681 設定路徑
#Font = ImageFont.truetype(path + "Arial.ttf",fontsize)


#---------FUNCTION-----------------------------------------------------------------------------------------------------------

def showphoto(root, filename):
    '''載入要增加浮水印的圖片，顯示的圖片複製圖片，可於操作視窗預覽'''
    global baseImage_filename #global 檔案名稱
    filelabel = Label(root, text=filename)
    filelabel.grid(row=2, column=1)
    baseImage_filename = os.path.basename(filename) #用於後續顯示底圖名稱
    photo = Image.open(filename) #TODO 因為這裡把baseImage 格式變成PhotoImage
    photo2 = ImageTk.PhotoImage(photo)#不複製圖片直接顯示開啟的圖檔，只是開啟圖檔不會覆蓋，但存檔時需存新檔
    print("type(photo): {}, photo: {}, \ntype(photo2): {}, photo2: {}" .format(type(photo), photo,type(photo2), photo2)) #確認檔案格式
    print("^^^^^^^^上方為載入圖片---------------------------------------------------------")
    #  type(photo): <class 'PIL.PngImagePlugin.PngImageFile'>, photo: <PIL.PngImagePlugin.PngImageFile image mode=P size=225x225 at 0x7F9B55E949D0>, 
    #  type(photo2): <class 'PIL.ImageTk.PhotoImage'>, photo2: pyimage1
    imagelabel = Label(root, image=photo2) #
    imagelabel.grid(row=3, column=1) #設定預覽圖片顯示位置
    return photo,photo2 #回傳物件
    #  type(baseImge): <class 'tuple'> , photo2: pyimage1 , photo: <PIL.PngImagePlugin.PngImageFile image mode=P size=225x225 at 0x7F9B55E949D0> imagelabel = Label(root, image=photo2)

    # #------------------顯示的圖片為複製圖片
    # previewphoto = Image.open(filename)  # 載入圖片
    # previewphoto_copy = previewphoto.copy()  # 複製圖片
    # photo = ImageTk.PhotoImage(previewphoto_copy)
    # print("type(previewphoto): {}, previewphoto:{}, type(photo): {}, photo: {}"
    #       .format(type(previewphoto), previewphoto, type(photo), photo))
    # print("previewphoto_copy %s" % previewphoto_copy)
    #--------------------------多餘的code
    # previewphoto_new = Image.new('RGBA', (100, 200), 'purple') #產生圖塊
    # previewphoto_new.show() #使用主機預設的圖片瀏覽器開啟
    # imagelabel.image = photo #標示圖片，於顯示的TK視窗顯示?



def openImage(filename):
    ''' 用PIL 的Image模組開啟檔案'''
    img = Image.open(filename)
    return img


def showsmallphoto(root, filename):
    '''在編輯視窗產生預覽用圖片，將圖片縮小，並放編輯視窗'''
    # img = (Image.open(filename)).thumbnail((10, 10)) #這樣不行 因為這會認為是open類別的方法
    Label(root, text=filename).grid(row=1, column=2)
    img = Image.open(filename)  # 產生物件
    img.thumbnail((400, 100)) #等比例縮小照片
    photo = ImageTk.PhotoImage(img)
    imagelabel = Label(root, image=photo)
    imagelabel.image = photo
    imagelabel.grid(row=0, column=2)



def loadphoto():
    '''lod and return photo filename'''
    file = filedialog.askopenfilename(
        title='Open a file',
        initialdir='Users\妻寶王',
        filetypes=(("png files", "*png"), ("jpg files", "*.jpg"), ("all files", "*.*"))
    )
    # file
    status_label["text"] ="Import %s to be baseimage" %(os.path.basename(file))
    print("Import %s" %(os.path.basename(file)))
    return file


# button1 選擇照片用按鈕
def button1_action():
    '''按鈕1用於選擇照片 觸發的按鈕 ?多餘的function 如果只是要顯示的話'''
    global baseImage  #定義為global
    # print(loadiningphoto)
    # baseImage = loadingphoto #本來以為無法存檔
    baseImage= showphoto(window, loadphoto())
    # print("file: %s and filename: %s" % (baseImage, os.path.basename(os.path.abspath(baseImage))))
    print('type(baseImge): %s'  % type(baseImage), ', photo: %s' % type(baseImage[0]), ', photo2: %s ' % type(baseImage[1]))#檢查格式　<class 'PIL.ImageTk.PhotoImage'>
    print("^^^^^^^^上方為定義baseImage---------------------------------------------------------")



#button2 
def editbutton_action():
    '''跳出編輯畫面，編輯畫面包含 1.輸入文字 2.匯入LOGO 3.透ß明度調整
     4.調整大小 5.旋轉浮水印 6.確認上傳編輯後浮水印 7.重複出現 8.出現間距'''
    setting_window = Toplevel()
    setting_window.title("調整介面")
    setting_window.minsize(width=700, height=500) #調整視窗大小
    # TODO 設定頁面的滾動條 步驟
    # Creaste A Main Frame
    main_frame = Frame(setting_window)
    main_frame.pack(fill=BOTH, expand=True)  # fill內容如何填充視窗 expand 為1或True 內容是否全部展開
    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    # Add A Scrollbar To The Canvas
    my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=BOTH)
    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas, padx=10, pady=10) #TODO 增加依據原件大小，自動變更視窗
    # Add that New frame To a Window In the Canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    

    def print_and_get():
        # text_for_watermark = entrytext.get() #用Enrtry()元件時獲得輸入內容
        text_for_watermark = entrytext.get("1.0", 'end') #用text()元件 https://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-widget
        transparency_rate = scale_used_transparency(scalbar_var.get())
        shrinkage_rate = spinbox_used()
        rotate_angle = scale_used_rotation(scalbar_var2.get())
        fontsize = int(30*shrinkage_rate)
        Font = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), fontsize)
        baseImageCovertRGBA = baseImage[0].convert('RGBA') #字體透明 https://blog.csdn.net/Dxy1239310216/article/details/121517053
        tex_overylay = Image.new('RGBA', baseImageCovertRGBA.size,(255,255,255,0))
        image_draw = ImageDraw.Draw(tex_overylay)
        textsize=image_draw.textbbox((0,0),text_for_watermark, font=Font)
        positions = listbox_used(listbox, textsize)
        if positions == (0,0):
            text_for_watermark =text_repeated_permutation(text_for_watermark, textsize, baseImage[0])

        print(f"text_for_watermark: ---\"{text_for_watermark}\"----,transparency_rate: ---\"{transparency_rate}\"---")
        print(f"shrinkage_rate: ---\"{shrinkage_rate}\"---,rotate_angle: ---\"{rotate_angle}\"---,positons: ---\"{positions}\"---")
       

        if baseImage != "None Photo":
            global textImg # 將修改後的圖變更為golobal，使得
            # baseImage[0].paste(entry_im) #單行text
            # image_draw.text(positions,text_for_watermark,font=Font, fill=(255,0,0,transparency_rate))
            image_draw.multiline_text(positions,text_for_watermark,font=Font, fill=(255,0,0,transparency_rate))
            tex_overylay = tex_overylay.rotate(rotate_angle)
            status_label["text"] ="Add watermark \"%s\" to %s..." % (text_for_watermark, baseImage_filename)
            textImg = Image.alpha_composite(baseImageCovertRGBA, tex_overylay) 
            print("show %s" %(textImg))
            textImg.show()
        else:
            print("None Photo")

         # showsmallphoto(second_frame, entry_im)#測試是否可以

 

    def logobutton_action():
        showsmallphoto(second_frame, loadphoto())  # 用另一個function
    #     這裡會跳異常 "_tkinter.TclError: image "pyimage1" doesn't exist" ， 因為在一個程式中只能存在一個根視窗，
    #     也就是說只能存在一個Tk()，其他的視窗只能以頂層視窗（Toplevel()）的形式存在。於是將qudian類下的Tk()改成Toplevel()後，問題完全解決。
    #     參考網址: https://www.itread01.com/content/1550112337.html

#---------設定配置-----------------------------------------------------------------------------------------------------------

    # 1.輸入文字
    entry_label = Label(second_frame, text="key in text for watermark")
    entry_label.grid(column=0, row=0)
    entrytext = Entry(second_frame, width=15)  # 這裡有輸入的介面
    entrytext.insert(INSERT, "key in Text")  # 可以輸入END和INSERT但不知道差別在哪
    entrytext.grid(column=0, row=1)



    # 2.匯入LOGO
    logollabel =Label(second_frame, text="Import Logo")
    logollabel.grid(column=1,row=0)
    logobutton = Button(second_frame, text="Import Logo", command=logobutton_action)
    logobutton.grid(column=1, row=1)
    # logobutton = Button(second_frame, text="Import Logo", command=logobutton_action).grid()
    # print(logobutton.get())

    # 3.透明度調整，控制方法用scale bar
    transparencylabel = Label(second_frame, text="Transparency")
    transparencylabel.grid(column=0, row=2)
    scalbar_var = DoubleVar()#設定scalbar_var的值 
    scalbar = Scale(second_frame, from_=0, to=100, orient="horizontal", troughcolor="skyblue",
    width="20", variable=scalbar_var)
    scalbar.grid(column=0, row=3)

    def scale_used_transparency(value):
        '''透明度換算，當數值為100時透明度為100％'''
        print('scale_used: ', value)
        transparency_rate = 255 - int(value)/100*255 #以百分比表示透明度
        return int(transparency_rate) #回傳選擇值


    # 4.調整大小，控制方法用spinbox，等比例縮小値
    shrinkagelabel = Label(second_frame, text="Size")
    shrinkagelabel.grid(column=1, row=2)
    # spinbox_var = StringVar() #建立 tk 變數
    # spinbox_var.set("")
    # spinbox_var = 0

    def spinbox_used():
        print("shrinkage_rate: %s" %(spinbox.get()))
        # spinbox_var.set(spinbox.get())
        spinbox_var = 1 + int(spinbox.get())/100
        return spinbox_var

    spinbox = Spinbox(second_frame, from_=0, to=100, increment=10, width=5, command=spinbox_used)
    spinbox.grid(column=1, row=3)

    
    # 5.旋轉角度調整，控制方法用scale bar
    Rotationlabel = Label(second_frame, text="Rotation")
    Rotationlabel.grid(column=0, row=4)
    # Called with current scale value.
    scalbar_var2 =DoubleVar()

    def scale_used_rotation(value):
        selection = "Rotation angle: "+ str(value) +"°"
        Rotationlabel.config(text=selection)
        print("shrinkage_rate: %s" %(value))
        return int(value)

    scalbar = Scale(second_frame, from_=0, to=360, orient="vertical", troughcolor="skyblue",
                    width="20", variable=scalbar_var2, command=scale_used_rotation)
    scalbar.grid(column=0, row=5)


    # 6.分佈位置，用list選項，出現在四角或重複出現
    Label(second_frame, text="Position").grid(column=1, row=4)

    
    # Listbox
    def listbox_used(event, textsize= (0,0,0,0)): 
        #預設textsize= (0,0,0,0)，沒預設會一直跳錯誤
        #Note here that Tkinter passes an event object to litbox_used()
        # Gets current selection from listbox
        water_mark_postion =listbox.get(listbox.curselection())
        W , H = baseImage[0].size
        w=int(textsize[2])
        h=int(textsize[3])
        print(water_mark_postion)
        if water_mark_postion =="Upper left":
            text_postion =  (10, 10) #預設空格(10,10)
        elif water_mark_postion =="Upper right":
            text_postion =  (int(W-w-10), 10) 
        elif water_mark_postion =="Lower left":
            text_postion =  (10, int(H-h-10)) 
        elif water_mark_postion =="Lower right":
            text_postion =  (int(W-w-10), int(H-h-10)) 
        elif water_mark_postion == "Center":
            text_postion =  ((W-w)/2,(H-h)/2)
        elif water_mark_postion == "Repeated permutation":
            text_postion =  (0, 0)
        # print(text_postion)
        return text_postion
        #print(listbox.get(listbox.curselection()))

    def text_repeated_permutation(text, texbbox_size, baseImage):
        '''使文字變成多行'''
        repeat = text
        width, high = int(texbbox_size[2]), int(texbbox_size[3])
        basimage_width, basimage_height = baseImage.size 
        count, consthigh = width, int(high)
        print(f'len(text), baseImage.size, consthigh {len(text), baseImage.size, consthigh}')
        #print(f'math.ceil(basimage_width/high){math.ceil(basimage_width/high)}')
        #for _ in range(math.ceil(basimage_width/high)):#換while
        while basimage_height/high > 0.5:
            if count < basimage_width+width*2:
                repeat = repeat + " " + text
                count+=width
                #count += len(text+" ")#單位不同，不能這樣算 len是位元數 圖是piexl，會出現換行次數不正確的問題
                #print(f"count, high{count, high}")
            else:
                repeat = repeat + "\n" + "\n" + text
                count = width
                high +=consthigh
                print(f"count, high{count, high}")
        text = repeat
        print(text)
        return text

    listbox = Listbox(second_frame, height=5, selectmode="browse", selectforeground="red")
    image_positon = ["Upper left", "Upper right", "Lower left", "Lower right","Center", "Repeated permutation"]
    for item in image_positon:
        listbox.insert(image_positon.index(item), item)
    listbox.bind("<<ListboxSelect>>", listbox_used)
    listbox.grid(column=1, row=5)

    # 7.確認
    def confirmbutton():
        '''按下按鈕後paste浮水印到base_photo'''
        pass
        # photo_for_modif.text((20,150),str(text_for_watermark), fill='gray')
        # # confirm(photofile, transparent=scale_used(), size=spinbox_used(), rotate=radio_used())
        # print("check")

    edit_finish_button = Button(second_frame, text="DONE", command=print_and_get, width=10, height=2)  # 注意command的function都不能有()，會變成布須觸發就執行
    edit_finish_button.grid(row=5, column=2)

#savebutton
def saveImage():
    print(textImg)
    file_name =  os.path.basename(baseImage_filename)
    print(file_name)
    file_path = os.path.expanduser("~/Desktop/") + "watermark_"+ file_name 
    textImg.save(file_path) #PIL 儲存照片的語法是 物件.save(儲存的路徑/名稱str格式)

openImagebutton = Button(text="瀏覽", command=button1_action, width=5, font=('Arial', 12 ,"bold"))
openImagebutton.grid(row=0, column=1) #選擇檔案按鈕

editImagebutton = Button(text='設定', command=editbutton_action, width=5, font=('Arial', 12 ,"bold"))
editImagebutton.grid(row=1, column=1) #跳出編輯選項按鈕

saveImagebutton = Button(text='SAVE',command=saveImage, font=('Aril', 12 ,"bold"))
saveImagebutton.grid(row=0, column=2)
#TODO新增SAVE按鈕測試存檔後圖示，測試到底為什麼浮水印字體為什麼不能調整透明度

window.mainloop()  # 維持視窗不關，


#---其他嘗試的code---------------------------------------------------------------------------
# print(editwindow)
# return editwindow
# editwindow.mainloop() 不用維持? 不知道為什麼

#本來預計用來做確認的method
    # def confirm(file, **kwargs):
    #     print(file)
    #     photo = Image.open(file)
    #     editlogo = photo.copy()
    #     width, height = editlogo.size
    #     rewidth = int(round(width * kwargs.get("size") * 0.1))
    #     rehight = int(round(height * float(kwargs.get("size") * 0.1)))
    #     print(f"這個是width{width}")
    #     # file.putalpha(kwargs["transparent"]) 方法為字典類型，想像kwargs字典key，會帶出的值
    #     # 參考 https://www.udemy.com/course/100-days-of-code/learn/lecture/20804136#notes
    #     newimage = editlogo \
    #         .putalpha(int(round(kwargs.get("transparent")))) \
    #         .resize((rewidth, rehight)) \
    #         .rotate(int(kwargs.get("rotate"))).save('editlogo.png')
    #     Image.open('editlogo.png')
    #     showsmallphoto(second_frame, newimage)
    #     print("have photo")

    # #     ❶ >> > width, height = catIm.size
    # #     ❷ >> > quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
    # #     >> > quartersizedIm.save('quartersized.png')
    # #
    # # ❸ >> > svelteIm = catIm.resize((width, height + 300))
    # # >> > svelteIm.save('svelte.png')

        # 本來用來獲得數值 Called with current scale value.
    # def scale_used(value):
    #     # modifphoto.putalpha((int(value) / 255) * 255)
    #     print('scale_used: ', value)
    #     transparency_rate = round(int(value)/100,2) #以百分比表示透明度
    #     alphavalue = math.ceil(transparency_rate * 255) #無條件去除小數點進位
    #     print(transparency_rate, "-" ,alphavalue)
    #     return alphavalue #回傳選擇值
    # # 5.旋轉，控制方法用radio，可以選擇傾斜15、30、45度 改成scale_bar
    # Label(second_frame, text="Rotation").grid(column=0, row=4)
    # def radio_used():
    #     print(radio_state.get())
    #     return (radio_state.get())
    #     # print(value)
    # # Variable to hold on to which radio button value is checked.
    # radio_state = IntVar()
    # radio_state.set(0)
    # for degree in (range(15, 96, 15)):
    #     Radiobutton(second_frame, text=str(f"{degree}°"), value=degree, variable=radio_state, command=radio_used).grid()
        # ------------不知道要幹嘛-------------
    # global photofile
    # print(photofile)
    # photofile = filename
    # print(photofile)
    # return photofile
       #W, H = baseImageCovertRGBA.size
        # print(textsize)
        # w=textsize[2]
        # h=textsize[3]
        # print(w,h)
        
        # if positions =="Repeated permutation":
        #     text_for_watermark = "ABC"
            #  u"""\
            #     ALWAYS BE HAPPY
            #     (LAUGHING IS THE \n BEST MEDICINE)"""
            # print(text_repeated_permutation(text = text_for_watermark, 
            # texbbox_size=textsize,baseImage=baseImageCovertRGBA))
            # print(type(text_for_watermark))

            # repeat_text = text_for_watermark
            # for _ in range(int(textsize[3])//int(baseImageCovertRGBA.size[1])):
            #     textsize=image_draw.textbbox((0,0),text_for_watermark, font=Font)
            #     if int(textsize[2]) < baseImageCovertRGBA[1]:
            #         repeat_text += " "+ text_for_watermark
            #     else:
            #         repeat_text += "\n" + text_for_watermark
            # text_for_watermark = repeat_text

