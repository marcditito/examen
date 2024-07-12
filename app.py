from fun import menu,asignarsalario,clasificar_empleados,estadisticas,reporte_sueldos

op =0
lista=[]
while True:
    
    op = menu()
    if op == 1:
        asignarsalario(lista)
    elif op == 2:
        clasificar_empleados(lista)  
    elif op == 3:
        estadisticas(lista) 
    elif op == 4:
        reporte_sueldos(lista)
    elif op == 5:
        print("Finalizando programa ...")
        print("desarrollado por marco maldonado")
        print("21.562.332-7")
        break
