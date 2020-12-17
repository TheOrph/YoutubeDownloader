from __future__ import unicode_literals
from tkinter import *
import youtube_dl
import os

root = Tk()
root.title("YouTube Downloader")
root.iconbitmap("C:/Users/mgelh/PycharmProjects/YoutubeDownloader/media/logo_youtube64.ico")
root.minsize(width=600, height=150)

quality = StringVar()
format_opts = ["No URL chosen"]
formats_drop = OptionMenu(root, quality, *format_opts)

def showdloadbtn(args):
    dload_btn = Button(root, text="Download", command=download)
    dload_btn.grid(row=2, column=2)

def showformats():
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
    result = ydl.extract_info(inputEntry.get(), download=False)
    formats = result.get('formats', [result])

    global formats_drop
    global format_opts

    format_opts = []
    for f in formats:
        format_opts.append(f["format"] + "   " + f["ext"])

    formats_drop.destroy()
    formats_drop = OptionMenu(root, quality, *format_opts, command=showdloadbtn)
    formats_drop.grid(row=2, column=0, columnspan=2)


def download():
    ydl_opts = {
        # "format": "249 - audio only (tiny)"
    }
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
formats_drop.grid(row=2, column=0, columnspan=2)

root.mainloop()
