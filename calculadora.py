print('Calculadora basica de dois numeros')

print('1. Adição')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')
print('5. Sair')

escolha_operação = int(input('Escolha uma operação: ')) 

numero1 = int(input('Entre com o numero1: ')) 
numero2 = int(input('Entre com o numero2: ')) 


def soma():
    soma = numero1 + numero2 
    print(f'O resultado é: {soma}')

def subtracao():
    subtracao = numero1 - numero2
    print(f'O resultado é: {subtracao}')

def multiplicao():
    multiplicao = numero1 * numero2
    print(f'O resultado é: {multiplicao}')

def divisao():
    divisao = numero1 / numero2
    print(f'O resultado é: {divisao}')    

if escolha_operação == 1: 
    soma() 
elif escolha_operação == 2: 
    subtracao()  
elif escolha_operação == 3: 
    multiplicao() 
elif escolha_operação == 4: 
    divisao()  
elif escolha_operação == 5: 
   print('Sair')  
else: 
    ('Opção invalida')       
    