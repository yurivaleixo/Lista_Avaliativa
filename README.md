# Lista_Avaliativa

EX1 explicação:

criar_tabuleiro_quatro_por_quatro(): Essa função inicia um tabuleiro vazio, representado como uma grade 4x4 de espaços em branco.

mostrar_tabuleiro_4x4(tabuleiro): O tabuleiro é exibido com linhas e colunas separadas por barras verticais e linhas horizontais.

verificar_vitoria_quatro_por_quatro(tabuleiro, jogador, linha, coluna): Esta função verifica se o jogador atual venceu após a última jogada. Isso é feito ao verificar quatro condições: se todas as casas na linha, coluna, diagonal principal ou diagonal secundária da última jogada pertencem ao mesmo jogador. Se uma dessas condições for verdadeira, a função retorna True, indicando a vitória do jogador.
---------------
EX2 explicação: 

criar_tabuleiro_nxn(tamanho): Cria um tabuleiro vazio com tamanho personalizado, onde n é especificado pelo jogador.

mostrar_tabuleiro(tab): Exibe o tabuleiro de forma visualmente agradável, independentemente do tamanho, com barras verticais e linhas horizontais.

verificar_vitoria(tab, jogador, linha, coluna): Verifica se o jogador atual venceu, checando linha, coluna, diagonal principal e diagonal secundária.
---------------
EX3 explicação:

1. Escolha Aleatória da Palavra:
   - O programa seleciona uma palavra aleatória da lista de palavras `palavras` e a guarda como `palavra_secreta`.
2. Exibição da Palavra Oculta:
   - Esta função mostra a palavra secreta com letras adivinhadas corretamente reveladas e espaços em branco para letras não adivinhadas.
3. Loop Principal do Jogo:
   - Loop controla o jogo, permitindo que o jogador faça tentativas até adivinhar ou usar todas as tentativas.
4. Entrada do Jogador:
   - O jogador insere uma palavra de 5 letras como tentativa, convertida para letras minúsculas.
5. Verificação da Tentativa do Jogador:
   - Verifica se a tentativa do jogador tem exatamente 5 letras.
6. Verificação da Adivinhação do Jogador:
   - Verifica se a tentativa do jogador corresponde à palavra secreta. Se corresponder, o jogador ganha. Caso contrário, mostra letras corretas no lugar errado, no lugar certo, e letras incorretas.
---------------
EX4 explicação:

O código Python permite cadastrar usuários com campos personalizados e imprimir os usuários com várias opções de filtro. Ele usa uma lista chamada banco_usuarios para armazenar os dados dos usuários. 
A função cadastrar_usuario() coleta informações dos usuários e permite adicionar campos personalizados. 
A função imprimir_usuarios() exibe os usuários com base em filtros selecionados, como nome e campos específicos. 
A função main() controla o fluxo do programa, permitindo ao usuário cadastrar novos usuários, imprimir usuários ou encerrar o programa. É uma aplicação simples de gerenciamento de dados de usuários.





