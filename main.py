from __future__ import unicode_literals
from tkinter import *
import youtube_dl
import os

root = Tk()
root.title("YouTube Downloader")
root.iconbitmap("C:/Users/mgelh/PycharmProjects/YoutubeDownloader/media/logo_youtube64.ico")
root.minsize(width=600, height=150)

quality = StringVar()


def showformats():
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
    result = ydl.extract_info(inputEntry.get(), download=False)
    formats = result.get('formats', [result])

    i = 2
    for f in formats:
        # todo lieber als dropdown? liste anlegen und items einfügen
        
        # r = Radiobutton(root, text=(f['format'] + "   " + f['ext']), variable=quality, value=f['format'])
        # r.grid(row=i, column=0, columnspan=2)
        i += 1


def download():
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    path = "C:/Users/mgelh/PycharmProjects/YoutubeDownloader/dist"
    path = os.path.realpath(path)
    os.startfile(path)


inputLabel = Label(root, text="Video URL: ")
inputEntry = Entry(root, width=80)
formatsButton = Button(root, text="List Formats", command=showformats)

inputEntry.insert(0,
                  "https://www.youtube.com/watch?v=YXPyB4XeYLA&t=11876s&ab_channel=freeCodeCamp.org")  # todo Test-URL entfernen

inputLabel.grid(row=0, column=0)
inputEntry.grid(row=0, column=1)
formatsButton.grid(row=1, column=1)

root.mainloop()
