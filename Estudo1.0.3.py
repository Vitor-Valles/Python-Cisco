"""
PYTHON COMO CALCULADORA

• A função print() pode exibir resultados de expressões matemáticas, como:
  print(2 + 2)  # → 4

• Isso significa que o Python pode ser usado como uma calculadora — funcional, embora não de bolso.

• Estamos entrando no mundo das expressões e operadores.
"""
"""
OPERADORES BÁSICOS EM PYTHON

• Operadores aritméticos mais comuns:
  +   → adição
  -   → subtração
  *   → multiplicação
  /   → divisão (sempre float)
  //  → divisão inteira (arredonda para baixo)
  %   → módulo (resto da divisão)
  **  → exponenciação

• Literal + operador = expressão.
"""
"""
EXPONENCIAÇÃO (**)

• Exemplo:
  print(2 ** 3)  # → 8

• Regras:
  - int ** int → int
  - float em qualquer operando → resultado será float

• Ex:
  print(2 ** 3.0)  # → 8.0
"""
"""
MULTIPLICAÇÃO (*)

• Multiplica dois valores:
  print(3 * 2)  # → 6
  print(3.0 * 2)  # → 6.0 (float)

• Preserva a regra int/float.
"""
"""
DIVISÃO (/)

• Sempre retorna float:
  print(4 / 2)   # → 2.0
  print(1 / 2)   # → 0.5

• Mesmo quando resultado parece inteiro: ainda é float.
"""
"""
DIVISÃO INTEIRA (//)

• Resultado sem parte decimal:
  print(5 // 2)    # → 2
  print(5.0 // 2)  # → 2.0

• Arredondamento sempre "para baixo":
  print(-3 // 2)   # → -2
  print(-3.0 // 2) # → -2.0

• Também chamada de floor division.
"""
"""
MÓDULO (%)

• Retorna o RESTO da divisão:
  print(14 % 4)     # → 2

• Lógica:
  14 // 4 = 3
  3 * 4 = 12
  14 - 12 = 2 → resultado

• Pode usar float:
  print(12 % 4.5)   # → 3.0
"""
"""
DIVISÃO POR ZERO

• Irá causar erro:
  - print(1 / 0)
  - print(1 // 0)
  - print(1 % 0)

• NUNCA divida por zero.
"""
"""
ADIÇÃO (+)

• Soma dois valores:
  print(2 + 3)  # → 5
"""
"""
SUBTRAÇÃO (-) | OPERADORES UNÁRIOS E BINÁRIOS

• Subtração (binária): dois operandos.
  print(5 - 2)  # → 3

• Negação (unária): um operando.
  print(-3)    # → -3

• Também existe + unário (sem efeito prático):
  print(+3)    # → 3
"""
"""
PRIORIDADE DOS OPERADORES

• Operadores têm prioridades diferentes, que determinam a ordem da execução:
  Ex: 2 + 3 * 5  → resultado: 17 (multiplica primeiro)

• Tabela resumida de prioridades:
  1. **              (exponenciação)
  2. +x, -x          (unários)
  3. *, /, //, %     (multiplicação e divisões)
  4. +, -            (adição e subtração)

• Parênteses mudam a ordem natural:
  print((2 + 3) * 5)  # → 25
"""
"""
LIGAÇÃO (ASSOCIATIVIDADE)

• Operadores com mesma prioridade são avaliados da ESQUERDA para a DIREITA (ligação à esquerda),
  exceto ** (exponenciação), que é da DIREITA para a ESQUERDA.

• Exemplo:
  print(9 % 6 % 2)    # → 1  (ligação à esquerda)
  print(2 ** 2 ** 3)  # → 256 (ligação à direita → 2 ** (2 ** 3))

• Cuidado com:
  print(-3 ** 2)      # → -9
  print(-(3 ** 2))    # → -9
  print((-3) ** 2)    # → 9
"""
"""
RESUMO FINAL

• EXPRESSÕES: combinação de dados, operadores e funções → produz valor.
• OPERADORES:
  - Unários: atuam sobre 1 operando (ex: -x)
  - Binários: atuam sobre 2 operandos (ex: x + y)
• PRINCIPAIS OPERADORES ARITMÉTICOS:
  +   → adição
  -   → subtração
  *   → multiplicação
  /   → divisão com float
  //  → divisão inteira
  %   → módulo (resto)
  **  → exponenciação
• PRIORIDADES:
  1. **
  2. +x, -x
  3. *, /, //, %
  4. +, -
• EXPRESSÕES COM PARÊNTESIS são avaliadas primeiro.
• Exceção: ** é o único com ligação à direita.
"""
