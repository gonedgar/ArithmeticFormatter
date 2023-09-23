def determinar_espacios(espacio:int, guion = False):
    a = ""
    for i in range(espacio):
        if guion == True:
            a = a + "-"
        else:
            a = a + " "
    return a
        

def arithmetic_arranger(operaciones:list, resultado = False):
    
    if len(operaciones) > 5:
        return print("Error: Too many problems.")
    
    elementos = []
    for item in operaciones:
        a = item.split()
        
        # Si los números no contienen solo dígitos
        try:
            int(a[0])
            int(a[2])
        except:
            return print("Error: Numbers must only contain digits.")
        
        # Si los números contienen más de 4 dígitos
        if len(a[0]) > 4 or len(a[2]) > 4:
            return print("Error: Numbers cannot be more than four digits.")
        
        if not a[1] == "+" and not a[1] == '-':
            return print("Error: Operator must be '+' or '-'.")
        # Se determinan los espacios a[3] a dejar
        # Se determina la posición a[4]: 0, los dos números son iguales; 1, el de arriba es mayor; 2, el de abajo es mayor
        # Se determina el tamaño total a[5]
        x = len(a[0]) - len(a[2])
        if x == 0:
            a.append(x)
            a.append(0)
            a.append(len(a[0]) + 2)
        elif x > 0:
            a.append(x)
            a.append(1)
            a.append(len(a[0]) + 2)
        elif x < 0:
            a.append((x * -1))
            a.append(2)
            a.append(len(a[2]) + 2)
        
        elementos.append(a)
    
    # Strings para concatenar los caracteres junto con los espacios para después imprimirlos
    linea1 = ""
    linea2 = ""
    linea3 = ""
    
    # Aquí se recorre cada item lista de la lista elementos y se colocan espacios dependiendo cuál número sea mayor
    # También se pone el signo de la operación y se hace la linea3 que es para los guiones debajo de cada operación
    for item in elementos:
        if item[4] == 0:
            linea1 = linea1 + '  ' + item[0]
            linea2 = linea2 + item[1] + ' ' + item[2]
        elif item[4] == 1:
            linea1 = linea1 + '  ' + item[0]
            linea2 = linea2 + item[1] + ' ' + determinar_espacios(item[3]) + item[2]
        elif item[4] == 2:
            linea1 = linea1 + '  ' + determinar_espacios(item[3]) + item[0]
            linea2 = linea2 + item[1] + ' ' + item[2]
        linea1 = linea1 + '    '
        linea2 = linea2 + '    '
        linea3 = linea3 + determinar_espacios(item[5],True) + '    '    
    
    # Se imprimen las 3 líneas para mostrar las operaciones en terminal
    print(linea1)
    print(linea2)
    print(linea3)
    
    # Si se llamó a la función con True como segundo argumento, entonces se calculan los resultados y se muestran en una línea nueva
    if resultado == True:
        resultados = ""
        total = 0
        for item in elementos:
            if item[1] == '+':
                total = int(item[0]) + int(item[2])
            elif item[1] == '-':
                total = int(item[0]) - int(item[2])
            resultados = resultados + determinar_espacios(item[5]-len(str(total))) + str(total) + '    '
        print(resultados)