import pandas
import os
import openpyxl

funciones = [["1", "Facilitar el uso de un computador"], ["2", "Abstraer el hardware del computador"],
             ["3", "Administrar los recursos del computador"], ["4", "Administrar las tareas del computador"],
             ["5", "Administrar los archivos del computador"]]

archivoxlsx = "archivo.xlsx"


def imprimirTXT():
    os.remove("archivo.txt")
    archivotxt = open("archivo.txt", "a")
    for i in range(5):
        archivotxt.write(str(i + 1) + ") " + funciones[i][1] + "\n")
    archivotxt.close()


def imprimirXSLX():
    df = pandas.DataFrame(data=funciones, columns=["Numero", "Función"])
    with pandas.ExcelWriter("archivo.xlsx") as writer:
        df.to_excel(writer)
        print(df)


imprimirTXT()
imprimirXSLX()
