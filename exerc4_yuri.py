# Lista para armazenar os dados dos usuários
banco_usuarios = []

# Função para cadastrar um usuário 
def cadastrar_usuario(campos_obrigatorios):
    usuario = {}
    
    for campo in campos_obrigatorios:
        valor = input(f"Digite o valor para '{campo}': ")
        usuario[campo] = valor
    
    while True:
        novo_campo = input("Digite um campo adicional (ou 'sair' para encerrar): ")
        if novo_campo.lower() == 'sair':
            break
        valor = input(f"Digite o valor para '{novo_campo}': ")
        usuario[novo_campo] = valor
    
    banco_usuarios.append(usuario)
    print("Usuário cadastrado!")

# Função para imprimir usuários com opções de filtragem
def imprimir_usuarios(*args, **kwargs):
    opcao = input("Digite a opção:\n1 - Imprimir todos\n2 - Filtrar por nomes\n3 - Filtrar por campos\n4 - Filtrar por nomes e campos\n")
    
    if opcao == '1':
        for usuario in banco_usuarios:
            print(usuario)
    elif opcao == '2':
        nomes = args
        for usuario in banco_usuarios:
            if usuario['nome'] in nomes:
                print(usuario)
    elif opcao == '3':
        campos = kwargs.keys()
        for usuario in banco_usuarios:
            if all(usuario.get(campo) == kwargs[campo] for campo in campos):
                print(usuario)
    elif opcao == '4':
        nomes = args
        campos = kwargs.keys()
        for usuario in banco_usuarios:
            if usuario['nome'] in nomes and all(usuario.get(campo) == kwargs[campo] for campo in campos):
                print(usuario)
    else:
        print("Opção inválida")

# Função principal 
def main():
    campos_obrigatorios = input("Digite os nomes dos campos obrigatórios separados por vírgula: ").split(',')

    while True:
        print("\nMenu:")
        print("1 - Cadastrar usuário")
        print("2 - Imprimir usuários")
        print("0 - Encerrar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_usuario(campos_obrigatorios)
        elif opcao == '2':
            imprimir_usuarios()
        elif opcao == '0':
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
