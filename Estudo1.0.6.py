"""
INTERAÇÃO COM O USUÁRIO: input() E CONVERSÕES DE TIPO

• A função input() permite que o usuário digite dados no console e retorna esse valor como uma *string*.
• Diferente da função print(), que apenas exibe dados, input() *coleta* dados.

=======================
input() sem argumento
-----------------------
- Uso básico: input() lê uma entrada do usuário.
- Exemplo:
    print("Conta-me qualquer coisa...")
    anything = input()
    print("Hum...", anything, "...Realmente?")
- O programa pausa esperando a entrada e só continua após o usuário apertar Enter.
- O valor retornado *deve* ser salvo em uma variável — se não, será perdido.

=======================
input() com argumento
-----------------------
- Você pode passar uma mensagem para input(), tornando o código mais limpo:
    anything = input("Conta-me qualquer coisa...")
    print("Hum...", anything, "...Realmente?")

=======================
Resultado de input() é sempre string
-----------------------
- Mesmo que o usuário digite números, o valor retornado será uma string.
- Isso impede operações aritméticas diretas, como:
    anything = input("Digite um número: ")
    something = anything ** 2.0  # ERRO! TypeError

=======================
Operações Proibidas com input()
-----------------------
- Tentar usar operadores matemáticos com strings causa erro:
    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'

=======================
Conversão de tipos com int() e float()
-----------------------
- Para usar os dados numericamente, converta a string usando:
    • int(string): converte para número inteiro.
    • float(string): converte para número decimal.
- Exemplo:
    value = float(input("Digite um número: "))
    print("Quadrado:", value ** 2)

=======================
Hipotenusa com input()
-----------------------
- input(), int() e float() juntos permitem programas interativos com números.
- Exemplo:
    a = float(input("Comprimento do cateto A: "))
    b = float(input("Comprimento do cateto B: "))
    print("Hipotenusa =", (a ** 2 + b ** 2) ** 0.5)
- A variável intermediária pode ser omitida se o valor for usado diretamente no print().

=======================
Operadores de string: + e *
-----------------------
• `+` concatena strings:
    "Hello" + "World" → "HelloWorld"
    - Não é comutativo: "ab" + "ba" ≠ "ba" + "ab"
    - Ambos os lados devem ser strings.

• `*` replica strings:
    "Hi" * 3 → "HiHiHi"
    - Funciona com string * número ou número * string.
    - Se o número for ≤ 0, o resultado é uma string vazia.

=======================
Conversão str()
-----------------------
• A função str() converte números em strings:
    str(3.14) → "3.14"
    - Muito útil para exibir resultados com print() como string concatenada:
        print("Resultado: " + str(valor))
    - Essa conversão é sempre possível e segura.

=======================

Resumo: input(), strings e interatividade

1. A função print() envia dados para o console.
   A função input() **obtém** dados do console (entrada do usuário).

2. input() pode receber um argumento opcional (prompt):
   Exibe uma mensagem antes do usuário digitar algo:
       name = input("Digite seu nome: ")
       print("Olá, " + name + ". Prazer em conhecê-lo!")

3. Quando input() é chamada:
   - O programa pausa até o usuário inserir um valor e apertar Enter.
   - O console entra em “modo de entrada”.
   - O cursor pisca aguardando a digitação.

   Obs: No ambiente Edube, o tempo de execução é limitado (alguns segundos).
   Para testar o comportamento completo (como pausa indefinida até a entrada), 
   use sua máquina local (ex: IDLE, terminal Python, VSCode...).

   Exemplo prático:
       name = input("Digite seu nome: ")
       print("Olá, " + name + ". Prazer em conhecê-lo!")

       print("\nPressione Enter para finalizar o programa.")
       input()
       print("O FIM.")

4. O resultado de input() é sempre uma **string**.
   - Ao usar o operador `+`, ocorre **concatenação** (junção de strings).
       Exemplo:
           num_1 = input("Digite o primeiro número: ")  # Ex: 12
           num_2 = input("Digite o segundo número: ")   # Ex: 21
           print(num_1 + num_2)  # Saída: 1221 (não 33)

5. Também é possível usar o operador `*` para **replicação de strings**:
       my_input = input("Digite algo: ")  # Ex: Olá
       print(my_input * 3)                # Saída: OláOláOlá

Resumo geral:
-------------
• input() torna o programa interativo.
• Sempre retorna string → é preciso converter se quiser realizar cálculos.
• Operadores + e * têm uso específico para strings:
   + → concatenação
   * → replicação



"""
