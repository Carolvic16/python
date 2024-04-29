import os

estrelas = [{'nome':'Sirus', 'constelação':'Cão Maior', 'ativo': True}, 
                {'nome':'Vega', 'constelação':'Lira', 'ativo': False}]

def opcoes_nome():

    print('Estrelass Sistema Solar \n')

    print('1. Cadastrar Estrela')
    print('2. Listar Estrela')
    print('3. Verificar Estrela')
    print('4. Sair\n')

def sair_aplicacao(): 
    os.system('cls')
    print('Fechando')

def voltar_ao_menu():
    input('Digite qualquer tecla \n')
    main()

def opcao_invalida():
    print('Opcao invalida!\n')

    voltar_ao_menu()

def titulo(escolha): 
    os.system('cls')
    print(escolha)
    print()

def cadastrar_estrela(): 
    titulo('Cadastrar Estrela')
    nome_estrela = input('Digite o nome da estrela: ')
    constelacao_estrela = input('Digite a constelação da estrela: ')
    estrelas.append({'nome': nome_estrela, 'constelação': constelacao_estrela, 'ativo': True})
    print(f'A estrela {nome_estrela} foi cadastrada com sucesso')

    voltar_ao_menu()


def listar_estrelas():
    titulo('Listando Estrelas')

    for estrela in estrelas:
     nome_estrela = estrela['nome']
     constelação = estrela ['constelação']
     print(f'. Estrela: {nome_estrela}, Constelação: {constelação} ')
     
    voltar_ao_menu()

def alterar_estado():
    titulo('Alterando estado')
    nome_estrela = input('Qual estrela deseja alterar o estado? ')
    estrela_encontrada = False
     
    for estrela in estrelas:
        if nome_estrela== estrelas['nome']:
            estrela_encontrada = True
            estrelas['ativo'] = not estrelas['ativo']
            mensagem = f'A estrela {estrelas} foi ativado com sucesso' if estrelas['ativo'] else f'A estrela {nome_estrela} foi desativado com sucesso'
            print(mensagem)
            
    if not estrela_encontrada:
        print('A estrela não foi encontrado')

    voltar_ao_menu()

    


def selecione():
    try:
        opcao_selecionada = int(input('Escolha uma opcao: '))
     
     
        if opcao_selecionada == 1:
            cadastrar_estrela()
        elif opcao_selecionada == 2: 
            listar_estrelas()
        elif opcao_selecionada == 3: 
            alterar_estado()
        elif  opcao_selecionada == 4: 
            sair_aplicacao()
        else:
            opcao_invalida()
    except:
        opcao_invalida()



def main (): 
    os.system('cls')
    opcoes_nome()
    selecione()
  

if __name__ == '__main__':
    main()
    

