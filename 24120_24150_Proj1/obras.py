class Obra:
    def __init__(self, nomeArq: str, paraGravacao: bool) -> None:
        self.AnoDaObra: str[4] = ''
        self.MesDaobra: str[2] = ''
        self.AutorDaObra: str[20] = ''
        self.NomeDaObra: str[20] = ''
        self.Estilo: str[15] = ''
        self.ValorEstimado = 0.0
        self.urlFoto: str[100] = ''

    def lerCamposDoArquivo(self):
        pass
    def gravarCamposNoArquivo(self):
        pass
    def preencherCampos(self, novoAno, novoMes, novoAutor, novoNome, novoEstilo, novoValor, novaURL):
        pass
    def fecharArquivo(self):
        pass
    def __str__(self) -> str:
        pass
    def compararCom(self, outraObra: Obra) -> int:
        pass