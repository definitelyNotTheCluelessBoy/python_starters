import tkinter, tkinter.filedialog, PyPDF2

def open_window():
    print('nice')
    filename = tkinter.filedialog.askopenfilename(parent=root,title = "Select a File",filetypes = [("Pdf files","*.pdf*")])
    print(filename)

    if filename:
        mypdf = PyPDF2.PdfFileReader(filename)
        T = tkinter.Text(root)
        #print(mypdf.getNumPages())
        for i in range(mypdf.getNumPages()):
            page = mypdf.getPage(i)
            textFromPage=page.extractText()
            T.insert('insert',textFromPage)
        T.pack()

root = tkinter.Tk()
root.geometry('500x500')
root.title('text extractor')

label = tkinter.Label(root, text ='najdi pdf')
label.pack()

button = tkinter.Button(root,text='vyhladaj PDF',command=open_window)
button.pack()

root.mainloop()