'''
Print e um nome de função, funções servem para gerar um efeito (Exemplo: enviar uma mensagem no terminal, criar um arquivo, tocar um som etc..)
avaliar um valor (por exemplo, a raiz quadrada de um valor ou o comprimento de um determinado texto) e retorná-lo como resultado da função; é isso que torna as funções do Python parentes de conceitos matemáticos.

ma função em programação pode ter:

    Um efeito (como exibir algo na tela),

    Um resultado (valor retornado),

    E argumentos (valores fornecidos para ela funcionar).
'''


print('Olá Mundo!')

'''
Python não permite o uso de mais de uma instrução na mesma linha exemplo:

print("Exemplo") print("Outro Exemplo")

A Maneira corrta de se fazer isso seria:

print("Exemplo")
print("Outro exemplo")

Ou usando o /n mostrado abaixo
'''
print("Exemplo\nOutro exemplo\n")

'''
O Python sempre executaria de cima para baixo da esquerda para direita e nunca esquecera uma função mesmo que vazia exemplo abaixo:

'''
print("Exemplo")
print("")
print("Outro exemplo")


'''
O que são argumentos de palavra-chave?

São nomes específicos que você passa para funções, junto com um valor, para modificar seu comportamento.
Na função print(), os mais usados são:

    end: o que aparece no final da linha.

    sep: o que aparece entre os valores impressos.

'''
print("Olá", "mundo", sep="-", end="!")

'''
Explicação:

    sep="-" → o separador entre os valores é um hífen.

    end="!" → a linha termina com um ponto de exclamação, em vez da quebra de linha (\n).

Outros exemplos:
'''

print("Meu nome é", end=" ")
print("Monty Python.\n")

print("Meu", "nome", "é", "Monty", "Python.", sep="-") 

print("\nMeu", "nome", "é", sep="_",end=">>>")
print("Monty Python.") 

'''
Regras importantes:

    Os argumentos sep e end devem vir depois dos valores normais (posicionais) da função.

    O valor pode ser qualquer string, inclusive vazia ("").

    A função print() por padrão usa sep=" " e end="\n" (espaço como separador e nova linha ao final).
'''

print(" ____________________"*2)
print(" |                  |"*2)
print(" |                  |"*2)
print(" |                  |"*2)
print(" |                  |"*2)
print(" |                  |"*2)
print(" ____________________"*2)

"""
Resumo – Função print() e argumentos em Python

1. A função print() é interna do Python e exibe mensagens no console.
2. Funções incorporadas (como print(), len(), type()) estão sempre disponíveis.
3. Para chamar uma função, use seu nome seguido de parênteses:
   Ex: print("Olá", "mundo") – argumentos separados por vírgula.
   Um print() vazio imprime uma linha em branco.
4. Strings em Python podem usar aspas simples ('') ou duplas ("").
5. Programas são compostos por instruções, como comandos de exibição com print().
6. A barra invertida (\) indica caracteres especiais, como \n (nova linha).
7. Argumentos posicionais têm significado pela ordem em que aparecem.
8. Argumentos de palavra-chave usam nomes explícitos, como end= ou sep=.
9. Na função print(), use:
   - sep="..." para definir o separador entre valores. Ex: sep="-"
   - end="..." para definir o que imprimir no final. Ex: end=">>>"
"""


