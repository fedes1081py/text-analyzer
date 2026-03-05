def convertir_lista(texto):
    texto_split = texto.split(" ")
    return texto_split

def contar_palabras(lista):
    contador = 0
    for word in lista:
        contador+=1
    return contador

def contar_letras(text):
    contador = 0
    for char in text:
        if not char == " ":
            contador +=1
    return contador

def palabra_mas_larga(lista):
    palabra = ""
    pivot = 0
    for word in lista:
        cantidad = contar_letras(word)
        if  cantidad > pivot:
            palabra = word
            pivot = cantidad

    return palabra

def contar_vocales(texto):
    vocales = 'aeiou'
    contador = 0
    for char in texto:
        if char in vocales:
            contador+=1
    return contador

def pedir_texto():
    while True:
        texto = input("Decime el texto: ")
        if not texto.strip():
            print("Texto vacio intenta de nuevo")
        else:
            return texto

def analizar_texto():
    texto = pedir_texto()
    vocales_contadas = contar_vocales(texto)
    letras_contadas = contar_letras(texto)
    texto_en_lista = convertir_lista(texto)
    palabra_larga = palabra_mas_larga(texto_en_lista)
    palabras_contadas = contar_palabras(texto_en_lista)

    print(f"El texto {texto} \n Tiene {vocales_contadas} vocales contadas\nTiene {letras_contadas} letras contadas\nTiene {palabras_contadas} palabras contadas\nLa palabra mas larga es {palabra_larga} ")




    
    
analizar_texto()