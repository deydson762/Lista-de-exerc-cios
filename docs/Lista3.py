selector = int(input("Digite o número do exercício: "))

# Sequência (entrada,processamento,saída)
if selector == 1:
    print("Exercicio 1")
    num = int(input("Digite um número: "))
    print("O resultado é:", num * 2)

elif selector == 2:
    print("Exercicio 2")
    num = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    print("O resultado é:", num + num2)

elif selector == 3:
    print("Exercicio 3")
    num = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    print("O resultado é:", (num + num2) / 2)

elif selector == 4:
    print("Exercicio 4")
    raio = int(input("Digite o raio do círculo: "))
    print("A area do cículo é:", (raio * raio) * 3.14)

elif selector == 5:
    print("Exercicio 5")
    lado = int(input("Digite o lado do quadrado: "))
    print("O perímetro do quadrado é:", lado * 4)
    print("A area do quadrado é:", lado * lado)

elif selector == 6:
    print("Exercicio 6")
    reais = int(input("Digite o valor em reais: "))
    print("O valor em dólares é:", reais / 5.27)

elif selector == 7:
    print("Exercicio 7")
    idade = int(input("Digite a idade: "))
    print("A idade em dias é", idade * 365)

elif selector == 8:
    print("Exercicio 8")
    base = int(input("Digite o valor da base: "))
    altura = int(input("Digite o valor da altura: "))
    print("A area do triângulo é:", (base * altura) / 2)

elif selector == 9:
    print("Exercicio 9")
    preço = int(input("Digite o preço do produto: "))
    print("O preço com desconto de 10% é:", preço * 0.9)

elif selector == 10:
    print("Exercicio 10")
    prova1 = int(input("Digite a nota da primeira prova: "))
    prova2 = int(input("Digite a nota da segunda prova: "))
    print("A média das provas é:", (prova1 + prova2) / 2)

# Seleção (if, else)
elif selector == 11:
    print("Exercicio 11")
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar!")

elif selector == 12:
    print("Exercicio 12")
    num = int(input("Digite um número: "))
    if num > 0:
        print("O número é positivo")
    elif num < 0:
        print("O número é negativo")
    else:
        print("O número é zero")

elif selector == 13:
    print("Exercicio 13")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if num1 > num2:
        print("O primeiro número é maior")
    elif num2 > num1:
        print("O segundo número é maior")
    else:
        print("Os números são iguais")

elif selector == 14:
    print("Exercicio 14")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    if num1 < num2 and num1 < num3:
        print("O primeiro número é menor")
    elif num2 < num1 and num2 < num3:
        print("O segundo número é menor")
    elif num3 < num1 and num3 < num2:
        print("O terceiro número é menor")
    else:
        print("Os números são iguais")

elif selector == 15:
    print("Exercicio 15")
    idade = int(input("Digite a sua idade: "))
    if idade >= 18:
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")

elif selector == 16:
    print("Exercicio 16")
    nota = int(input("Digite a nota do aluno: "))
    if nota >= 7:
        print("O aluno foi aprovado")
    else:
        print("O aluno foi reprovado")

elif selector == 17:
    print("Exercicio 17")
    num = int(input("Digite um número: "))
    if num >= 1 and num <= 100:
        print("O número está entre 1 e 100")
    else:
        print("O número não está entre 1 e 100")

elif selector == 18:
    print("Exercicio 18")
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        print("O aluno foi aprovado")
    else:
        print("O aluno foi reprovado")

elif selector == 19:
    print("Exercicio 19")
    ano = int(input("Digite o ano: "))
    if ano % 4 == 0:
        print("O ano é bissexto")
    else:
        print("O ano não é bissexto")

elif selector == 20:
    print("Exercicio 20")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if num1 > num2:
        diferenca = num1 - num2
        print(f"A diferença entre os números é: {diferenca}")
    elif num2 > num1:
        diferenca = num2 - num1
        print(f"A diferença entre os números é: {diferenca}")
    else:
        print("Os números são iguais")

# Iteração (while, for)
elif selector == 21:
    print("Exercicio 21")
    for i in range(1, 21):
        print(i)

elif selector == 22:
    print("Exercicio 22")
    i = 20
    while i >= 1:
        print(i)
        i -= 1

