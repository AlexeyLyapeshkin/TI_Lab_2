from lfsr11 import DeCipher,Cipher
import tkinter
import PIL.Image
import PIL.ImageTk
import numpy

text1 = 'Биты исходного( или зашифрованного ) файла, 15 байт: '
text2 = 'Биты ключа, 15 байт: '
text3 = 'Биты шифрофайла( или расшифрованного ), 15 байт: '
text4 = 'Начальное состояние регистра (29 символов), 15 байт: '

def OutInf(window,btn1, img):


    def bytes_(filename):

        def bytes_from_file(filename, chunksize=8192):
            with open(filename, "rb") as f:
                while True:
                    chunk = f.read(chunksize)
                    if chunk:
                        for b in chunk:
                            yield b
                    else:
                        break

        b_arr = bytearray()
        for b in bytes_from_file(filename):
            b_arr.append(b)

        return b_arr


    def ReadFile(mode,reg,tx1,tx2,tx3):
        from tkinter import messagebox as kek

        def isBinary(reg):
            lol = reg.get()
            print(lol)
            for i in lol:
                if i in [2,10]:
                    print(i)
                    return False
                else:
                    return True

        print(isBinary(reg))
        tx1.delete('1.0', tkinter.END)
        tx2.delete('1.0', tkinter.END)
        tx3.delete('1.0', tkinter.END)

        from tkinter.filedialog import askopenfilename
        filename = askopenfilename()
        if mode == 'c':

            if len(reg.get()) == 29 and reg.get().isdigit() and isBinary(reg):
                reg = int(reg.get(),2)
                key = Cipher(filename,reg)

                #key bits
                tx2.insert(tkinter.END,''.join(format(x, '08b') for x in key[0:16]))


                #file bits
                bits = bytes_(filename)
                tx1.insert(tkinter.END,''.join(format(x, '08b') for x in bits[0:16]))

                bits = bytes_(filename+'.cph')
                tx3.insert(tkinter.END,''.join(format(x, '08b') for x in bits[0:16]))

            else:
                kek.showerror('Ошибочка.','С Вашим регистром что-то не так...')

        if mode == 'd':
            if len(reg.get()) == 29 and reg.get().isdigit() and isBinary(reg):
                reg = int(reg.get(),2)
                key = DeCipher(filename,reg)

                #key bits
                tx2.insert(tkinter.END,''.join(format(x, '08b') for x in key[0:16]))


                #file bits
                bits = bytes_(filename)
                tx1.insert(tkinter.END,''.join(format(x, '08b') for x in bits[0:16]))

                filename = filename[:(len(filename) - 4)]
                bits = bytes_(filename)
                tx3.insert(tkinter.END,''.join(format(x, '08b') for x in bits[0:16]))
            else:
                kek.showerror('Ошибочка.', 'С Вашим регистром что-то не так...')

        return filename

    #hide button
    btn1.place_forget()
    img.place_forget()

    #lbls

    label_01 = tkinter.Label(window, text=text4)
    label_01.place(relx=.1, y=50)

    label_1 = tkinter.Label(window,text=text1)
    label_1.place(x=100,y=100)

    label_2 = tkinter.Label(window,text=text2)
    label_2.place(x=100,y=250)

    label_3 = tkinter.Label(window,text=text3)
    label_3.place(x=100,y=400)

    label_count = tkinter.Label(window, text='Empty')
    label_count.place(relx=.6,rely=0.1)

    #text
    tk_text_1 = tkinter.Text(width = 105,height = 5)
    tk_text_1.place(relx=.03,y=140)
    #tk_text_1.insert(tkinter.END,'kek')
    tk_text_2 = tkinter.Text(width = 105,height = 5)
    tk_text_2.place(relx=.03,y=290)

    tk_text_3 = tkinter.Text(width=105, height = 5)
    tk_text_3.place(relx=.03, y=440)

    #entrys
    initial_reg = tkinter.StringVar()
    polynom = tkinter.StringVar()

    initial_entry = tkinter.Entry(textvariable = initial_reg)
    initial_entry.place(relx=.1,rely=.13,width=512)

    def update_():
        if initial_entry.get() != '':
            label_count['text'] = str(len(initial_entry.get()))

    #buttons
    c_button = tkinter.Button(window,width=20,text='Lets Chiphre!', bg='Dodger Blue', fg='White', command= (lambda  : ReadFile('c',initial_entry,tk_text_1,tk_text_2,tk_text_3)))
    c_button.place(relx=.7,rely=0.13)

    dc_button = tkinter.Button(window, width=20, text='Lets Dechiphre!', bg='Dodger Blue', fg='White', command=(lambda: ReadFile('d',initial_entry,tk_text_1,tk_text_2,tk_text_3)))
    dc_button.place(relx=.7, rely=0.18)

    check_button = tkinter.Button(window, width=10, text='Check length', bg='Dodger Blue', fg='White',
                        command=(lambda: update_()))
    check_button.place(relx=.85, rely=0.13)

    #Hide(window)

    Main_Window.update()



def MakeStartWindow(window):

    Button_Main = tkinter.Button(window, text='Lets chiphre!', bg='Dodger Blue', fg='White', width=30, height=2,
                                 command=(lambda: OutInf(window,Button_Main, label)))
    Button_Main.place(x=350, y=300)

    path = "img/kek2.png"
    im = PIL.Image.open(path)
    photo = PIL.ImageTk.PhotoImage(im)
    label = tkinter.Label(Main_Window, image=photo, width=600, height=300)
    label.image = photo  # keep a reference!
    label.place(x=180, y=0)

# start GUI
Main_Window = tkinter.Tk()
Main_Window.geometry('600x600')
Main_Window.title('Stream chiphers')

#make GUI
MakeStartWindow(Main_Window)

Main_Window.update_idletasks()
# end of prog
Main_Window.mainloop()
