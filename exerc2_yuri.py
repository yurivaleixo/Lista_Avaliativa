
def criar_tabuleiro(n):
    """
    Cria um tabuleiro vazio de tamanho n x n.

    Args:
        n (int): O tamanho do tabuleiro (número de linhas e colunas).

    Returns:
        list: Uma lista de listas representando o tabuleiro vazio.
    """
    return [[" " for _ in range(n)] for _ in range(n)]

def mostrar_tabuleiro(tabuleiro):
    """
    Mostra o tabuleiro atual na tela.

    Args:
        tabuleiro (list): O tabuleiro atual representado como uma lista de listas.
    """
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * (4 * len(linha) - 1))

def verificar_ganhador(tabuleiro, jogador, linha, coluna):
    """
    Verifica se um jogador ganhou o jogo.

    Args:
        tabuleiro (list): O tabuleiro atual representado como uma lista de listas.
        jogador (str): O jogador atual ("X" ou "O").
        linha (int): A linha em que a última jogada foi feita.
        coluna (int): A coluna em que a última jogada foi feita.

    Returns:
        bool: True se o jogador ganhou, False caso contrário.
    """
    n = len(tabuleiro)

    def linha_vencedora():
        return all(tabuleiro[linha][i] == jogador for i in range(n))

    def coluna_vencedora():
        return all(tabuleiro[i][coluna] == jogador for i in range(n))

    def diagonal_principal_vencedora():
        return all(tabuleiro[i][i] == jogador for i in range(n))

    def diagonal_secundaria_vencedora():
        return all(tabuleiro[i][n - 1 - i] == jogador for i in range(n))

    return (linha_vencedora() or coluna_vencedora() or 
            diagonal_principal_vencedora() or diagonal_secundaria_vencedora())

def jogar_jogo():
    """
    Função principal que permite aos jogadores jogarem o jogo da velha NxN.
    """
    print("Bem-vindo ao Jogo da Velha NxN!")
    n = int(input("Digite o tamanho do tabuleiro (NxN): "))
    
    tabuleiro = criar_tabuleiro(n)
    jogador_atual = "X"
    total_jogadas = 0
    
    while True:
        mostrar_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}.")
        
        linha = int(input(f"Digite a linha (0 a {n-1}) para {jogador_atual}: "))
        coluna = int(input(f"Digite a coluna (0 a {n-1}) para {jogador_atual}: "))
        
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            total_jogadas += 1
            
            if verificar_ganhador(tabuleiro, jogador_atual, linha, coluna):
                mostrar_tabuleiro(tabuleiro)
                print(f"O jogador {jogador_atual} venceu!")
                break
            elif total_jogadas == n * n:
                mostrar_tabuleiro(tabuleiro)
                print("Empate! O jogo acabou.")
                break
            
            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Essa posição já está ocupada. Tente novamente.")

if __name__ == "__main__":
    jogar_jogo()
