
import os
import mat
import obras
from tkinter import filedialog

def ListagemDeObras():
    tipo_de_arquivo = (
        ("Arquivo de texto", "*.txt*"),
    )
    nomeDoArquivo = filedialog.askopenfilename(title= 'Selecione o arquivo',
                                               initialdir= r'c:\temp',
                                               multiple = False,
                                               filetypes= tipo_de_arquivo)
    

def opcao4():
    math = mat.Matematica()
    base = int(input("Digite quantas linhas do triângulo de Pascal devem ser mostradas: "))
    math._numeroBase = base
    triangulo = math.trianguloDePascal()
    for linha in triangulo:
        print(linha)


def fazer(escolha):
    opcoesPrevistas =  "01234"
    if escolha not in opcoesPrevistas:
        print("Opção inválida")
        tecla = input("Pressione [enter] para continuar: ")
    match escolha:
        case "0":
            os.system("cls") or None
            print("Programa finalizado. Obrigado pelo uso!")
        case "1":

            tecla = input("Pressione [enter] para continuar: ")
        case "2":
            
            tecla = input("Pressione [enter] para continuar: ")
        case "3":

            tecla = input("Pressione [enter] para continuar: ")
        case "4":
            opcao4()
            tecla = input("Pressione [enter] para continuar: ")
    

def SeletorDeOpcoes():
    opcao = ''
    while opcao != '0':
        os.system("cls") or None
        print("Seletor de opções\n")
        print("[0] --> Terminar programa")
        print("[1] --> Cadastro de obras de arte")
        print("[2] --> Listagem de obras de arte")
        print("[3] --> Página web de obras de arte")
        print("[4] --> Triângulo de Pascal")
        opcao = input("Digite a opção desejada: ")
        fazer(opcao)

if __name__ == '__main__':
    SeletorDeOpcoes()
