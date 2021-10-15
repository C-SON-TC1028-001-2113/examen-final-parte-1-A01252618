def main():
    num = int(input("Enter a number: "))
    #escribe tu código abajo de esta línea
    contador = len(str(num))

    if contador<=6:
        if num>0:
            n=int(str(num)[::-1])
            print(n)
        elif num<0:
            numero=num*-1
            n=int(str(numero)[::-1])
            m=n*-1
            print(m)
    else:
        print('Too long')
    


if __name__=='__main__':
    main()
