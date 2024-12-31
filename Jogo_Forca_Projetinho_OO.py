import json
import random
from abc import ABC, abstractmethod

class ArquivoHandler:
    """Classe para manipulação de arquivos JSON."""
    @staticmethod
    def salvar_dados(caminho, dados):
        with open(caminho, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)

    @staticmethod
    def carregar_dados(caminho):
        try:
            with open(caminho, 'r') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            return {}

class JogoBase(ABC):
    """Classe abstrata representando um jogo genérico."""
    @abstractmethod
    def iniciar(self):
        pass

class JogoDaForca(JogoBase):
    """Classe principal do jogo da forca."""
    def __init__(self, palavras):
        self.__palavras = palavras
        self.__palavra_secreta = ''
        self.__tentativas = 6
        self.__letras_descobertas = []
        self.__letras_erradas = []

    def __escolher_palavra(self):
        self.__palavra_secreta = random.choice(self.__palavras).upper()
        self.__letras_descobertas = ['_'] * len(self.__palavra_secreta)
        self.__tentativas = 6
        self.__letras_erradas = []

    def __exibir_status(self):
        print("\nPalavra: ", ' '.join(self.__letras_descobertas))
        print(f"Tentativas restantes: {self.__tentativas}")
        print(f"Letras erradas: {', '.join(self.__letras_erradas)}")

    def __verificar_letra(self, letra):
        if letra in self.__palavra_secreta:
            for index, char in enumerate(self.__palavra_secreta):
                if char == letra:
                    self.__letras_descobertas[index] = letra
        else:
            self.__tentativas -= 1
            self.__letras_erradas.append(letra)

    def iniciar(self):
        self.__escolher_palavra()
        print("Bem-vindo ao Jogo da Forca! Tema: Times de Futebol")
        
        while self.__tentativas > 0 and '_' in self.__letras_descobertas:
            self.__exibir_status()
            letra = input("Digite uma letra: ").strip().upper()
            if len(letra) != 1 or not letra.isalpha():
                print("Entrada inválida. Tente novamente.")
                continue

            if letra in self.__letras_descobertas or letra in self.__letras_erradas:
                print("Você já tentou essa letra. Tente outra.")
                continue

            self.__verificar_letra(letra)

        if '_' not in self.__letras_descobertas:
            print("\nParabéns! Você venceu!")
            print("A palavra era:", self.__palavra_secreta)
        else:
            print("\nVocê perdeu. Suas tentativas acabaram.")
            print("A palavra era:", self.__palavra_secreta)

class GerenciadorDePalavras:
    """Classe para gerenciar as palavras do jogo."""
    def __init__(self, caminho):
        self.__caminho = caminho
        self.__dados = ArquivoHandler.carregar_dados(self.__caminho)

    def adicionar_palavra(self, palavra):
        if palavra.upper() not in self.__dados.get("palavras", []):
            self.__dados.setdefault("palavras", []).append(palavra.upper())
            ArquivoHandler.salvar_dados(self.__caminho, self.__dados)

    def obter_palavras(self):
        return self.__dados.get("palavras", [])

if __name__ == "__main__":
    caminho_arquivo = "palavras.json"
    gerenciador = GerenciadorDePalavras(caminho_arquivo)

    # Adicionar times do Brasileirão Série A 2024
    times_brasileirao_2024 = [
        "Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional",
        "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Vasco da Gama",
        "Vitória", "Atlético Mineiro", "Fluminense", "Grêmio", "Cuiabá",
        "Red Bull Bragantino", "Santos", "Goiás", "Athletico Paranaense",
        "Criciúma"
    ]

    for time in times_brasileirao_2024:
        gerenciador.adicionar_palavra(time)

    while True:
        palavras = gerenciador.obter_palavras()
        jogo = JogoDaForca(palavras)
        jogo.iniciar()
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até a próxima.")
            break
