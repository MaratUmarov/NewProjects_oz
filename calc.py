from tkinter import*


window=Tk()
window.geometry("400x400")
window.resizable(0,0)
window.title("Pirany's Calc")



in_frame=Frame(window,width=380,heght=50)
in_frame.pack(side=TOP)

b_frame=Frame(window,width=380,heght=450,bg="Darkgrey")
b_frame.pack()


count_text=StringVar()
entry=Entry(in_frame,font=("Helvetica",20,"bold"),textvariable=count_text,width=70,justify=RIGHT)
entry.pack(ipady=14)

solution=""
def button_click(label):
    global solution
    if label=="C":
        solution=""
        count_text.set("")
    elif label=="=":
        result=str(eval(solution))
        count_text.set(result)
        solution=""
    else:
        solution=solution+str(label)
        count_text.set(solution)

def create_button(parent,text,row,column,command, width=13,columnspan=1)
    btn=Button(
        parent,
        text=text,
        width=width,
        heght=5,
        bd=0,
        bg="White" if text.isdigit() else "Lightgrey":
        command=command
    )                
    btn.grid(row=row,column=column,columnspan=columnspan,padx=1,pady=1)
create_button(b_frame,"C",0,0,lambda:button_click("C"),width=42,columnspan=3)         
create_button(b_frame,"0",4,0,lambda:button_click(0),width=27,columnspan=2)         
create_button(b_frame,".",0,0,lambda:button_click("."))

operations=["/","*",]


window.mainloop()