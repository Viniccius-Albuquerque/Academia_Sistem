class Exercicio:
    def __init__(self, id, nome, series, repeticoes, id_treino):
        self.id = id
        self.nome = nome
        self.series = series
        self.repeticoes = repeticoes
        self.id_treino = id_treino
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nnome):
        if not isinstance(nnome, str):
            raise ValueError("digite um nome valido")
        nnome = nnome.strip()
        if nnome == "":
            raise ValueError("Nome não pode ser vazio")
        self._nome = nnome
        
    @property
    def id_treino(self):
        return self._id_treino

    @id_treino.setter
    def id_treino(self, nid_treino):
        if not isinstance(nid_treino, int):
            raise ValueError("Escreva corretamente seu id")

        if nid_treino <= 0:
            raise ValueError("id não pode ser menor ou igual a zero")
        self._id_treino = nid_treino
        
    @property
    def series(self):
        return self._series

    @series.setter
    def series(self, nseries):
        if not isinstance(nseries, int):
            raise ValueError("Escreva corretamente seu id")

        if nseries <= 0:
            raise ValueError("id não pode ser menor ou igual a zero")
        self._series = nseries
        
    @property
    def repeticoes(self):
        return self._repeticoes

    @repeticoes.setter
    def repeticoes(self, nrepeticoes):
        if not isinstance(nrepeticoes, int):
            raise ValueError("Escreva corretamente seu id")

        if nrepeticoes <= 0:
            raise ValueError("id não pode ser menor ou igual a zero")
        self._repeticoes = nrepeticoes
        
class ExercicioCreate(Exercicio):
    def __init__(self, nome, series, repeticoes, id_treino):
        super().__init__(None, nome, series, repeticoes, id_treino)
        
class ExercicioUpdate(Exercicio):
    def __init__(self, id, nome, series, repeticoes):
        super().__init__(id, nome, series, repeticoes, 1)