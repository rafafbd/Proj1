class Obra:
    def __init__(self, nomeArq: str, paraGravacao: bool) -> None:
        self.AnoDaObra: str[4] = ''
        self.MesDaobra: str[2] = ''
        self.AutorDaObra: str[20] = ''
        self.NomeDaObra: str[20] = ''
        self.Estilo: str[15] = ''
        self.ValorEstimado = 0.0
        self.urlFoto: str[100] = ''
        self._arqParaGravacao : bool = paraGravacao
        self._arquivo = open(nomeArq, "a" if paraGravacao else "")

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

    def gravarCamposNoArquivo(self, paraGravacao):
        if paraGravacao:
            linha = self.AnoDaObra + self.AutorDaObra + self.Estilo + self.MesDaobra + self.NomeDaObra + str(self.ValorEstimado) + self.urlFoto
            self._arquivo.write(linha)
            
    def preencherCampos(self, novoAno, novoMes, novoAutor, novoNome, novoEstilo, novoValor, novaURL):
        pass
    def fecharArquivo(self):
        pass
    def __str__(self) -> str:
        pass
    def compararCom(self, outraObra) -> int:
        pass