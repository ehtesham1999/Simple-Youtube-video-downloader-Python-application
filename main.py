from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
file_size = 0

"""
url = "https://www.youtube.com/watch?v=KJBulnH454I"
path_to_save_video = "C:\\Users\\ehtesham\\Desktop\\DWM report"

ob = YouTube(url)
strm = ob.streams.all()

for i in strm:
    print(i)
    print()

print()
print(strm[0].title+" ")
print(int((ob.streams.get_highest_resolution().filesize/1000000)))
#ob.streams.get_lowest_resolution().download(path_to_save_video)
"""
def progress(stream =None,chunk = None,file_handle=None,remaining=0):
    file_downloaded = (file_size-remaining)
    per = (file_downloaded/file_size)*100
    dButton.config(text="{:00.0f} % dowmnloaded".format(per))

def makeselection(strm):
    count = 0
    for i in strm:
        Lb1.insert(count, strm[count])
        count += 1
    Lb1.pack()

    value = Lb1.get(Lb1.curselection())
    print(value)

def start_Download():
    global file_size
    try:
        dButton.config(text='please wait.....')
        dButton.config(state=DISABLED)
        path_to_save_video = askdirectory()
        if path_to_save_video is None:
            return


        url = urlField.get()
        ob = YouTube(url,on_progress_callback=progress)
        print(url)
        print(path_to_save_video)
        strm = ob.streams.all()
        file_size = strm[0].filesize
        vTitle.config(text=strm[0].title)
        vTitle.pack(side=TOP)
        makeselection(strm)


        #print()
        #print(strm[0].title + " ")
        #print(int((ob.streams.get_highest_resolution().filesize / 1000000)))
        #ob.streams.get_lowest_resolution().download(path_to_save_video)
        dButton.config(text='start download')
        dButton.config(state=NORMAL)
        showinfo("Download finished","Downlaoded Successfully")
        urlField.delete(0,END)
        vTitle.pack_forget()

    except Exception as e:
        print(e)
        print("error")


def start_Download_Thread():
    thread = Thread(target=start_Download())
    thread.start()



# GUI

main = Tk()
main.title("Youtube Downloader")
main.iconbitmap('tube.ico')
main.geometry("500x600")
file = PhotoImage(file='youtube-icon.png')
headingIcon = Label(main,image=file)
headingIcon.pack(side=TOP)

#URL textfield

urlField = Entry(main,font=("verdana",20),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=10)


#Download Button

dButton = Button(main,text="start download",font=("verdana",20),relief='ridge',command=start_Download_Thread)
dButton.pack(side=TOP,pady=10)

vTitle = Label(main,text="video title")
Lb1 = Listbox(main,width=80,height=100)




main.mainloop()

