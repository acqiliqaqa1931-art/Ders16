# import tkinter as tk
#
# pencere=tk.Tk()
# pencere.geometry("300x200")
# def yenisehife():
#     yeni=tk.Tk()
#     yeni.geometry("500x500")
#
# btn=tk.Button(pencere,text="Yeni sehife",command=yenisehife)
# btn.pack(pady=100)
#
# pencere.mainloop()




# import tkinter as tk
#
# pencere=tk.Tk()
# pencere.title("Tkinter")
# pencere.geometry("500x500")
#
# def c():
#     duyme.config(text="Salam")
#
# def d():
#     duyme.config(text="Necesen?")
#
#
#
# yazi=tk.Label(pencere,text="Duymeni Bas.")
# yazi.pack()
#
#
# duyme=tk.Button(pencere,text="Salam",font=("Arial",14),command=c)
# duyme.pack(pady=20)
#
# duyme2=tk.Button(pencere,text="Necesen?",font=("Arial",14),command=d)
# duyme2.pack(pady=20)
#
#
#
# pencere.mainloop()



















# import tkinter as tk
# pencere=tk.Tk()
# pencere.geometry("300x200")
# def yenisehife():
#     yeni=tk.Tk()
#     yeni.geometry("500x500")
#     def geri():
#         yeni.destroy()
#
#     geriduyme=tk.Button(yeni,text="Geri qayit",command=geri)
#     geriduyme.pack()
#
# btn=tk.Button(pencere,text="Yeni sehife",command=yenisehife)
# btn.pack()
#
# pencere.mainloop()

#
# import tkinter as tk
# p=tk.Tk()
# p.geometry("300x200")
#
# frame=tk.Frame(p,bg="lightblue")
# frame.pack(fill="both",expand=True)
#
# lb=tk.Label(frame,text="Bu frame icindedir")
# lb.pack()
#
# p.mainloop()

# import tkinter as tk
# pencere=tk.Tk()
# pencere.geometry("300x300")
#
# frame1=tk.Frame(pencere)
# frame1.pack(fill="both",expand=True)
#
# label1=tk.Label(frame1,text="Bura ilk sehife")
# label1.pack(pady=20)
#
# def sehife2_ac():
#     frame1.pack_forget()
#     frame2.pack(fill="both",expand=True)
#
# def geriqayit():
#     frame2.pack_forget()
#     frame1.pack()
#
# btn1=tk.Button(frame1,text="Yeni sehifeye kec",command=sehife2_ac)
# btn1.pack(pady=10)
#
# frame2=tk.Frame(pencere)
#
# label2=tk.Label(frame2,text="Bura ikinci sehife")
# label2.pack(pady=20)
#
# btn2=tk.Button(frame2,text="Ilk sehifeye qayit",command=geriqayit)
# btn2.pack(pady=10)
#
# pencere.mainloop()





# import tkinter as tk
# from tkinter import messagebox
#
# pencere=tk.Tk()
# pencere.geometry("300x300")
#
# def goster():
#     messagebox.showinfo("Melumat","Bu bir info mesajidir")
#
#
# btn=tk.Button(pencere,text="Mesaj goster",command=goster)
# btn.pack(pady=20)
#
# pencere.mainloop()



# import tkinter as tk
# from tkinter import messagebox
#
# window=tk.Tk()
# window.geometry("300x300")
#
# login=tk.Entry(window)
# login.pack(pady=10)
#
# password=tk.Entry(window,show="*")
# password.pack(pady=20)
#
# def yoxla():
#     if login.get()=="" or password.get()=="":
#         messagebox.showerror("Xeta!","Login ve ya password bos ola bilmez!")
#
#     else:
#         yeni=tk.Tk()
#         yeni.geometry("500x500")
#
# btn=tk.Button(window,text="Qeydiyyat tamamla",command=yoxla)
# btn.pack(pady=25)
#
# window.mainloop()



