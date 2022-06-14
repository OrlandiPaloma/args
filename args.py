#exemplo1:

def func(*args):
    print(args)

lista = [1,2,3,4,5]
print(*lista)
print(*lista, sep='-') #Sep é utilizado para separar
print()

#exemplo2:

def func(*args): #lembrando que ARGS é uma tupla
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

func(1,2,3,4,5)
print()

#exemplo3:

def func(*args):
    for v in args:
        print(v)

func(8,7,6,5,4)
print()

#exemplo4:

def func(*args):
    print(args)

lista = [10,11,12,13]
func(*lista, 88, 99)
