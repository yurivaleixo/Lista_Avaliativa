# Função para criar um tabuleiro 
def criar_tabuleiro_nxn(tamanho):
    return [[" " for _ in range(tamanho)] for _ in range(tamanho)]

# Função para exibir o tabuleiro 
def mostrar_tabuleiro(tab):
    for linha in tab:
        print(" | ".join(linha))  
        print("-" * (4 * len(linha) - 1))   

# Função para verificar vitória 
def verificar_vitoria(tab, jogador, linha, coluna):
    tamanho = len(tab)
    
    # Verificações de vitória: linha, coluna, diagonal principal e diagonal secundária

def jogar_jogo_da_velha_nxn():
    tamanho = int(input("Digite o tamanho do tabuleiro que deseja: "))
    
    tabuleiro = criar_tabuleiro_nxn(tamanho)
    jogador_atual = "X"
    
    while True:
        mostrar_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}.")
        
        linha = int(input(f"Digite a linha (0 a {tamanho-1}) para {jogador_atual}: "))
        coluna = int(input(f"Digite a coluna (0 a {tamanho-1}) para {jogador_atual}: "))
        
        # Verifica se a jogada é válida e atualiza o tabuleiro

if __name__ == "__main__":
    jogar_jogo_da_velha_nxn() 
