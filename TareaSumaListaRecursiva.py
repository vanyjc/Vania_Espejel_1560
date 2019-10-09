def suma_lista(lista):
    if len(lista)==1:
        return lista[0]
    else:
        value = lista[len(lista)-1] 
        lista.pop(len(lista)-1)
        return value + suma_lista(lista)
    
def main():
    l = [3,5,2,4]
    print(suma_lista(l))
main()
