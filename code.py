import tkinter as tk

def encrypt():
    inpString = input1.get()
    key = input2.get()
    encryptDecrypt(inpString, key)

def decrypt():
    inpString = input1.get()
    key = input2.get()
    encryptDecrypt(inpString, key)

def encryptDecrypt(inpString, key):
    newStr = ""
    txt = ""

    for i in inpString:
        result = ord(i) ^ ord(key)
        newStr = chr(result)
        txt = txt + newStr
    output.delete(0, tk.END)    
    output.insert(0, txt)



window = tk.Tk()
frame = tk.Frame(master=window, width=300, height=300,bg="#26242f")
frame.pack()


window.title("Encrypt/Decrypt Using Python")

window.geometry("400x300")
window.minsize(300, 300)
window.maxsize(500, 400)
window.configure(background="#26242f")


head = tk.Label(master=frame, text="Encrypt/Decrypt Using Python",fg="white",bg="#26242f", font=10)
head.pack(pady=(10,20))


label1 = tk.Label(master=frame, text="Enter Text To Encrypt/Decrypt",fg="white", bg="#26242f")
label1.pack()
input1 = tk.Entry(master=frame)
input1.pack()


label2 = tk.Label(master=frame, text="Enter The Key",fg="white", bg="#26242f")
label2.pack(pady=(20,0))
input2 = tk.Entry(master=frame)
input2.pack()
key = input2.get()


label3 = tk.Label(master=frame, text = "Convert",fg="white", bg="#26242f")
label3.pack(pady=(20,0))
btn1 = tk.Button(master=frame, text = "Go", command = encrypt)
btn1.pack()



label4 = tk.Label(master=frame, text = "Output: ",fg="white", bg="#26242f")
label4.pack(pady=(20,0))
output = tk.Entry(master=frame)
output.pack()


window.mainloop()