#codigo python de un arbol de navidad donde demuestra una matriz que esta sumando de 1 a 10#


num=10
for i in range(num):
    print(" "*(num- i- 1)+"*"*(2*i+1))

for n in range(int (num/2)):
    print(" " * int (num - num/4)+ "|" *int (num/2))
print( "feliz navidad amigos")
