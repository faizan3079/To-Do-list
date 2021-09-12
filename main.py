from tkinter import *
import tkinter.messagebox as mb
td=Tk()

td.geometry('400x400+500+150')
fr= Frame(td)
fr.pack(pady=20)
def add():
    task =  e.get()
    if task  != "":
        lb.insert(0,task)
    else:
        mb.showinfo("Empty Task","Add a task")

def rem():
    work = lb.delete(ANCHOR)
    mb.showinfo("Removed","Your selected Task is Removed ")
    

# td.iconbitmap(default='todo.ico')
td.title("To-Do-List")
td.config(bg='#ABC3F3')
pic= PhotoImage(file= 'todo.png')
td.iconphoto(False, pic)
e=Entry(td,bd=5)
b1 = Button(td, text="Add a task",command= add,bd=5, pady = 5,bg='light green') 
b2= Button(td ,text = "Remove the task", command =rem ,bd=5,pady = 5,bg='#EC6A75')
lb= Listbox(td, height= 15, width= 40,font= ('Times',10))
task_list = [
    'Eat apple',
    'drink water',
    'go gym',
    'write software',
    'write documentation',
    'take a nap',
    'Learn something',
    'paint canvas'
    ]
for item in task_list:
    lb.insert(0, item)
s= Scrollbar(td)
s.pack(side =RIGHT)
lb.config(yscrollcommand=s.set)
s.config(command=lb.yview)


e.pack(side= BOTTOM , padx = 20, pady = 20)
lb.pack(side= TOP)
b1.place(x=326,y=300)
b2.place(x=0,y=300)

td.mainloop()
