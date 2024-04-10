class Matematica:

    def __init__(self):
        self._numeroBase = 0

    def fatorial (self, x :int) -> int:
        produtorio = 2
        valor = 1
        while produtorio <= x:
            valor *= produtorio
            produtorio += 1

        return valor
    

    def trianguloDePascal(self):
        triangulo = []
        num = 0
        k = 0
        n = 0
        while n <= self._numeroBase:
            linha = ''
            while k <= n:
                num = Matematica.fatorial(n) / Matematica.fatorial(k) * Matematica.fatorial(n-k)
                k += 1
                n += 1
                num = str(num)
                linha += num
            linha = linha.ljust(6, " ")
            triangulo.append(linha)
        return triangulo


mat = Matematica()
mat._numeroBase = 3
print(mat.trianguloDePascal())


        