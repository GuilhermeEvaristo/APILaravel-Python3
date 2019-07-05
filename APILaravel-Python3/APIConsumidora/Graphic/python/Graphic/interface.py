from tkinter import *
import requests
import json
import os


#Get/Post
def post(nome):
    if requests.post('http://localhost:8000/api/reis', data = {'name':nome}):
        return('Enviado com Sucesso!')
    else :
        return('Deu Algum erro ai...')
def get():
    data = requests.get('http://localhost:8000/api/reis')
    binary = data.content
    output = json.loads(binary)
    for item in output['data']:
        labelList['text'] = "Saudem o Rei " + item['name']
#Window Configuration
window = Tk()
window.title("Game Of Python 3.0")
canvas = Canvas(window.resizable(0,0), height='500', width='500')
canvas.pack()
#Background
background = PhotoImage(file='teste.png')
backgroundLabel = Label(window, image=background)
backgroundLabel.place(relwidth=1, relheight=1)
#Frames
frameList = Frame(window, bg='#f0f0f5', bd=10)
frameList.place(relx=0.5, rely=0.50, relwidth=0.75, relheight=0.4, anchor='center')

frameList2 = Frame(window, bg='#f0f0f5', bd=10)
frameList2.place(relx=0.5, rely=0.9, relwidth=0.75, relheight=0.1, anchor='center')

frame = Frame(window, bg='#f0f0f5', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='center')

frame2 = Frame(window, bg='#f0f0f5', bd=5)
frame2.place(relx=0.5, rely=0.23, relwidth=0.75, relheight=0.1, anchor='center')
#Entry inputs
entry = Entry(frame, font=20)
entry.place(relwidth=0.65, relheight=1)
#Buttons
button = Button(frame, text="King Name",command=lambda : post(entry.get()))
button.place(relx=0.7, relwidth=0.30, relheight=1)

button2 = Button(frameList2, text="Saudação",command=lambda : get())
button2.place(relwidth=1, relheight=1)
#Labels
labelList = Label(frameList, bg='white')
labelList.place(relwidth=1, relheight=1)

window.mainloop()