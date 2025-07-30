"""
INTRODUÇÃO À FUNÇÃO print() EM PYTHON

Seu primeiro programa:
• O primeiro programa em Python costuma ser: print("Olá, Mundo!")
• Elementos: nome da função `print`, parênteses, aspas e o texto a ser impresso.
• Esse código deve ser executado no console ou em um arquivo `.py`.

A função print():
• `print()` é uma função incorporada ao Python, usada para exibir dados no console.
• Funções podem causar efeitos (como mostrar algo na tela) ou retornar valores.
• `print()` causa um efeito (imprimir), mas **não retorna valores úteis**.

Argumentos de função:
• As funções Python podem ter zero, um ou mais argumentos.
• Os argumentos são colocados entre parênteses.
• No caso do `print()`, seu argumento é uma **string** (texto entre aspas).

Chamada de função:
• Uma chamada de função tem o formato: `nome_da_função(argumento)`.
• O Python:
  1. Verifica se o nome da função existe.
  2. Verifica se os argumentos são válidos.
  3. Executa a função.
  4. Volta para continuar o código após a execução da função.

Efeitos, argumentos e retorno do print():
• Efeito: mostra o que for passado como argumento.
• Aceita praticamente qualquer tipo de argumento (string, número, booleano, etc).
• Retorno: `None` (não retorna valor útil).

Instruções:
• Cada linha em Python deve conter **apenas uma instrução**.
• Várias chamadas de `print()` mostram várias linhas no console.
• Chamadas vazias como `print()` geram uma **linha em branco**.

Escape e nova linha (\n):
• `\n` é um caractere especial que **cria uma nova linha** dentro da string.
• A barra invertida (`\`) inicia uma sequência de escape.
• Para exibir uma barra invertida literal, use `\\`.

Vários argumentos no print():
• Ex: `print("Olá", "Python")` — múltiplos argumentos são separados por vírgulas.
• O `print()` insere automaticamente **espaços entre os argumentos**.

Argumentos posicionais:
• A ordem dos argumentos importa.
• Exemplo: `print("A", "B")` imprime A antes de B.

Argumentos de palavra-chave:
• `print()` aceita dois argumentos especiais:
  - `sep="..."` → muda o separador entre os argumentos (padrão é espaço).
  - `end="..."` → muda o que aparece no fim da impressão (padrão é nova linha).
• Ex: 
    print("A", "B", sep="-", end="!") → saída: A-B!
• Pode-se usar ambos juntos, respeitando a ordem: argumentos posicionais primeiro, depois os nomeados.

RESUMO GERAL:
• `print()` → função interna usada para mostrar mensagens no console.
• Funções internas não precisam ser importadas.
• `print()` pode receber múltiplos argumentos e formatá-los com `sep` e `end`.
• Strings são delimitadas por "aspas duplas" ou 'aspas simples'.
• Caracteres de escape como `\n` produzem efeitos especiais nas strings.
• Instruções são comandos executados linha a linha.
"""
