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

    def lerCamposDoArquivo(self, paraGravacao):
        if not paraGravacao:
            self._arquivo.readline()
            linha: str = self._arquivo.readline()
            self.AnoDaObra = linha[0:4]
            self.MesDaobra = linha[4:6]
            self.AutorDaObra = linha[6:100]
            self.NomeDaObra = linha[100:200]
            self.Estilo = linha[200:205]
            self.ValorEstimado = linha[205:215]
            self.urlFoto = linha[215:]

    def gravarCamposNoArquivo(self):
        self._arquivo.write(self.__str__())
        
    def preencherCampos(self, novoAno: str, novoMes: str, novoAutor: str, novoNome: str, novoEstilo: str, novoValor, novaURL: str):
        self.AnoDaObra = novoAno.rjust(4, " ")
        self.MesDaobra = novoMes.rjust(2, " ")
        self.AutorDaObra = novoAutor.ljust(20, " ")
        self.NomeDaObra = novoNome.ljust(20, " ")
        self.Estilo = novoEstilo.ljust
        novoValor = str(novoValor)
        self.ValorEstimado = novoValor.ljust(9, " ")
        self.urlFoto = novaURL.ljust(100, " ")
    def fecharArquivo(self):
        self._arquivo.close()
    def __str__(self) -> str:
        linha = self.AnoDaObra + self.AutorDaObra + self.Estilo + self.MesDaobra + self.NomeDaObra + str(self.ValorEstimado) + self.urlFoto
        return linha
    def compararCom(self, outraObra) -> int:
        pass