class Treino:
    def __init__(self, id, nome, dia_semana, id_aluno):
        self.id = id
        self.nome = nome
        self.dia_semana = dia_semana
        self.id_aluno = id_aluno
        
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
    def dia_semana(self):
        return self._dia_semana
    
    @dia_semana.setter
    def dia_semana(self, ndia_semana):
        if not isinstance(ndia_semana, str):
            raise ValueError("digite um dia valido")
        ndia_semana = ndia_semana.strip().lower()
        if ndia_semana == "":
            raise ValueError("dia não pode ser vazio")
        if ndia_semana.endswith("-feira"):
            ndia_semana = ndia_semana.replace("-feira", "")
        self._dia_semana = ndia_semana
        
    @property
    def id_aluno(self):
        return self._id_aluno

    @id_aluno.setter
    def id_aluno(self, nid_aluno):
        if not isinstance(nid_aluno, int):
            raise ValueError("Escreva corretamente seu id")

        if nid_aluno <= 0:
            raise ValueError("id não pode ser menor ou igual a zero")
        self._id_aluno = nid_aluno