# import tkinter as tk
# from tkinter import messagebox
#
# pencer=tk.Tk()
# pencer.title("Qeydiyyat")
# pencer.geometry("500x500")
#
# login_frame=tk.Frame(pencer)
# login_frame.pack(fill="both",expand=True)
#
# login_entry=tk.Entry(login_frame)
# login_entry.pack(pady=10)
#
# pass_entry=tk.Entry(login_frame,show="*")
# pass_entry.pack(pady=10)
#
# def devam_et():
#     l=login_entry.get()
#     p=pass_entry.get()
#
#
#     if l=="" or p=="":
#         messagebox.showerror("Xeta!","Bos buraxmaq olmaz")
#     else:
#         login_frame.pack_forget()
#         yeni_frame.pack(fill="both",expand=True)
#
#
#
# btn=tk.Button(login_frame,text="Devam et",bg="green",command=devam_et)
# btn.pack(pady=25)
#
# yeni_frame=tk.Frame(pencer)
#
# def geri():
#     yeni_frame.pack_forget()
#     login_frame.pack(fill="both",expand=True)
#
#
# btn2=tk.Button(yeni_frame,text="Geri qayit",command=geri)
# btn2.pack()
#
#
#
# pencer.mainloop()





# import tkinter as tk
#
#
# pencere=tk.Tk()
# pencere.geometry("400x400")
# listbox=tk.Listbox(pencere)
# listbox.pack(pady=20)
# listbox.insert(tk.END,"Behram")
# listbox.insert(tk.END,"Bilal")
# listbox.insert(1,"Gul")
#
#
# pencere.mainloop()




# import tkinter as tk
#
# root=tk.Tk()
# root.geometry("500x500")
#
# listbox1=tk.Listbox(root)
# listbox1.pack()
#
# my_list=["Adem","Ziyeddin","Murad","Ferid","Nihad"]
#
# for item in my_list:
#     listbox1.insert(tk.END,item)
#
# def show_selected():
#     selected=listbox1.curselection()
#     for i in selected:
#         print(listbox1.get(i))
#
#
# btn=tk.Button(root,text="Sec",command=show_selected)
# btn.pack(pady=20)
#
#
# root.mainloop()










# import tkinter as tk
#
# pencere=tk.Tk()
# pencere.geometry("500x500")
#
# listbox1=tk.Listbox(pencere)
# listbox1.pack()
#
#
# listbox2=tk.Listbox(pencere)
# listbox2.pack()
#
#
#
#
#
# my_list=["HR departman","Adem","Ziyeddin","Murad"]
#
# my_list2=["Proqramlasdirma","Ferid","Nihad","Muhammed","Mehemmed"]
#
# for item in my_list:
#     listbox1.insert(tk.END,item)
#
# def show_selected():
#     selected=listbox1.curselection()
#     for i in selected:
#         print(listbox1.get(i))
#
# for item1 in my_list2:
#     listbox2.insert(tk.END,item1)
#
# def show_selected1():
#     selected=listbox2.curselection()
#     for i in selected:
#         print(listbox2.get(i))
#
#
# pencere.mainloop()









# import tkinter as tk
#
# pencere=tk.Tk()
# pencere.geometry("500x500")
#
# listbox=tk.Listbox(pencere)
# listbox.pack()
#
# my_list=["AA","BB","CC","DD","EE"]
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
#
# btn = tk.Button(pencere, text="Sil", command=delete)
# btn.pack(pady=20)
#
# btn1=tk.Button(pencere,text="Hamisini sil",command=deleteall)
# btn1.pack()
#
#
#
# pencere.mainloop()











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
# def sil():
#     secim=listbox.curselection()
#     if secim:
#         index=secim[0]
#         listbox.delete(index)
#     else:
#         messagebox.showerror("Xeta","Secim edin!")
#
# def update():
#     secim=listbox.curselection()
#     if secim:
#         index=secim[0]
#         yenideyer=yazi.get()
#         if yenideyer:
#             listbox.delete(index)
#             listbox.insert(index,yenideyer)
#             yazi.delete(0, tk.END)
#         else:
#             messagebox.showwarning("Xeta","Doldurun")
#     else:
#         messagebox.showerror("Xeta","Secim edin")
#
#
#
#
#
# def deleteall():
#     listbox.delete(0,tk.END)
#
#
# btn=tk.Button(pencere,width=20,text="Elave et",command=elave_et,bg="green")
# btn.pack(pady=5)
#
# btn1=tk.Button(pencere,width=20,text="Sil",command=sil,bg="red")
# btn1.pack(pady=5)
#
# btn2=tk.Button(pencere,width=20,text="Hamisini sil",command=deleteall,bg="darkred")
# btn2.pack(pady=5)
#
# btn2=tk.Button(pencere,width=20,text="Deyis",command=update,bg="lightblue")
# btn2.pack(pady=5)
#
#
# pencere.mainloop()

















