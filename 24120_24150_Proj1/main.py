
import os
import mat
import obras
import tkinter
from tkinter import filedialog
import webbrowser


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
    autor = input("Digite o nome do autor da obra: ")
    nome = input("Digite o nome da obra: ")
    estilo = input("Digite o estilo da obra: ")
    valor = float(input("Informe o valor estimado da obra: "))
    url = input("Digite o link url da imagem da obra: ")
    obra.preencherCampos(ano, mes, autor, nome, estilo, valor, url)
    obra.gravarCamposNoArquivo()
    comando = 'sort z:\\dados\\dados.txt /o ordenado.txt /+1'
    os.system(comando) or None
    obra.fecharArquivo()

def opcao2():
    somatoria = 0
    contador = 0
    Obra = obras.Obra(ListagemDeObras(), False)
    linha = "-"
    while linha != "":
        linha = Obra.lerCamposDoArquivo()   
        if linha != "":     # Como a linha recebe outra string dentro do while, usa-se dupla verificacao    
            print(linha)
            
            somatoria += Obra.ValorEstimado
            
            contador += 1
        
    print(f"      Número de obras: {contador}                  Valor: {somatoria}")
    Obra.fecharArquivo()
        

def opcao3():
    obra_no_html = ''
    obra1 = obras.Obra(ListagemDeObras(), False)
    arqRelatorio = open("Obras.html", "w")
    Total = 0.0
    ano = 500000 # 500000 garante que o ano nao e igual a nenhum outro ano 
    valores_do_mesmo_ano = 0.0 # Soma dos valores de obras de mesmo ano
    contador = 1
    # Estrutura basica do html e iniciacao da tabela
    estrutura_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabela de Obras</title>
    <style>
        *{
            text-align: center;
        }
        
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
    while obra1.lerCamposDoArquivo() != "":
        Total += float(obra1.ValorEstimado)
        ano_anterior = ano
        ano = obra1.AnoDaObra
        

        if contador != 1 and ano != ano_anterior: # Se o ano for diferente do anterior e nao for a primeira iteracao
                    obra_no_html += f'''
                        <tr class="titulo">
                            <th colspan="4">Total</th>
                            <th>{valores_do_mesmo_ano}</th>
                            <th></th>
                        </tr>
                    '''
                    valores_do_mesmo_ano = 0.0
        valores_do_mesmo_ano += float(obra1.ValorEstimado)
        obra_no_html += f'''
            <tr>
                <td>{obra1.AnoDaObra}/{obra1.MesDaobra}</td>
                <td>{obra1.NomeDaObra}</td>
                <td>{obra1.Estilo}</td>
                <td>{obra1.AutorDaObra}</td>
                <td>{obra1.ValorEstimado}</td>
                <td><img scr="{obra1.urlFoto}"></td>
            </tr>

        '''
        #print(obra_no_html)
        #print(f'iteracao: {contador}')
        contador += 1
    estrutura_html += obra_no_html
        
        
        
            

    estrutura_html += f'''
            <tr class="titulo">
                <th colspan="4">Total Geral</th>
                <th>{Total}</th>
                <th></th>
            </tr>
        </table>
    </div>
</body>
</html>
        '''
    arqRelatorio.write(estrutura_html)
    webbrowser.open_new_tab("Obras.html")
    arqRelatorio.close()

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


