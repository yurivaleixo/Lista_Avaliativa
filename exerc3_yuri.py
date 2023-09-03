import random

# Lista de palavras para o jogo
palavras = ["carro", "balde", "folha", "mesas", "raios", "marte", "caixa", "livro", "floco", "cacho"]


palavra_secreta = random.choice(palavras)

# numero de tentativas permitidas
tentativas_maximas = 6

# lista de palavras corretas e incorretas
letras_corretas = []
letras_incorretas = []

print("Seja Bem-Vindo!")
print("Tente adivinhar a palavra de 5 letras.")

# Função para exibir a palavra oculta com letras reveladas
def exibir_palavra_oculta(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

# Loop 
while tentativas_maximas > 0:
    palavra_oculta = exibir_palavra_oculta(palavra_secreta, letras_corretas)
    print(f"Palavra atual: {palavra_oculta}")


    if letras_incorretas:
        print(f"Letras incorretas: {', '.join(letras_incorretas)}")

    # Solicita uma tentativa 
    tentativa = input("Digite uma palavra de 5 letras: ").lower()

    # Verifica se a tentativa é válida 
    if len(tentativa) == 5:
        if tentativa == palavra_secreta:
            print("Meus parabéns! Você acertou!")
            break
        else:
            letras_corretas_temp = []
            letras_incorretas_temp = []
            
            # Compara cada letra da tentativa com a palavra secreta
            for i, letra in enumerate(tentativa):
                if letra == palavra_secreta[i]:
                    letras_corretas_temp.append(letra)
                elif letra in palavra_secreta:
                    letras_incorretas_temp.append(letra)

            # Atualiza as listas de letras corretas e incorretas
            letras_corretas += letras_corretas_temp
            letras_incorretas += letras_incorretas_temp
            tentativas_maximas -= 1

            # Printa letras corretas e incorretas
            print(f"Letras corretas no lugar errado: {', '.join(letras_corretas_temp)}")
            print(f"Letras corretas no lugar certo: {', '.join(letras_corretas)}")
            print(f"Letras incorretas: {', '.join(letras_incorretas_temp)}")

    else:
        print("Digite uma palavra de 5 letras válida.")


if tentativas_maximas == 0:
    print(f"Acabou! A palavra correta era: {palavra_secreta}")
