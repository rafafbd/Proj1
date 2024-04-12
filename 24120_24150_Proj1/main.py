
import os
import mat
import obras
import tkinter
from tkinter import filedialog


objeto = tkinter.Tk() # Instaciação da classe Tk
objeto.withdraw()
objeto.attributes("-topmost", True) # É para o explorador de arquivos aparecer em cima do visual studio code

def ListagemDeObras():
    tipo_de_arquivo = (
        ("Arquivo de texto", "*.txt*"),
    )
    nomeDoArquivo = filedialog.askopenfilename(title= 'Selecione o arquivo',
                                               initialdir= r'c:\temp',
                                               multiple = False,
                                               filetypes= tipo_de_arquivo)
    return nomeDoArquivo
    

def opcao1():
    obra = obras.Obra(ListagemDeObras(), True)
    ano = input("Digite o ano da obra: ")
    mes = input("Digite o mês da obra: ")
    autor = input("Digite o nome do autor da obra")
    nome = input("Digite o nome da obra: ")
    estilo = input("Digite o estilo da obra: ")
    valor = float(input("Informe o valor estimado da obra: "))
    url = input("Digite o link url da imagem da obra: ")
    obra.preencherCampos(ano, mes, autor, nome, estilo, valor, url)
    obra.gravarCamposNoArquivo()
    obra.fecharArquivo()

def opcao2():
    somatoria = 0
    contador = 0
    Obra = obras.Obra(ListagemDeObras(), "r")
    while Obra.lerCamposDoArquivo() != "":
        print(Obra.lerCamposDoArquivo())
        somatoria += Obra.ValorEstimado
        contador += 1
    print(f"      Número de obras: {contador}                  Valor: {somatoria}")
        

def opcao3():
    obra1 = obras.Obra(ListagemDeObras(), False)
    leitura = open(obra1._arquivo)
    arqRelatorio = open("obras.html", "w")
    estrutura_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabela de Obras</title>
    <style>
        table, th, tr, td{
            border-collapse: collapse;
            border: 1px solid black;
            overflow: hidden;
        }

        .titulo{
            background-color: rgb(126, 199, 231);
        }

        .subDivisoes{
            background-color: rgb(209, 254, 254);
        }

        .pintado{
            background-color: rgb(252, 252, 181);
        }

    </style>
</head>
<body>
    <div>
        <table>
            <tr class="titulo">
                <th colspan="6">RELATÓRIO DE OBRAS DA GALERIA VIRTUAL</th>
            </tr>

            
            '''
    while leitura.readline() != "":
        linha = leitura.readline()
        estrutura_html += f'''
            <tr>
                <td>{linha[0:4]}/{linha[4:6]}</td>
                <td>{linha[21:41]}</td>
                <td>{linha[6:21]}</td>
                <td>{linha[41:61]}</td>
                <td>{linha[61:71]}</td>
                <td><img scr="{linha[71:171]}"></td>
            </tr>

            <tr class="subDivisoes">
                <th colspan="4">Total</th>
                <th></th>
                <th></th>
            </tr>
        '''

    estrutura_html += f'''
            <tr class="titulo">
                <th colspan="4">Total Geral</th>
                <th></th>
                <th></th>
            </tr>
        </table>
    </div>
</body>
</html>
        '''
    
    

    
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
            opcao1()
            tecla = input("Pressione [enter] para continuar: ")
        case "2":
            opcao2()
            tecla = input("Pressione [enter] para continuar: ")
        case "3":
            opcao3()
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