# import tkinter as tk
# from tkinter import messagebox
#
# user_data={}
#
# def register_page():
#     reg=tk.Toplevel(root)
#     reg.title("Qeydiyyat")
#     reg.geometry("300x350")
#
#     tk.Label(reg,text="Istifadeci ad").pack(pady=5)
#     ent_user=tk.Entry(reg)
#     ent_user.pack()
#
#     tk.Label(reg,text="Istifadeci password").pack(pady=5)
#     ent_pass=tk.Entry(reg,show="*")
#     ent_pass.pack()
#
#     tk.Label(reg,text="Nickname").pack(pady=5)
#     ent_nickname=tk.Entry(reg)
#     ent_nickname.pack()
#
#     tk.Label(reg,text="Age").pack(pady=5)
#     ent_age=tk.Entry(reg)
#     ent_age.pack()
#
#     tk.Label(reg,text="Cins").pack(pady=5)
#     ent_gender=tk.Entry(reg)
#     ent_gender.pack()
#
#     def register():
#         username=ent_user.get()
#         password=ent_pass.get()
#         name=ent_nickname.get()
#         age=ent_age.get()
#         gender=ent_gender.get()
#
#         if not username or not password:
#              messagebox.showerror("Xeta","Istifadeci adi ve ya sifre bos ola bilmez")
#              return
#
#         if username in user_data:
#              messagebox.showerror("Xeta","Istifadeci adi istifade olunur!Basqa ad yoxla.")
#              return
#
#         user_data[username]={
#             "password":password,
#             "name":name,
#             "age":age,
#             "gender":gender
#         }
#         messagebox.showinfo("OK","Qeydiyyat tamamlandi")
#         reg.destroy()
#
#     tk.Button(reg,text="Qeyd ol",bg="green",fg="white",command=register).pack(pady=5)
#
# def change_password_window(username):
#     win=tk.Toplevel(root)
#     win.title("Sifre deyis")
#     win.geometry("300x230")
#
#     tk.Label(win,text="Kohne password").pack(pady=5)
#     old_pass=tk.Entry(win,show="*")
#     old_pass.pack()
#
#     tk.Label(win,text="Yeni password").pack(pady=5)
#     new_pass=tk.Entry(win,show="*")
#     new_pass.pack()
#
#     tk.Label(win,text="Passwordu tesdiqle").pack(pady=5)
#     new_pass1=tk.Entry(win,show="*")
#     new_pass1.pack()
#
#     def change_pass():
#         if old_pass.get()!=user_data[username]["password"]:
#             messagebox.showerror("Xeta","Parol sehvdir")
#             return
#
#         if new_pass.get()!=new_pass1.get():
#             messagebox.showerror("Xeta","Yeni password uygun gelmir")
#             return
#
#         user_data[username]["password"]=new_pass.get()
#         messagebox.showinfo("OK","Ugurlu tamamlandi")
#
#         win.destroy()
#
#     tk.Button(win,text="Tesdiqle",bg="#4acf50",fg="white",command=change_pass).pack(pady=15)
#
#
# def open_profile(username):
#     prof=tk.Toplevel(root)
#     prof.title("Profil")
#     prof.geometry("300x380")
#
#     user=user_data[username]
#
#     tk.Label(prof,text=f"Profil:{username}",font=("Arial",14,"bold")).pack(pady=10)
#
#     tk.Label(prof,text="Ad").pack()
#
#     ent_name=tk.Entry(prof)
#     ent_name.insert(0,user["name"])
#     ent_name.pack()
#
#     tk.Label(prof,text="Yas").pack()
#
#
#     ent_age=tk.Entry(prof)
#     ent_age.insert(0,user["age"])
#     ent_age.pack()
#
#     tk.Label(prof,text="Cins").pack()
#
#     ent_gender=tk.Entry(prof)
#     ent_gender.insert(0,user["gender"])
#     ent_gender.pack()
#
#     def update_info():
#         user["ad"]=ent_name.get()
#         user["yas"]=ent_age.get()
#         user["cins"]=ent_gender.get()
#         messagebox.showinfo("OK","Melumat yenilendi")
#
#
#     def delete_account():
#         if messagebox.askyesno("Tesdiq","Hesabi silmek istiyirsiniz?"):
#             del user_data[username]
#             messagebox.showinfo("OK","Hesab silindi")
#             prof.destroy()
#
#
#     tk.Button(prof,text="Yenile",bg="grey",fg="pink",command=update_info).pack(pady=5)
#
#     tk.Button(prof,text="Hesabi sil",bg="blue",fg="white",command=delete_account).pack(pady=5)
#
#     tk.Button(prof,text="Sifre deyis",bg="green",fg="white",command=lambda:change_password_window(username)).pack(pady=5)
#
#
# def open_admin_panel():
#     admin_win=tk.Toplevel(root)
#     admin_win.title("Admin Panel")
#     admin_win.geometry("700x700")
#     tk.Label(admin_win,text="Admin Paneli").pack(pady=10)
#
#     listbox=tk.Listbox(admin_win,width=30)
#     listbox.pack(pady=10)
#
#     for username in user_data:
#         listbox.insert(tk.END,username)
#
#     tk.Label(admin_win, text="Ad").pack(pady=5)
#     ent_name = tk.Entry(admin_win)
#     ent_name.pack()
#
#     tk.Label(admin_win, text="Yas").pack(pady=5)
#     ent_age = tk.Entry(admin_win)
#     ent_age.pack()
#
#     tk.Label(admin_win, text="Cins").pack(pady=5)
#     ent_gender = tk.Entry(admin_win)
#     ent_gender.pack()
#
#     tk.Label(admin_win, text="Yeni sifre").pack(pady=5)
#     ent_new_password = tk.Entry(admin_win,show="*")
#     ent_new_password.pack()
#
#     def select_user(event):
#         selected=listbox.curselection()
#         if selected:
#             username=listbox.get(selected[0])
#             user=user_data[username]
#             ent_name.delete(0,tk.END)
#             ent_name.insert(0,user["name"])
#
#             ent_age.delete(0,tk.END)
#             ent_age.insert(0,user["age"])
#
#             ent_gender.delete(0,tk.END)
#             ent_gender.insert(0,user["gender"])
#     listbox.bind("<<ListboxSelect>>",select_user)
#
#     def update_user():
#         selected = listbox.curselection()
#         if selected:
#             username = listbox.get(selected[0])
#
#             user = user_data[username]
#             user["ad"]=ent_name.get()
#             user["yas"] = ent_age.get()
#             user["cins"] = ent_gender.get()
#             messagebox.showinfo("OK",f"{username} Melumat yenilendi!")
#
#     def change_user_pass():
#         selected = listbox.curselection()
#         if selected:
#             username = listbox.get(selected[0])
#             new_pass=ent_new_password.get()
#
#             if len(new_pass)<3:
#                 messagebox.showerror("Xeta","Sifre 3den az ola bilmez!")
#                 return
#
#             user_data[username]["password"]=new_pass
#             messagebox.showinfo("OK", "Sifre yenilendi!")
#
#     def delete():
#         selected=listbox.curselection()
#         if selected:
#             username=listbox.get(selected[0])
#             if messagebox.askyesno("Tesdiq", "Hesabi silmek istiyirsiniz?"):
#                 del user_data[username]
#                 listbox.delete(selected[0])
#
#                 ent_name.delete(0,tk.END)
#                 ent_age.delete(0,tk.END)
#                 ent_gender.delete(0,tk.END)
#                 messagebox.showinfo("OK",f"{username} silindi!")
#
#     tk.Button(admin_win, text="Yenile", bg="grey", fg="pink", command=update_user).pack(pady=5)
#
#     tk.Button(admin_win, text="Hesabi sil", bg="blue", fg="white", command=delete).pack(pady=5)
#
#     tk.Button(admin_win, text="Sifre deyis", bg="green", fg="white", command=change_user_pass).pack(pady=5)
#
#
#
# def login():
#     username=ent_user.get()
#     password=ent_pass.get()
#
#     if username=="admin" and password=="admin":
#         open_admin_panel()
#
#     elif username in user_data and user_data[username]["password"]==password:
#         open_profile(username)
#     else:
#         messagebox.showerror("Xeta","Login ve ya Sifre sehvdir")
#
#
#
#
#
# root=tk.Tk()
# root.title("Login Sistemi")
# root.geometry("500x500")
#
# tk.Label(root,text="Istifadeci adi").pack(pady=5)
# ent_user=tk.Entry(root)
# ent_user.pack()
#
# tk.Label(root,text="Istifadeci password").pack(pady=5)
# ent_pass=tk.Entry(root,show="*")
# ent_pass.pack()
#
# btn=tk.Button(root,text="Daxil ol",bg="pink",fg="white",command=login)
# btn.pack(pady=10)
#
# btn1=tk.Button(root,text="Qeydiyyat",bg="#2196f3",fg="white",command=register_page)
# btn1.pack()
#
#
# root.mainloop()













