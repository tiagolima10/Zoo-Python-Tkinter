class Animais:
    """
    Classe para criar animais para o zoológico.
    """
    def __init__(self, nome, classe, idade, sexo):
        """
        Método que instancia a classe Animais.
        :param nome: nome do animal.
        :param classe: classe do animal.
        :param idade: idade do animal.
        :param sexo: sexo do animal.
        """
        self.nome = nome
        self._classe = classe
        self.idade = idade
        self.sexo = sexo

    @property
    def nome_animal(self):
        """
        Método que mostra o nome do animal.
        """
        return self.nome

    @nome_animal.setter
    def nome_animal(self, nome):
        """
        Método que modifica o nome do animal.
        """
        self.nome = nome

    @property
    def classe_animal(self):
        """
        Método que mostra a classe do animal.
        """
        return self._classe

    @classe_animal.setter
    def classe_animal(self, classe):
        """
        Método que modifica a classe do animal.
        """
        self._classe = classe

    @property
    def idade_animal(self):
        """
        Método que mostra a idade do animal.
        """
        return self.idade

    @idade_animal.setter
    def idade_animal(self, idade):
        """
        Método que modifica a idade do animal.
        """
        self.idade = idade

    @property
    def sexo_animal(self):
        """
        Método que mostra o sexo do animal.
        """
        return self.sexo

    @sexo_animal.setter
    def sexo_animal(self, sexo):
        """
        Método que modifica o sexo do animal.
        """
        self.sexo = sexo
