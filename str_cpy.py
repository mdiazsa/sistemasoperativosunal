ef so_strcpy(str1, str2):
    for i in range(len(str1)):
        str2 += str1[i]
        print(str2)
    return str2


def main():
    string1 = "Hola mundo"
    string2 = ""
    string2 = so_strcpy(string1, string2)
    print("El string2 es :", string2)

main()
