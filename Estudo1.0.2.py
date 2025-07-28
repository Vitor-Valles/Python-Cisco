"""
LITERAIS: OS DADOS EM SI

• Um **literal** é um valor direto e fixo escrito no código – seu valor é conhecido apenas por ele mesmo.
  Exemplo: 123 é um literal; 'c' não é (por si só, precisa de contexto).

• Tipos comuns de literais em Python:
  - Numéricos: inteiros (ex: 123), ponto flutuante (ex: 3.14)
  - String: sequências de caracteres entre aspas (ex: "Olá", 'Python')
  - Booleanos: True e False
  - Especial: None

• Exemplo:
  print("123")  # Literal de string
  print(123)    # Literal numérico (int)
  # Ambos imprimem "123", mas são diferentes internamente.

• A função print() pode exibir diferentes tipos de literais de forma legível para humanos.
"""

"""
LITERAIS NUMÉRICOS

• Tipos:
  - Inteiros (int): ex: 10, -5, +42
  - Ponto flutuante (float): ex: 2.5, -0.4, 0.0

• Python não aceita vírgula, ponto ou espaço dentro dos números:
  - Incorreto: 1,000 / 1.000 / 1 000
  - Correto: 1000

• Desde o Python 3.6, sublinhados (_) podem ser usados para facilitar leitura:
  - Ex: 1_000_000

• Bases numéricas:
  - Binária (base 2): prefixo `0b` → ex: 0b1010 = 10
  - Octal (base 8): prefixo `0o` → ex: 0o123 = 83
  - Hexadecimal (base 16): prefixo `0x` → ex: 0x123 = 291

• print() converte essas bases para decimal automaticamente.

• Exemplos:
  print(11111111)
  print(11_111_111)
  print(0o123)
  print(0x123)
"""

"""
LITERAIS DE PONTO FLUTUANTE (float)

• Números com parte fracionária: ex: 3.14, 0.0, -0.5

• Use ponto (.) — nunca vírgula — para decimais:
  - Correto: 2.5
  - Incorreto: 2,5

• É possível omitir o zero antes ou depois do ponto:
  - .5 → 0.5
  - 4. → 4.0

• Notação científica:
  - Use `e` ou `E`: base × 10^expoente
  - Ex: 3e3 = 3 × 10³ = 3000.0
  - Ex: 1.6E-35 = 1.6 × 10⁻³⁵

• Python pode exibir automaticamente valores pequenos em notação científica.

• Exemplos:
  print(2.5)
  print(.5)
  print(4.)
  print(3e3)
  print(1.6E-35)
  print(0.0000000000000000000001)  # → 1e-22
"""

"""
STRINGS EM PYTHON

• Strings são usadas para representar texto.

• Devem estar entre aspas:
  - Simples: 'texto'
  - Duplas: "texto"

• Inserindo aspas dentro de strings:
  1. Escape com barra invertida:
     - Ex: print("Ele disse \"Olá\"")
  2. Usar aspas alternadas:
     - Ex: print('Ele disse "Olá"')

• Apóstrofos em strings:
  - Escape: print('I\'m happy.')
  - Alternância: print("I'm happy.")

• Barra invertida (\\) é usada para:
  - \'  \"  \\  \n  \t etc.

• Uma string pode estar vazia:
  - Ex: '' ou ""

• Exemplos:
  print("Olá, mundo!")
  print('Python é "legal"')
  print("Eu sou Monty Python.")
  print("")
"""

"""
VALORES BOOLEANOS

• Booleanos representam verdadeiro ou falso:
  - True
  - False

• São usados para expressar condições:
  - print(4 > 2)  → True
  - print(3 == 5) → False

• Internamente:
  - True = 1
  - False = 0

• Sensível a maiúsculas/minúsculas:
  - Correto: True / False
  - Incorreto: true / FALSE

• Exemplo:
  print(True)
  print(False)
  print(True > False)  # True
  print(True < False)  # False
"""

"""
EXTRA: LITERAL ESPECIAL - None

• Representa "ausência de valor" ou "nada".
• Tipo: NoneType
• Usado como valor padrão em funções, inicializações, etc.

• Exemplo:
  valor = None
  print(valor)  # → None
"""
