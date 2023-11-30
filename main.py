import os
from tkinter.filedialog import askdirectory
import customtkinter as ctk



ctk.set_appearance_mode('System')
ctk.set_default_color_theme('dark-blue')

app = ctk.CTk()
app.geometry('250x200')
app.title('Organizador')
app.resizable(False, False)

frame = ctk.CTkFrame(master=app, width=250, height=200)
frame.place(x=1, y=0)

txt = ctk.CTkLabel(master=frame, text='Qual pasta organizar?',font=('Reboco', 18)).place(x=40, y=40) 

def btn():

    caminho = askdirectory(title="Selecione uma pasta")

    l_arq = os.listdir(caminho)

    locais = {
        "imagens": [".png", ".jpg"],
        "planilhas": [".xlsx", ".xls", ".csv"],
        "arquivos": [".pdf", ".docx", ".txt"],
        "executavel": [".exe",".diagcab",".aplicativo",".cmd"],
        "Zip": [".zip", ".rar"],
        "videos": [".avi", ".mp4", ".amv",".wav"],
        "musicas": [".mp3"],
        "ISO": [".iso",".msi",".img"]
    }

    for arquivo in l_arq:
        
        nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
        for pasta in locais:
            if extensao in locais[pasta]:
                if not os.path.exists(f"{caminho}/{pasta}"):
                    os.makedirs(f"{caminho}/{pasta}")
                os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
                

botao = ctk.CTkButton(master=frame, text='Procurar', command=btn)
botao.place(x=55, y=80)
   
app.mainloop()
