import tkinter

main_window = tkinter.Tk()

# Tk, Label, Button --> class
# label1, tombol1 --> object
# pack(), mainloop() --> method

label1 = tkinter.Label(main_window, text = "Label 1")
label2 = tkinter.Label(main_window, text = "Label 2")

tombol1 = tkinter.Button(main_window, text = "Tombol 1")
tombol2 = tkinter.Button(main_window, text = "Tombol 2")

# method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# method menampilkan GUI
main_window.mainloop()