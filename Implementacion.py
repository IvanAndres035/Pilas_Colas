from Pilas import *
def main():

    miPila = PilaDinamica()
    miPila.Insertar(30)
    miPila.Insertar(40)
    print(miPila.tamPila())
    return 0

if __name__=='__main__':
    main()