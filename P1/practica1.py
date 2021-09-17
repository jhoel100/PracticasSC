def intercambiar1(datos):
    respuesta=[]
    for i in datos:
        aux=""
        for j in i:
            if(j=='j'):
                aux=aux+'i'
            else:
                if(j=='h'):
                    aux=aux+'i'
                else:
                    if(j=='ñ'):
                        aux=aux+'n'
                    else:
                        if(j=='k'):
                            aux=aux+'l'
                        else:
                            if(j=='u'):
                                aux=aux+'v'
                            else:
                                if(j=='w'):
                                    aux=aux+'v'
                                else:
                                    if(j=='y'):
                                        aux=aux+'z'
                                    else:
                                        aux=aux+j
        respuesta.append(aux)
    return respuesta

def intercambiar2(datos):
    respuesta=[]
    for i in datos:
        aux=""
        for j in i:
            if(j=='á'):
                aux=aux+'a'
            else:
                if(j=='é'):
                    aux=aux+'e'
                else:
                    if(j=='í'):
                        aux=aux+'i'
                    else:
                        if(j=='ó'):
                            aux=aux+'o'
                        else:
                            if(j=='ú'):
                                aux=aux+'u'
                            else:
                                aux=aux+j
        respuesta.append(aux)
    return respuesta

def intercambiar3(datos):
    respuesta=[]
    for i in datos: 
        respuesta.append(i.upper())
    return respuesta

def intercambiar4(datos):
    respuesta=[]
    for i in datos:
        aux=""
        for j in i:
            if(j!=' ' and j!=',' and j!=';' and j!='?' and j!='¿' and j!='!' and j!='¡' and j!='(' and j!=')' and j!='"' and j!=':' and j!='.' ):
                aux=aux+j
        respuesta.append(aux)
    return respuesta

def frecuencia(datos):
    respuesta=[0]*26
    for i in datos:
        for j in i:
            respuesta[ord(j)-65]=respuesta[ord(j)-65]+1
    indices=[]
    for i in range(26):
        indices.append(chr(i+65))

    dicc=dict(zip(indices,respuesta))
    
    res={k: v for k, v in sorted(dicc.items(), key=lambda item: item[1],reverse=True)}
    
    return res


def convUTF8(datos):
    respuesta=[]
    for i in datos:
        aux=""
        for j in i:
            aux=aux+str(ord(j))
        respuesta.append(aux)
    return respuesta

def insertarAQUI(datos):
    respuesta=[]
    con=0
    for i in datos:
        aux=""
        for j in i:
            aux=aux+j
            con=con+1
            if(con%20==0):
                aux=aux+"AQUI"
        respuesta.append(aux)
    residuo=con%4
    if(residuo!=0):
        respuesta[len(respuesta)-1]=respuesta[len(respuesta)-1]+"X"*(4-residuo)
    
    return respuesta

def triagramas(texto):
    triagramas = []
    #separamos en grupos de 3
    for indice, c in enumerate(texto):
      if (indice == len(texto)-3):
        break
      sequencia = texto[indice] + texto[indice+1] + texto[indice+2]
      triagramas.append(sequencia)
    
    #contamos las veces que se repite cada triagrama
    frecTriang = {}
    for trigram in triagramas:
      frecTriang[trigram] = texto.count(trigram)
    
    #armamos un diccionario con las frecuencias ordenadas  
    frecTriang = {k: v for k, v in sorted(frecTriang.items(), key=lambda item: item[1], reverse=True)}
    
    frec_triang = {}
    
    #imprimimos los 15 traiagrams con mas frecuencia
    i = 0
    for k, v in frecTriang.items():
      if i == 15:
        break
      frec_triang[k] = v
      print(k, v)
      i += 1
    return frec_triang

def frecuencias(texto,frec_triang):
    frec_triang_indice = {}
    #creamos un diccionario con los indices
    for k in frec_triang.keys():
      frec_triang_indice[k] = [i for i in range(len(texto)) if texto.startswith(k, i)]
    
    #creamos un diccionario con los delta
    frec_triang_deltas = {}
    for k, v in frec_triang_indice.items():
      t = []
      for i in range(len(frec_triang_indice[k])-1):
        t.append(frec_triang_indice[k][i+1]-frec_triang_indice[k][i])
      frec_triang_deltas[k] = t
    print(frec_triang_indice)
    print("")
    print(frec_triang_deltas)



entrada = open("texto.txt", "r",encoding='utf8')

salida = open("HERALDOSNEGROS_pre.txt", "w")


datos=[]
lineas = entrada.readlines()
for linea in lineas:
	datos.append(linea.strip('\n'))

print("Datos Iniciales: ")
print(datos)
print("")
print("Los datos modificados son: ")
respuesta=intercambiar4(intercambiar3(intercambiar2(intercambiar1(datos))))
print(respuesta)
print(" ")
print("La tabla de frecuencia es:")
freqs=frecuencia(respuesta)

i = 0
for k, v in freqs.items():
  if i == 5:
    break
  print(k, v)
  i += 1
print(freqs)
print("")
print("La conversion a valores UTF es: ")
print(convUTF8(respuesta))
print("")
print("La insercion de AQUI y las X son: ")
print(insertarAQUI(datos))
print("")
texto=""
for i in respuesta:
    salida.writelines(i+'\n')
    texto=texto+i

print("Los triagramas son: ")
frec_triang=triagramas(texto)
print("")
print("Las frecuencias son: ")
frecuencias(texto,frec_triang)

entrada.close()
salida.close()