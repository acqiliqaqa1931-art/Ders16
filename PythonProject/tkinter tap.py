# import tkinter as tk
# from tkinter import messagebox
#
# pencere=tk.Tk()
# pencere.geometry("500x500")
#
#
# listbox=tk.Listbox(pencere,width=30,height=20)
# listbox.pack()
#
# my_list=["Nutella","Plombir","Kolbasa","Sosiska","Fanat","Tendir coreyi","Zavod coreyi","Sirab","Alma","Lays","Qogal","Cappy multimeyve"]
#
# yazi=tk.Entry(pencere,width=30)
# yazi.pack(pady=5)
#
# def elave_et():
#     elave=yazi.get()
#     if elave:
#         listbox.insert(tk.END,elave)
#         yazi.delete(0,tk.END)
#     else:
#         messagebox.showwarning("Xeta","Bos ola bilmez")
#
# for item in my_list:
#     listbox.insert(tk.END,item)
#
# def delete():
#     selected=listbox.curselection()
#     for i in selected:
#         listbox.delete(i)
#
# def deleteall():
#     listbox.delete(0,tk.END)
#
# def update():
#     secim = listbox.curselection()
#     if secim:
#         index = secim[0]
#         yenideyer = yazi.get()
#         if yenideyer:
#             listbox.delete(index)
#             listbox.insert(index, yenideyer)
#             yazi.delete(0, tk.END)
#         else:
#             messagebox.showwarning("Xeta", "Doldurun")
#     else:
#         messagebox.showerror("Xeta", "Secim edin")
#
#
# btn = tk.Button(pencere, text="Sil", command=delete,bg="red")
# btn.pack(pady=5)
#
# btn1=tk.Button(pencere,text="Hamisini sil",command=deleteall,bg="darkred")
# btn1.pack(pady=5)
#
# btn2=tk.Button(pencere,text="Elave et",command=elave_et,bg="green")
# btn2.pack(pady=5)
#
# btn3=tk.Button(pencere,text="Deyis",command=update,bg="blue")
# btn3.pack(pady=5)
#
# pencere.mainloop()

