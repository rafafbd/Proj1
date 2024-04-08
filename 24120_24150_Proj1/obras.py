class Obra:
    def __init__(self, nomeArq: str, paraGravacao: bool) -> None:
        self.AnoDaObra = ''
        self.MesDaobra = ''
        self.AutorDaObra = ''
        self.NomeDaObra = ''
        self.Estilo = ''
        self.ValorEstimado = 0.0
        self.urlFoto = ''

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