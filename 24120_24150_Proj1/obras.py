class Obra:
    def __init__(self, nomeArq: str, paraGravacao: bool) -> None:
        self.AnoDaObra = ''
        self.MesDaobra = ''
        self.AutorDaObra = ''
        self.NomeDaObra = ''
        self.Estilo = ''
        self.ValorEstimado = 0.0
        self.urlFoto = ''
        self._arqParaGravacao : bool = paraGravacao
        self._arquivo = open(nomeArq, "a" if paraGravacao else "r")

    def lerCamposDoArquivo(self):
        if not self._arqParaGravacao:
            linha: str = self._arquivo.readline()
            self.AnoDaObra = linha[0:4]
            self.MesDaobra = linha[4:6]
            self.Estilo = linha[6:21]
            self.NomeDaObra = linha[21:41]
            self.AutorDaObra = linha[41:61]
            self.ValorEstimado = linha[61:71]
            self.urlFoto = linha[71:171]
            return linha

    def gravarCamposNoArquivo(self):
        self._arquivo.write(self.__str__())
        
    def preencherCampos(self, novoAno: str, novoMes: str, novoAutor: str, novoNome: str, novoEstilo: str, novoValor, novaURL: str):
        self.AnoDaObra = novoAno.rjust(4, " ")
        self.MesDaobra = novoMes.rjust(2, " ")
        self.AutorDaObra = novoAutor.ljust(20, " ")
        self.NomeDaObra = novoNome.ljust(20, " ")
        self.Estilo = novoEstilo.ljust(15, " ")
        novoValor = str(novoValor)
        self.ValorEstimado = novoValor.ljust(10, " ")
        self.urlFoto = novaURL.ljust(100, " ")

    def fecharArquivo(self):
        self._arquivo.close()

    def __str__(self) -> str:
        linha = self.AnoDaObra + self.MesDaobra + self.Estilo + self.NomeDaObra + self.AutorDaObra + str(self.ValorEstimado) + self.urlFoto
        return linha
    
    def compararCom(self, outraObra) -> int:
        valor = 3   # Para ser diferente de qualquer valor pedido
        outraInstancia = outraObra
        instancia = int(self.AnoDaObra + self.MesDaobra + self.AutorDaObra + self.NomeDaObra)

        if instancia < outraInstancia:
            valor = -1

        if instancia == outraInstancia:
            valor = 0
            
        if instancia > outraInstancia:
            valor = 1