elif selector == 23:
    print("Exercicio 23")
    for i in range(2, 51, 2):
        print(i)

elif selector == 24:
    print("Exercicio 24")
    for i in range(1, 31, 2):
        print(i)

elif selector == 25:
    print("Exercicio 25")
    tabuada = int(input("Digite um número de 1 a 10: "))
    for i in range(1, 11):
        print(f"{tabuada} x {i} = {tabuada * i}")

elif selector == 26:
    print("Exercicio 26")
    soma = 0
    for numero in range(1, 101):
        soma += numero
    print(f"A soma dos números de 1 a 100 é: {soma}")

elif selector == 27:
    print("Exercicio 27")
    num = int(input("Digite um número: "))
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    
elif selector == 28:
    print("Exercicio 28")
    n = int(input("Digite um número: "))
    for i in range(1, n + 1):
        print(i, end=" ")

elif selector == 29:
    print("Exercicio 29")
    num = int(input("Digite um número: "))
    print("Múltiplos de 3 antes de", num, ":")
    for i in range(1, num):
        if i % 3 == 0:
            print(i, end=" ")

elif selector == 30:
    print("Exercicio 30")
    num = int(input("Digite um número: "))
    soma = 0
    for i in range(1, num + 1):
        soma += i
    print(f"A soma de 1 até {num} é: {soma}")

# Combinação de seleção e repetição
elif selector == 31:
    print("Exercicio 31")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    num4 = int(input("Digite o quarto número: "))
    num5 = int(input("Digite o quinto número: "))
    maior = num1
    if num2 > maior:
        maior = num2
    if num3 > maior:
        maior = num3
    if num4 > maior:
        maior = num4
    if num5 > maior:
        maior = num5
    print(f"O maior número é: {maior}")

elif selector == 32:
    print("Exercicio 32")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    num4 = int(input("Digite o quarto número: "))
    num5 = int(input("Digite o quinto número: "))
    menor = num1
    if num2 < menor:
        menor = num2
    if num3 < menor:
        menor = num3
    if num4 < menor:
        menor = num4
    if num5 < menor:
        menor = num5
    print(f"O menor número é: {menor}")

elif selector == 33:
    print("Exercicio 33")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    num4 = int(input("Digite o quarto número: "))
    num5 = int(input("Digite o quinto número: "))
    media = (num1 + num2 + num3 + num4 + num5) / 5
    print(f"A média é: {media}")

elif selector == 34:
    print("Exercicio 34")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    num4 = int(input("Digite o quarto número: "))
    num5 = int(input("Digite o quinto número: "))
    num6 = int(input("Digite o sexto número: "))
    num7 = int(input("Digite o sétimo número: "))
    num8 = int(input("Digite o oitavo número: "))
    num9 = int(input("Digite o nono número: "))
    num10 = int(input("Digite o décimo número: "))
    
    numeros = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
    numeros.sort()
    
    print("Números pares digitados em ordem crescente:")
    for num in numeros:
        if num % 2 == 0:
            print(num, end=" ")

elif selector == 35:
    print("Exercicio 35")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    num4 = int(input("Digite o quarto número: "))
    num5 = int(input("Digite o quinto número: "))
    num6 = int(input("Digite o sexto número: "))
    num7 = int(input("Digite o sétimo número: "))
    num8 = int(input("Digite o oitavo número: "))
    num9 = int(input("Digite o nono número: "))
    num10 = int(input("Digite o décimo número: "))
    
    numeros = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
    numeros.sort()
    
    print("Números positivos digitados em ordem crescente:")
    for num in numeros:
        if num > 0:
            print(num, end=" ")

elif selector == 36:
    print("Exercicio 36")
    n = int(input("Digite um número: "))
    for i in range(1, n):
        if i % 2 == 0:
            print(i, end=" ")

elif selector == 37:
    print("Exercicio 37")
    n = int(input("Digite um número: "))
    soma_impares = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            soma_impares += i
    print("Soma dos ímpares é", soma_impares)

elif selector == 38:
    print("Exercicio 38")
    num = int(input("Digite um número: "))
    print("Múltiplos de 7 entre 1 e", num, ":", end=" ")
    for i in range(1, num):
        if i % 7 == 0:
            print(i, end=" ")

