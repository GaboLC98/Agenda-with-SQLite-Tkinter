from io import open
print(""" █████╗  ██████╗ ███████╗███╗   ██╗██████╗  █████╗ 
██╔══██╗██╔════╝ ██╔════╝████╗  ██║██╔══██╗██╔══██╗
███████║██║  ███╗█████╗  ██╔██╗ ██║██║  ██║███████║
██╔══██║██║   ██║██╔══╝  ██║╚██╗██║██║  ██║██╔══██║
██║  ██║╚██████╔╝███████╗██║ ╚████║██████╔╝██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝""")
def start():
    ficherol=open("Lunes.txt","a")
    ficherom=open("Martes.txt","a")
    ficheromi=open("Miercoles.txt","a")
    ficheroj=open("Jueves.txt","a")
    ficherov=open("Viernes.txt","a")
    ficherol1=open("Lunes.txt","r")
    leer_lunes=ficherol1.readlines()
    ficherol1.close()
    ficherom1=open("Martes.txt","r")
    leer_martes=ficherom1.readlines()
    ficherom1.close()
    ficheromi1=open("Miercoles.txt","r")
    leer_miercoles=ficheromi1.readlines()
    ficheromi1.close()
    ficheroj1=open("Jueves.txt","r")
    leer_jueves=ficheroj1.readlines()
    ficheroj1.close()
    ficherov1=open("Viernes.txt","r")
    leer_viernes=ficherov1.readlines()
    ficherov1.close()
    opcion=int(input("\nSeleccione el nro de accion a realizar:\n1-Agregar a la agenda\n2-Eliminar de la agenda\n3-Ver agenda\n-----> "))
    while opcion:
        if opcion==1:
            dia_op1=int(input("¿A que dia desea agregar una tarea?\n1-Lunes\n2-Martes\n3-Miercoles\n4-Jueves\n5-Viernes\n"))
            tarea=input("Ingrese la tarea con la fecha de entrega: ")
            if dia_op1==1:
                ficherol.write(tarea+"\n")
                ficherol.close()
            elif dia_op1==2:
                ficherom.write(tarea+"\n")
                ficherom.close()
            elif dia_op1==3:
                ficheromi.write(tarea+"\n")
                ficheromi.close()
            elif dia_op1==4:
                ficheroj.write(tarea+"\n")
                ficheroj.close()
            elif dia_op1==5:
                ficherov.write(tarea+"\n")
                ficherov.close()
            else:
                print("Opcion incorrecta, vuelva a intentarlo")
            start()
        elif opcion==2:
            def del_line():
                for line in lineas:
                    if line!=leer_lunes[eliminar]:
                        fichero.write(line)
                fichero.close()
                start()
            numero=int(input("En que dia desea eliminar:\n1-Lunes\n2-Martes\n3-Miercoles\n4-Jueves\n5-Viernes\n-----> "))
            if numero==1:
                print(f"TAREAS: {leer_lunes}")                
                fichero=open("Lunes.txt","w")
                lineas=leer_lunes
            elif numero==2:
                print(f"TAREAS: {leer_martes}")
                fichero=open("Martes.txt","w")
                lineas=leer_miercoles             
            elif numero==3:
                print(f"TAREAS: {leer_miercoles}")
                fichero=open("Miercoles.txt","w")
                lineas=leer_jueves               
            elif numero==4:
                print(f"TAREAS: {leer_jueves}")
                fichero=open("Jueves.txt","w")
                lineas=leer_viernes               
            elif numero==5:
                print(f"TAREAS: {leer_viernes}")
                fichero=open("Viernes.txt","w")
                lineas=leer_viernes
            else:
                print("Opcion incorrecta, vuelva a intentarlo")
                start()
            eliminar=int(input("¿Que tarea desea eliminar? (nros del 0 a n) ------> "))
            del_line()     
        elif opcion==3:
            print(f"LUNES: {leer_lunes}\nMARTES: {leer_martes}\nMIERCOLES: {leer_miercoles}\nJUEVES: {leer_jueves}\nVIERNES: {leer_viernes} ")
            start()
        else:
            print("Opcion incorrecta, vuelva a intentarlo") 
            start()
start()
