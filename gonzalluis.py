def seRepite(digcombinados,r):
    ''' 
        Dominio:
            Un string que contiene el numerador y denominador
            combinados, ademas de tener los ceros a la izquierda
            si estos son menores a 10000. Y r, que representa
            la cantidad de veces que un digito puede repetirse
        Codominio:
           True o False
           Falso cuando un digito aparece mas de r veces
           True cuando cumple que los digitos aparezcan
           r veces o menos
    '''
    for x in digcombinados:
        if digcombinados.count(x) > r: return False
    return True
def encontrarsolucion(c,r):
    ''' 
        Dominio:
            Dos números enteros, en donde C puede valer 1 a 20 y R 1 a 5
        Codominio:
            Todas las posibles combinaciones en donde A/B = C,
            donde A y B tienen 4 a 5 digitos, y se aparecen R veces o menos
    '''
    for numerador in range(c*1000, 100000,c): 
        denominador = numerador // c
        num_str = str(numerador).zfill(5) 
        den_str = str(denominador).zfill(5)
        if seRepite(num_str + den_str,r): 
            print(f"{numerador}/{denominador}={c}")
t = int(input())
while t:
    t-=1
    c,r = input().split() 
    encontrarsolucion(int(c),int(r))