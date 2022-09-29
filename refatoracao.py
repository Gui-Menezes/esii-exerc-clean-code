def definicaoDeFasesDaVida(idade):
    if idade < 14:
        resultado =  "Criança"
    elif idade < 18:
        resultado = "Adolecente"
    elif idade < 65:
        resultado = "Adulto"
    else:
        resultado = "Idoso"

    return resultado

def imprimirFaseDaVida(valor):
    print(f"{seuNome}, você é {valor}")

# programa principal
seuNome  = input("Digite seu nome: ")
suaIdade = int(input("Digite sua idade: ") )

imprimirFaseDaVida(definicaoDeFasesDaVida(suaIdade))