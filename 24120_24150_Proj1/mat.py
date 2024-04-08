class Matematica:

    def __init__(self):
        self.__numeroBase = int

    def fatorial (x :int) -> int:
        _produtorio = 2
        _valor = 1
        while _produtorio <= x:
            _valor *= _produtorio
            _produtorio += 1

        return _valor
    

    def trianguloDePascal(self):
        _k = 0
        _n = 0