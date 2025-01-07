# Jogo da Forca - Times do Brasileirão 2024

Este projeto implementa um jogo da forca em Python com o tema "Times do Brasileirão 2024". Ele utiliza conceitos de programação orientada a objetos (POO) e manipulação de arquivos JSON para gerenciar palavras.

## Estrutura do Código

O código é dividido em várias classes que encapsulam funcionalidades específicas:

### 1. **ArquivoHandler**
Classe utilitária para manipular arquivos JSON:
- `salvar_dados`: Salva dados no formato JSON.
- `carregar_dados`: Carrega dados de um arquivo JSON.

### 2. **JogoBase**
Uma classe abstrata que define a estrutura de um jogo genérico por meio do método `iniciar`.

### 3. **JogoDaForca**
Implementa a lógica do jogo da forca:
- Gerencia a escolha da palavra secreta, as tentativas, letras descobertas e erradas.
- Exibe o status do jogo, verifica letras inseridas pelo jogador e determina vitória ou derrota.

### 4. **GerenciadorDePalavras**
Gerencia a lista de palavras usadas no jogo:
- `adicionar_palavra`: Adiciona uma palavra ao arquivo JSON.
- `obter_palavras`: Retorna as palavras disponíveis.

## Como o Código Funciona

1. **Carregamento de Palavras**  
   As palavras são armazenadas em um arquivo `palavras.json`. Caso o arquivo não exista, ele será criado e preenchido com os times do Brasileirão Série A de 2024.

2. **Inicialização do Jogo**  
   O jogo escolhe uma palavra aleatoriamente da lista carregada. O jogador tem 5 tentativas para adivinhar a palavra, sendo informado sobre letras erradas e o progresso atual.

3. **Interação do Usuário**  
   Durante cada rodada, o jogador insere uma letra. O jogo valida a entrada e atualiza o status conforme necessário.

4. **Finalização**  
   Após acertar ou esgotar as tentativas, o jogador é informado do resultado e pode escolher jogar novamente.

## Executando o Jogo

1. Certifique-se de ter o Python 3 instalado.
2. Salve o código em um arquivo chamado `Jogo_Forca.py`.
3. Execute o arquivo no terminal:
   ```bash
   python Jogo_Forca.py
   ```

## Customizações

- **Adicionar Novas Palavras**  
  Você pode editar diretamente o arquivo `palavras.json` ou modificar o método `adicionar_palavra` para incluir palavras dinamicamente.

- **Alterar o Tema**  
  Para mudar o tema do jogo, basta substituir as palavras carregadas no arquivo `palavras.json` por outras relacionadas ao tema desejado.

## Requisitos

- Python 3.7 ou superior
- Biblioteca `json` (inclusa no Python padrão)

## Recursos Implementados

- Organização modular usando POO.
- Persistência de dados com arquivos JSON.
- Validação e feedback ao jogador.
- Gerenciamento de palavras dinâmico.



