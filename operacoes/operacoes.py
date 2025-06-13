 # Parte 3: operações matemáticas

def eh_par(n):
    return n % 2 == 0

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    try:
        a = int(input("Digite o primeiro número inteiro: "))
        b = int(input("Digite o segundo número inteiro: "))
    except ValueError:
        print("Por favor, informe números inteiros válidos.")
        return

    # Operações básicas
    print(f"\nSoma:         {a} + {b} = {a + b}")
    print(f"Subtração:   {a} - {b} = {a - b}")
    print(f"Multiplicação: {a} * {b} = {a * b}")
    # Evita divisão por zero
    if b != 0:
        print(f"Divisão:     {a} / {b} = {a / b:.2f}")
    else:
        print("Divisão:     impossível dividir por zero.")

    # Par/ímpar e primo
    for valor, rotulo in [(a, "primeiro"), (b, "segundo")]:
        tipo_par = "par" if eh_par(valor) else "ímpar"
        tipo_primo = "primo" if eh_primo(valor) else "não primo"
        print(f"\nO {rotulo} número ({valor}) é {tipo_par} e {tipo_primo}.")

if __name__ == "__main__":
    main()
