import funciones as fn
print('BIENVENIDO A MASCOTA SEGURA')
print("")
while True:
    fn.menu()
    opc=fn.validar_opcion()
    if opc==1:
        fn.validacion_grabar()
    elif opc==2:
        fn.buscar()
    elif opc==3:
        fn.retirarse()
    else:
        fn.salida()
        break
    
