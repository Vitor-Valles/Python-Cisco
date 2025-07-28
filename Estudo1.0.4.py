"""
==============================
Variáveis (Python)
==============================

O que são variáveis?

- Variáveis são "caixas" que armazenam valores (números, textos, etc.).
- Cada variável tem:
    • Um nome (identificador)
    • Um valor (conteúdo que pode mudar)
- Permitem guardar resultados intermediários para usar depois.
- Exemplo:
    resultado = 2 + 2
    print(resultado)

Regras para nomes de variáveis

- Devem começar com letra (a-z ou A-Z) ou _
- Podem conter letras, números e _
- Python diferencia maiúsculas de minúsculas (ex: `idade` ≠ `Idade`)
- Não podem usar palavras-chave (reservadas) do Python como `if`, `import`, `def`, etc.

Exemplos válidos:
    nome, idade_2, altura_cm, preçoTotal, días_útiles

Exemplos inválidos:
    1nome, minha idade, if, !variável

- Convenção PEP8:
    • minúsculas com _ entre palavras → exemplo: `total_maçãs`
    • nomes claros, concisos e legíveis

Como criar variáveis

- Basta usar `nome = valor`
- Python cria a variável automaticamente ao atribuir pela primeira vez
- Exemplo:
    nome = "João"
    idade = 30

- Tipagem dinâmica: a variável pode mudar de tipo em tempo de execução
    idade = 30
    idade = "trinta"  # agora é uma string

Como usar variáveis

- Você pode usar variáveis dentro de expressões e funções como `print()`
- Mas: usar variável antes de definir gera erro

Exemplo:
    a = 10
    print("Valor de a:", a)

    print(b)  # ERRO: b não foi definida ainda

- Combinar texto e variáveis:
    versao = "3.11"
    print("Versão Python: " + versao)

Atribuindo novo valor

- Basta usar novamente `=`
- Exemplo:
    x = 5
    x = x + 1  # Agora x vale 6

- Isso é diferente da matemática! Aqui `=` significa "atribuir", e não "igual a".

Resolver problemas com variáveis

- Você pode usar variáveis para armazenar valores em fórmulas

Exemplo: Teorema de Pitágoras
    a = 3
    b = 4
    c = (a**2 + b**2) ** 0.5
    print("c =", c)  # Resultado: 5.0

Operadores de atalho (shortcuts)

- Em vez de escrever: x = x + 1
- Pode usar: x += 1
- Outros exemplos:
    • x *= 2
    • x /= 5
    • x -= 3
    • x %= 4

Padrão:
    variável op= expressão
    → equivale a: variável = variável op expressão

RESUMO

- Variáveis guardam dados com nome
- Criadas automaticamente quando você faz `nome = valor`
- Regras de nome:
    • Letras, números, _
    • Não podem começar com número
    • Sensíveis a maiúsculas
    • Não usar palavras-chave

- Operador de atribuição (=) define valor
- Operadores compostos: +=, -=, *=, etc.
- Tipagem dinâmica: não precisa declarar tipo antes
- Usar `print()` para exibir valores e combinar com textos
    Exemplo: print("Resultado:", var)


"""
