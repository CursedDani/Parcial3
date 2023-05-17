Nil = None #representación clásica de None
def Cons(x, xs): #representación clásica de celda --> Node
  return (x,xs) #tupla --> inmutable
  
#devuelve la cabeza de la celda
def head(xs):
  return xs[0]

#devuelve la cola de la celda
def tail(xs):
  return xs[1]

#define si la celda está vacía
def isEmpty(xs):
  return xs is Nil

def consecutive(xs):
    if xs:
        if tail(xs):
            if head(tail(xs)) == head(xs)+1:
                return True
            else:
                return consecutive(tail(xs))
        else:
           return False
    else:
      return False
    
a = Cons(1,Cons(3,Cons(4,Nil)))

b = Cons(4,Cons(8,Cons(23,Cons(0,Nil))))

print(consecutive(a))
print (consecutive(b))
