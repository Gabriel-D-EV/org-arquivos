import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

l_arq = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg"],
    "planilhas": [".xlsx", ".xls", ".csv"],
    "arquivos": [".pdf", ".docx"],
    "exe": [".exe"],
    "Zip": [".zip", ".rar"],
    "videos": [".avi", ".mp4"],
    "musicas": [".mp3"]
}

for arquivo in l_arq:
    
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.makedirs(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")