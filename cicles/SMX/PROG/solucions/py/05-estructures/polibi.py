matriz = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'K'],
    ['L', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']
]

frase = input("Frase a cifrar: ")
frase = frase.upper()
frase = frase.replace('J', 'I')
frase = frase.replace('Ñ', 'N')
resultado = ""

for caracter in frase:
    if caracter == " ":
        resultado += "  "
    else:        
        for f in range(5):
            for c in range(5):
                if matriz[f][c] == caracter:                    
                    resultado += f"{f+1}{c+1}"

print(f"Cifrado: {resultado}")