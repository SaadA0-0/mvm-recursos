import sys

matriz = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'K'],
    ['L', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']
]

# Agafem el text a xifrar de l'argument i el manipulem per treballar amb ell
arguments = sys.argv
frase = " ".join(arguments[1:])
frase = frase.upper()
frase = frase.replace('J', 'I')
frase = frase.replace('Ñ', 'N')
#frase = " ".join(sys.argv[1:]).upper().replace('J', 'I').replace('Ñ', 'N')
resultado = ""

for caracter in frase:
    if caracter == " ":
        resultado += "  "
    else:
        for f in range(5):
            for c in range(5):
                if matriz[f][c] == caracter:
                    resultado += f"{f+1}{c+1}"

print(resultado)