# import tkinter as tk
# from tkinter import ttk
#
# root=tk.Tk()
# root.geometry("500x500")
#
# adlar=["Kamal","Ferid","Nihad","Qulam"]
#
# combo=ttk.Combobox(root,values=adlar,state="readonly")
# combo.pack()
# def secildi(event):
#     secilen_ad=combo.get()
#
#     secilen_label.config(text=f"Secdiyiniz ad:{secilen_ad}")
#
# combo.bind("<<ComboboxSelected>>",secildi)
#
# secilen_label=tk.Label(root,text="Hele seciminizi etmemisiniz")
# secilen_label.pack(pady=10)
#
# root.mainloop()








# import tkinter as tk
# from tkinter import messagebox
#
# user_data={}
#
# def register_page():
#     reg=tk.Toplevel(root)
#     reg.title("Xestexana Qeydiyyati")
#     reg.geometry("300x350")
#
#
#     tk.Label(reg,text="Xestenin adi").pack(pady=5)
#     ent_user=tk.Entry(reg)
#     ent_user.pack()
#
#     tk.Label(reg,text="Xestenin xesteliyi").pack(pady=5)
#     ent_illness=tk.Entry(reg)
#     ent_illness.pack()
#
#     tk.Label(reg,text="Xestenin soyadi").pack(pady=5)
#     ent_nickname=tk.Entry(reg)
#     ent_nickname.pack()
#
#     tk.Label(reg,text="Xestenin yasi").pack(pady=5)
#     ent_age=tk.Entry(reg)
#     ent_age.pack()
#
#     tk.Label(reg,text="Xestenin nomresi").pack(pady=5)
#     ent_number=tk.Entry(reg)
#     ent_number.pack()
#
#     def register():
#         username=ent_user.get()
#         illness=ent_illness.get()
#         nickname=ent_nickname.get()
#         age=ent_age.get()
#         number=ent_number.get()
#
#         if not username or not illness or not nickname or not age or not number:
#              messagebox.showerror("Xeta","Qeydiyyati tam doldurun!")
#              return
#
#         if username and nickname in user_data:
#              messagebox.showerror("Xeta","Xestenin adi ve soyadi istifade olunur!")
#              return
#
#         if not age.isdigit() or not number.isdigit():
#             messagebox.showerror("Xeta","Yas ve Elaqe nomresi reqem olmalidir!")
#             return
#
#         user_data[username]={
#             "username":username,
#             "illness":illness,
#             "nickname":nickname,
#             "age":age,
#             "number":number
#         }
#         messagebox.showinfo("OK","Qeydiyyat tamamlandi")
#         reg.destroy()
#
#     tk.Button(reg,text="Qeyd ol",bg="green",fg="white",command=register).pack(pady=5)
#
#
# def open_profile(username):
#     prof=tk.Toplevel(root)
#     prof.title("Profil")
#     prof.geometry("300x380")
#
#     user=user_data[username]
#
#     tk.Label(prof,text=f"Profil:{username}",font=("Arial",14,"bold")).pack(pady=10)
#
#     tk.Label(prof,text="Ad").pack()
#
#     ent_user=tk.Entry(prof)
#     ent_user.insert(0,user["username"])
#     ent_user.pack()
#
#     tk.Label(prof,text="Yas").pack()
#
#
#     ent_age=tk.Entry(prof)
#     ent_age.insert(0,user["age"])
#     ent_age.pack()
#
#     tk.Label(prof,text="Nomre").pack()
#
#     ent_number=tk.Entry(prof)
#     ent_number.insert(0,user["number"])
#     ent_number.pack()
#
#     tk.Label(prof,text="Xestelik").pack()
#     ent_illness=tk.Entry(prof)
#     ent_illness.insert(0,user["illness"])
#     ent_illness.pack()
#
#     tk.Label(prof,text="Soyad").pack()
#     ent_nickname=tk.Entry(prof)
#     ent_nickname.insert(0,user["nickname"])
#     ent_nickname.pack()
#
#     def update_info():
#         age1=ent_age.get()
#         number1=ent_number.get()
#
#         if not age1.isdigit() or not number1.isdigit():
#             messagebox.showerror("Xeta","Yas ve ya nomre reqem olmalidir!")
#             return
#
#         user["username"]=ent_user.get()
#         user["age"]=ent_age.get()
#         user["number"]=ent_number.get()
#         user["illness"]=ent_illness.get()
#         user["nickname"]=ent_nickname.get()
#         messagebox.showinfo("OK","Melumat yenilendi")
#         prof.destroy()
#
#
#     def delete_account():
#         if messagebox.askyesno("Tesdiq","Hesabi silmek istiyirsiniz?"):
#             del user_data[username]
#             messagebox.showinfo("OK","Hesab silindi")
#             prof.destroy()
#
#
#     tk.Button(prof,text="Yenile",bg="grey",fg="pink",command=update_info).pack(pady=5)
#
#     tk.Button(prof,text="Hesabi sil",bg="blue",fg="white",command=delete_account).pack(pady=5)
#
# def open_admin_panel():
#     admin_win=tk.Toplevel(root)
#     admin_win.title("Admin Panel")
#     admin_win.geometry("700x700")
#     tk.Label(admin_win,text="Admin Paneli").pack(pady=10)
#
#     listbox=tk.Listbox(admin_win,width=30)
#     listbox.pack(pady=10)
#
#     for username in user_data:
#         listbox.insert(tk.END,username)
#
#     tk.Label(admin_win, text="Ad").pack(pady=5)
#     ent_user = tk.Entry(admin_win)
#     ent_user.pack()
#
#     tk.Label(admin_win, text="Xestelik").pack(pady=5)
#     ent_illness = tk.Entry(admin_win)
#     ent_illness.pack()
#
#     tk.Label(admin_win, text="Yas").pack(pady=5)
#     ent_age = tk.Entry(admin_win)
#     ent_age.pack()
#
#     tk.Label(admin_win, text="Number").pack(pady=5)
#     ent_number = tk.Entry(admin_win)
#     ent_number.pack()
#
#     tk.Label(admin_win,text="Soyad").pack(pady=5)
#     ent_nickname = tk.Entry(admin_win)
#     ent_nickname.pack()
#
#     def select_user(event):
#         selected=listbox.curselection()
#         if selected:
#             username=listbox.get(selected[0])
#             user=user_data[username]
#             ent_user.delete(0,tk.END)
#             ent_user.insert(0,user["username"])
#
#             ent_age.delete(0,tk.END)
#             ent_age.insert(0,user["age"])
#
#             ent_number.delete(0,tk.END)
#             ent_number.insert(0,user["number"])
#
#             ent_illness.delete(0,tk.END)
#             ent_illness.insert(0,user["illness"])
#
#             ent_nickname.delete(0,tk.END)
#             ent_nickname.insert(0,user["nickname"])
#
#
#     listbox.bind("<<ListboxSelect>>",select_user)
#
#     def update_user():
#         selected = listbox.curselection()
#         age2=ent_age.get()
#         number2=ent_number.get()
#         if selected:
#             username = listbox.get(selected[0])
#             if not age2.isdigit() or not number2.isdigit():
#                 messagebox.showerror("Xeta", "Yas ve ya nomre reqem olmalidir!")
#                 return
#
#
#             user = user_data[username]
#             user["username"]=ent_user.get()
#             user["age"] = ent_age.get()
#             user["number"] = ent_number.get()
#             user["illness"] = ent_illness.get()
#             user["nickname"]=ent_nickname.get()
#             messagebox.showinfo("OK",f"{username} Melumat yenilendi!")
#             admin_win.destroy()
#
#     def delete():
#         selected=listbox.curselection()
#         if selected:
#             username=listbox.get(selected[0])
#             if messagebox.askyesno("Tesdiq", "Hesabi silmek istiyirsiniz?"):
#                 del user_data[username]
#                 listbox.delete(selected[0])
#
#                 ent_user.delete(0,tk.END)
#                 ent_age.delete(0,tk.END)
#                 ent_number.delete(0,tk.END)
#                 messagebox.showinfo("OK",f"{username} silindi!")
#                 admin_win.destroy()
#
#     tk.Button(admin_win, text="Yenile", bg="grey", fg="pink", command=update_user).pack(pady=5)
#
#     tk.Button(admin_win, text="Hesabi sil", bg="blue", fg="white", command=delete).pack(pady=5)
#
#
#
#
# def login():
#     username=ent_user.get()
#     number=ent_number.get()
#
#     if username=="admin" and number=="admin123":
#         open_admin_panel()
#
#     elif username in user_data and user_data[username]["number"]==number:
#         open_profile(username)
#     else:
#         messagebox.showerror("Xeta","Login ve ya Sifre sehvdir")
#
#
#
#
#
# root=tk.Tk()
# root.title("Login Sistemi")
# root.geometry("500x500")
#
# tk.Label(root,text="Xestenin adi").pack(pady=5)
# ent_user=tk.Entry(root)
# ent_user.pack()
#
# tk.Label(root,text="Xestenin nomresi").pack(pady=5)
# ent_number=tk.Entry(root)
# ent_number.pack()
#
# btn=tk.Button(root,text="Daxil ol",bg="pink",fg="white",command=login)
# btn.pack(pady=10)
#
# btn1=tk.Button(root,text="Qeydiyyat",bg="#2196f3",fg="white",command=register_page)
# btn1.pack()
#
#
# root.mainloop()






