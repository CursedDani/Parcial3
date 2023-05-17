
from functools import reduce
def operacionesMatriz(m:list)->int:
    def operacion(char):
        def suma(x,y):
            return x+y
        def mult(x,y):
            return x*y
        if char == '+':
            return suma
        elif char=='*':
            return mult
    
    def extraerFilas(i=0,j=0):
        if j>= len(m) or i%2==0:
            return extraerFilas(i+1,0)
        
        if i>=len(m):
            return []
        
        return [m[i][j]] + extraerFilas(i,j+1)
    

    def extraerColumnas(i=0,j=0):
        if i>=len(m) or j%2==0:
            return extraerColumnas(0,j+1)
        if j>=len(m):
            return []
        
        return [m[i][j]] + extraerColumnas(i+1,j)
    s = operacion('+')
    m = operacion('*')
    sumatoria = reduce(lambda x,y:x+y,extraerFilas,0)
    productoria = reduce(lambda x,y:x*y,extraerColumnas,1)

    return sumatoria-productoria

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]


print(operacionesMatriz(matriz))
