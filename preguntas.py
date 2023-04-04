"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    
    sum = 0
    for dato in datosPreparados:
        sum += int(dato[1])
    return sum


def pregunta_02():
    
    listasUwu = []
    listasUwunt = []
    for dato in datosPreparados:
        letra = dato[0]
        if letra in listasUwu:
            val = listasUwu.index(letra)
            listasUwunt[val] += 1
        else:
            listasUwu.append(letra)
            listasUwunt.append(1)

    lista = list(zip(listasUwu, listasUwunt))
    return sorted(lista, key=lambda tup: tup[0])


def pregunta_03():
    
    listasUwu = []
    listasUwunt = []
    for dato in datosPreparados:
        letra = dato[0]
        if letra in listasUwu:
            val = listasUwu.index(letra)
            listasUwunt[val] += int(dato[1])
        else:
            listasUwu.append(letra)
            listasUwunt.append(int(dato[1]))

    lista = list(zip(listasUwu, listasUwunt))
    return sorted(lista, key=lambda tup: tup[0])


def pregunta_04():
    
    listasUwu = []
    listasUwunt = []
    for dato in datosPreparados:
        fecha = dato[2].split('-')
        mes = fecha[1]
        if mes in listasUwu:
            val = listasUwu.index(mes)
            listasUwunt[val] += 1
        else:
            listasUwu.append(mes)
            listasUwunt.append(1)
    lista = list(zip(listasUwu, listasUwunt))
    return sorted(lista, key=lambda tup: tup[0])


def pregunta_05():
    
    listasUwu = []
    listaT = []
    listaMax = []
    listaMin = []

    for dato in datosPreparados:
        letra = dato[0]
        if letra in listasUwu:
            val = listasUwu.index(letra)
            listaT[val].append(int(dato[1]))
        else:
            listasUwu.append(letra)
            listaT.append([int(dato[1])])
    for ele in listaT:
        listaMax.append(max(ele))
        listaMin.append(min(ele))

    lista = list(zip(listasUwu, listaMax, listaMin))
    return sorted(lista, key=lambda tup: tup[0])


def pregunta_06():
    
    listasUwu = []
    listaT = []
    listaMax = []
    listaMin = []

    for dato in datosPreparados:
        res = []
        for sub in dato[4].split(','):

            if ':' in sub:
                res.append(map(str.strip, sub.split(':', 1)))

        res = dict(res)
        for k in res.keys():
            letra = k
            if letra in listasUwu:
                val = listasUwu.index(letra)
                listaT[val].append(int(res[k]))
            else:
                listasUwu.append(letra)
                listaT.append([int(res[k])])

    for ele in listaT:
        listaMax.append(max(ele))
        listaMin.append(min(ele))

    lista = list(zip(listasUwu, listaMin, listaMax))
    return sorted(lista, key=lambda tup: tup[0])


def pregunta_07():
    
    listasUwu = []
    listasUwunt = []
    for dato in datosPreparados:
        num = int(dato[1])
        if num in listasUwu:
            val = listasUwu.index(num)
            listasUwunt[val].append(dato[0])
        else:
            listasUwu.append(num)
            listasUwunt.append([dato[0]])

    lista = list(zip(listasUwu, listasUwunt))
    return sorted(lista, key=lambda tup: tup[0])


def pregunta_08():
    
    listasUwu = []
    listasUwunt = []
    for dato in datosPreparados:
        num = int(dato[1])
        if num in listasUwu:
            val = listasUwu.index(num)
            if not dato[0] in listasUwunt[val]:
                listasUwunt[val].append(dato[0])
        else:
            listasUwu.append(num)
            listasUwunt.append([dato[0]])

    for l in listasUwunt:
        l = l.sort()

    lista = list(zip(listasUwu, listasUwunt))
    return sorted(lista, key=lambda tup: tup[0])


def pregunta_09():
    
    listasUwu = []
    listaT = []
    listasUwunt = []

    for dato in datosPreparados:
        res = []
        for sub in dato[4].split(','):

            if ':' in sub:
                res.append(map(str.strip, sub.split(':', 1)))

        res = dict(res)
        for k in res.keys():
            letra = k
            if letra in listasUwu:
                val = listasUwu.index(letra)
                listaT[val].append(int(res[k]))
            else:
                listasUwu.append(letra)
                listaT.append([int(res[k])])

    for ele in listaT:
        listasUwunt.append(len(ele))
    lista = dict(zip(listasUwu, listasUwunt))
    return lista


def pregunta_10():

    listasUwu = []
    listaA = []
    listaD = []

    for dato in datosPreparados:
        res = []
        listasUwu.append(dato[0])

        lista = dato[3].split(',')

        listaA.append(len(lista))

        for sub in dato[4].split(','):

            if ':' in sub:
                res.append(map(str.strip, sub.split(':', 1)))

        res = dict(res)

        listaD.append(len(res))

    lista = list(zip(listasUwu, listaA, listaD))
    return lista


def pregunta_11():
    
    dic = {}

    for dato in datosPreparados:
        valor = int(dato[1])
        for letra in dato[3].split(','):
            if letra in dic:
                dic[letra] += valor
            else:
                dic[letra] = valor
    return dic


def pregunta_12():
    
    dic = {}

    for dato in datosPreparados:
        res = []
        letra = dato[0]

        for sub in dato[4].split(','):

            if ':' in sub:
                res.append(map(str.strip, sub.split(':', 1)))

        res = dict(res)
        res = dict([a, int(x)] for a, x in res.items())
        valor = sum(res.values())
        if letra in dic:
            dic[letra] += valor
        else:
            dic[letra] = valor

    return dic
