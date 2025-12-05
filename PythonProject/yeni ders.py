# f=open("data.txt","w")
# f.write("Salam necesen?\nskskksks\nksdkksks\nsksksksks")
#
# f.close()
#
#
#
# a=open("data.txt","r")
# print(a.readlines())
#
# a.close()


# f=open("data.txt","r+")
# print(f.read())
# f.write("salam milekim\nsalam mileki\nsalam milek\nsalam mile\nsalam mil\nsalam mi\nsalam m\nsalam\nsala\nsal\nsa\ns\n")
#
# f.close()


# f=open("data.txt","a")
# f.write("Setr elave olundu")
# f.close()

# f=open("dat.txt","x")
# f.write("Bura yazildi")
# f.close()


# with open("data.txt","w") as f:
#     f.write("Say hello to my little friend")

# with open("data.txt","r") as f:
#     print(f.read())

# with open("data.txt","r+") as f:
#     print(f.read())
#     f.write("\nKia patpresi")

# with open("data.txt","a") as f:
#     f.write("\nVelosiped diski")

# with open("da.txt","x") as f:
#     f.write("asfatijer")



# with open("file1.txt","w") as f1:
#     f1.write("Hello World")
#
# with open("file1.txt","r") as f1:
#     content=f1.read()
#
# with open("file2.txt","w") as f2:
#     f2.write(content)
#
# with open("file3.txt","w") as f3:
#     f3.write(content)











import tkinter as tk
from PIL import Image,ImageTk

pencere=tk.Tk()

img=Image.open("images (1).jpg")
img=ImageTk.PhotoImage(img)
label=tk.Label(pencere,image=img)
label.pack()



pencere.mainloop()