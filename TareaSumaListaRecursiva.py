def suma_lista(lista):
    if len(lista)==1:
        return lista[0]
    else:
        value = lista[len(lista)-1] 
        lista.pop(len(lista)-1)
        return value + suma_lista(lista)
    
def main():
    l = [5,10,15,20,25]
    print(suma_lista(l))
main()
