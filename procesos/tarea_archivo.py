def leer():
    archivo = open("file.txt", "r")
    print(archivo.read() + "\n")
    archivo.close()

    main()

def escribir():
    archivo = open("file.txt", "w")
    texto = input("Escriba lo que desee introducir: ")
    archivo.write(texto)
    archivo.close()
    archivo = open("file.txt", "r")
    print(archivo.read())
    archivo.close()

    main()

def main():
    print("Elija entre las siguientes opciones: \n 1) Leer el archivo \n 2) Escribir en el archivo")
    opcion = input()
    if opcion == "1":
        leer()
    elif opcion == "2":
        escribir()

    else:
        main()

main()
