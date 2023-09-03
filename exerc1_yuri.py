# Função para criar um tabuleiro 4x4 
def criar_tabuleiro_quatro_por_quatro():
    return [[" " for _ in range(4)] for _ in range(4)]

# Função para exibir o tabuleiro 4x4 
def mostrar_tabuleiro_4x4(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))  # Mostra a linha do tabuleiro com barras verticais 
        print("-" * (7 * len(linha) - 1))  # Cria uma linha horizontal

# Função para verificar se um jogador venceu na posição atual
def verificar_vitoria_quatro_por_quatro(tabuleiro, jogador, linha, coluna):
    
    if all(tabuleiro[linha][i] == jogador for i in range(4)):
        return True
    
   
    if all(tabuleiro[i][coluna] == jogador for i in range(4)):
        return True
    
    
    if all(tabuleiro[i][i] == jogador for i in range(4)):
        return True
    
    
    if all(tabuleiro[i][3 - i] == jogador for i in range(4)):
        return True
    
    return False

# Função principal 
def jogar_jogo_da_velha_4x4():
    print("Bem-vindo ao Jogo da Velha!")

    tabuleiro = criar_tabuleiro_quatro_por_quatro()  # Inicializa o tabuleiro vazio
    jogador_atual = "X" 

    for _ in range(16):  # Loop para alternar entre os jogadores (16 jogadas no total)
        mostrar_tabuleiro_4x4(tabuleiro) 
        print(f"É a vez do jogador {jogador_atual}.")

        while True:
            linha = int(input("Digite a linha (0 a 3): "))  # Solicita a linha da jogada
            coluna = int(input("Digite a coluna (0 a 3): "))  # Solicita a coluna da jogada

            # Verifica se a jogada é válida (dentro dos limites do tabuleiro e a célula não está ocupada)
            if 0 <= linha < 4 and 0 <= coluna < 4 and tabuleiro[linha][coluna] == " ":
                break  # Sai do loop se a jogada for válida
            else:
                print("Posição inválida. Tente novamente!")

        tabuleiro[linha][coluna] = jogador_atual  # Atualiza o tabuleiro com a jogada do jogador

        # Verifica se o jogador da vez venceu usando a função verificar_vitoria_quatro_por_quatro()
        if verificar_vitoria_quatro_por_quatro(tabuleiro, jogador_atual, linha, coluna):
            mostrar_tabuleiro_4x4(tabuleiro)  # Apresenta o tabuleiro final
            print(f"O jogador {jogador_atual} venceu! Parabéns!!!")
            break  

        jogador_atual = "O" if jogador_atual == "X" else "X"  

    else:
        mostrar_tabuleiro_4x4(tabuleiro) 
        print("Deu empate!")

if __name__ == "__main__":
    jogar_jogo_da_velha_4x4()
