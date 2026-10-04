import wikipedia
from  tkinter import *

def on_click():
    q= get_q.get()
    text.insert(INSERT,  wikipedia.summary(q))
    # query = input ("Enter the topic :")
    # result = wikipedia.summary(query)
    # print (result )

Root = Tk()
Root.title("Wikipedia search")
question = Label(Root, text = "Question ")
question.pack()
get_q= Entry(Root,bd=5)
get_q.pack()

submit = Button(Root , text = "Search ", command= on_click )
submit.pack()

text = Text(Root)
text.pack()

Root.mainloop()