elif selector == 39:
    print("Exercicio 39")
    n = int(input("Digite um número: "))
    for i in range(1, n + 1):
        print(f"Tabuada do {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()

elif selector == 40:
    print("Exercicio 40")
    soma = 0
    numero = 1
    while numero != 0:
        numero = int(input("Digite um número: "))
        soma += numero
    print("Soma total:", soma)

# Problemas clássicos de treino
elif selector == 41:
    print("Exercicio 41")
    n = int(input("Digite um número: "))
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    print("Fatorial de", n, "é", fatorial)

elif selector == 42:
    print("Exercicio 42")
    n = int(input("Digite um número: "))
    
    if n == 1:
        print("Sequência Fibonacci: 0")
    elif n == 2:
        print("Sequência Fibonacci: 0, 1")
    else:
        a, b = 0, 1
        print("Sequência Fibonacci:", end=" ")
        print(a, end=", ")
        print(b, end=", ")
        
        for i in range(2, n):
            c = a + b
            print(c, end=", ")
            a, b = b, c
        print()

elif selector == 43:
    print("Exercicio 43")
    n = int(input("Digite um número: "))
    if n <= 0:
        print(f"{n} não é primo")
    elif n == 2:
        print(f"{n} é primo")
    else:
        primo = True
        for i in range(2, n):
            if n % i == 0:
                primo = False
                break
        if primo:
            print(f"{n} é primo")
        else:
            print(f"{n} não é primo")


elif selector == 44:
    print("Exercicio 44")
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    while a != b:
      if a > b:
        a = a - b
      else:
        b = b - a
    print(f"MDC é: {a}")

elif selector == 45:
    print("Exercicio 45")
    n = int(input("Digite um número: "))
    soma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i
    if soma_divisores == n:
        print(f"{n} é perfeito")
    else:
        print(f"{n} não é perfeito")

elif selector == 46:
    print("Exercicio 46")
    n = int(input("Digite um número: "))
    soma_digitos = 0
    while n > 0:
        soma_digitos += n % 10
        n //= 10
    print(f"Soma dos dígitos: {soma_digitos}")

elif selector == 47:
    print("Exercicio 47")
    n = int(input("Digite um número: "))
    numero_invertido = 0
    while n > 0:
        numero_invertido = numero_invertido * 10 + (n % 10)
        n //= 10
    print(f"Número invertido: {numero_invertido}")

elif selector == 48:
    print("Exercicio 48")
    senha_correta = int(input("Defina a senha correta: "))
    tentativa = 0
    
    while True:
        senha = int(input("Digite a senha: "))
        tentativa += 1
        
        if senha == senha_correta:
            print(f"Senha correta! Você acertou na {tentativa}ª tentativa.")
            break
        else:
            print("Senha incorreta. Tente novamente.")

elif selector == 49:
    print("Exercicio 49")
    print("Calculadora Simples")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    opcao = int(input("Escolha a operação (1-4): "))
    
    if opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif opcao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif opcao == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"Resultado: {num1} × {num2} = {resultado}")
    elif opcao == 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {num1} ÷ {num2} = {resultado}")
        else:
            print("Erro: Divisão por zero!")
    else:
        print("Opção inválida!")

elif selector == 50:
    print("Exercicio 50")
    valor = int(input("Digite o valor a sacar: "))
    
    if valor <= 0:
        print("Valor inválido!")
    else:
        print("Notas entregues:")
        if valor >= 100:
            notas100 = valor // 100
            print(f"{notas100} nota(s) de R$ 100")
            valor %= 100
        
        if valor >= 50:
            notas50 = valor // 50
            print(f"{notas50} nota(s) de R$ 50")
            valor %= 50
        
        if valor >= 20:
            notas20 = valor // 20
            print(f"{notas20} nota(s) de R$ 20")
            valor %= 20
        
        if valor >= 10:
            notas10 = valor // 10
            print(f"{notas10} nota(s) de R$ 10")
            valor %= 10
        
        if valor >= 5:
            notas5 = valor // 5
            print(f"{notas5} nota(s) de R$ 5")
            valor %= 5
        
        if valor >= 2:
            notas2 = valor // 2
            print(f"{notas2} nota(s) de R$ 2")
            valor %= 2
        
        if valor == 1:
            print("1 moeda(s) de R$ 1")

else:
    print("Exercicio não encontrado")
