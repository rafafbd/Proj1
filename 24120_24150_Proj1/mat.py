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
        n = 0
        while n < self._numeroBase:
            k = 0
            linha = ''
            while k <= n:
                num = int(self.fatorial(n) / self.fatorial(k) * self.fatorial(n-k))
                k += 1
                num = str(num)
                linha += num
                linha += " "
            n += 1
            triangulo.append(linha)
        return triangulo





        