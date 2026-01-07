# main.py
from model import listar_arquivos

arquivos = listar_arquivos()

print("Arquivos encontrados:")
for arquivo in arquivos:
    print(f"- {arquivo}")
