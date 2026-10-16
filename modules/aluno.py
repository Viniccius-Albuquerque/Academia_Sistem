class Aluno:
    PLANOS_VALIDOS = ["basico", "intermediario", "pro"]

    def __init__(self, id_aluno, nome, idade, plano, estado):
        self.id_aluno = id_aluno
        self.nome = nome
        self.idade = idade
        self.plano = plano
        self.estado = estado

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novoNome):
        if not isinstance(novoNome, str):
            raise ValueError("Escreva corretamente seu nome")

        novoNome = novoNome.strip()
        if novoNome == "":
            raise ValueError("Nome não pode ser vazio")
        self._nome = novoNome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, novaIdade):
        if isinstance(novaIdade, bool) or not isinstance(novaIdade, int):
            raise ValueError("Idade deve ser um número inteiro")

        if novaIdade <= 0:
            raise ValueError("Idade deve ser maior que zero")
        self._idade = novaIdade

    @property
    def plano(self):
        return self._plano

    @plano.setter
    def plano(self, novoPlano):
        if not isinstance(novoPlano, str):
            raise ValueError("Escreva corretamente seu plano")

        novoPlano = novoPlano.strip().lower()
        if novoPlano not in self.PLANOS_VALIDOS:
            raise ValueError("Plano inválido. Use basico, intermediario ou pro")

        self._plano = novoPlano

class AlunoCreate(Aluno):
    def __init__(self, nome, idade, plano):
        super().__init__(None, nome, idade, plano, None)

class AlunoUpdate(Aluno):
    def __init__(self, id, idade, plano):
        super().__init__(id, "nome temporario", idade, plano, None)