# import tkinter as tk
#
# root=tk.Tk()
# root.geometry("500x500")
#
# secilen=tk.StringVar()
#
# secilen.set("Baslangic deyer yoxdur")
#
# tk.Radiobutton(root,text="Kisi",value="Kisi",variable=secilen).pack()
# tk.Radiobutton(root,text="Qadin",value="Qadin",variable=secilen).pack()
# tk.Radiobutton(root,text="Diger",value="Diger",variable=secilen).pack()
#
# def goster():
#     tk.Label(root,text=f"Secdiyin:{secilen.get()}").pack(pady=10)
#
#
#
#
# tk.Button(root,text="Sec",command=goster).pack(pady=10)
#
#
#
#
# root.mainloop()











# import tkinter as tk
#
# root=tk.Tk()
# root.geometry("500x500")
#
#
# img=tk.PhotoImage(file="png-clipart-black-and-gray-bmw-e39-coupe-need-for-speed-carbon-need-for-speed-most-wanted-need-for-speed-underground-2-the-need-for-speed-need-for-speed-s-compact-car-sedan.png")
# lb=tk.Label(root,image=img)
# lb.pack()
#
# root.mainloop()



# import tkinter as tk
# from tkinter import *
# from PIL import Image,ImageTk
# root=tk.Tk()
# root.geometry("500x500")
# image1=Image.open("png-clipart-mario-mario.png")
#
# photo=ImageTk.PhotoImage(image1)
# lb=tk.Label(root,image=photo)
# lb.place(x=0,y=0)
#
#
# image2=Image.open("430-4301937_luigi-png-luigis-mansion-png-luigis-mansion-luigi.png")
#
# photo2=ImageTk.PhotoImage(image2)
# lb2=tk.Label(root,image=photo2)
# lb2.place(x=550,y=0)
#
# image3=Image.open("5b0eab3db81a279977aea2397d4a1b23.jpg")
#
# photo3=ImageTk.PhotoImage(image3)
# lb3=tk.Label(root,image=photo3)
# lb3.place(x=1250,y=0)
#
#
# root.mainloop()





# import tkinter as tk
# from tkinter import *
# from PIL import Image,ImageTk
#
# image_path=["png-clipart-mario-mario.png","430-4301937_luigi-png-luigis-mansion-png-luigis-mansion-luigi.png","5b0eab3db81a279977aea2397d4a1b23.jpg"]
#
# root=tk.Tk()
#
# root.geometry("700x700")
#
# def change_image():
#     global current_image
#     current_image=(current_image+1)%len(image_path)
#     image=Image.open(image_path[current_image])
#     tk_image=ImageTk.PhotoImage(image)
#     label.configure(image=tk_image)
#     label.image=tk_image
#     root.after(1000,change_image)
#
#
# current_image=0
# image = Image.open(image_path[current_image])
# tk_image = ImageTk.PhotoImage(image)
# label=tk.Label(root,image=tk_image)
# label.pack()
# root.after(2000, change_image)
#
# root.mainloop()















