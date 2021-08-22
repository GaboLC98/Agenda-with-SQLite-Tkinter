import sqlite3
print(""" █████╗  ██████╗ ███████╗███╗   ██╗██████╗  █████╗ 
██╔══██╗██╔════╝ ██╔════╝████╗  ██║██╔══██╗██╔══██╗
███████║██║  ███╗█████╗  ██╔██╗ ██║██║  ██║███████║
██╔══██║██║   ██║██╔══╝  ██║╚██╗██║██║  ██║██╔══██║
██║  ██║╚██████╔╝███████╗██║ ╚████║██████╔╝██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝""")
conexion=sqlite3.connect("agenda.db")
cursor=conexion.cursor()
def start():
    opcion=int(input("\nSeleccione el nro de accion a realizar:\n1-Agregar a la agenda\n2-Eliminar de la agenda\n3-Ver agenda\n-----> "))
    while opcion:
        if opcion==1:
            dia_op1=int(input("¿A que dia desea agregar una tarea?\n1-Lunes\n2-Martes\n3-Miercoles\n4-Jueves\n5-Viernes\n"))
            tarea=input("Ingrese la tarea: ")
            entrega=input("Ingrese la fecha de entrega: ")
            if dia_op1==1:
                cursor.execute(f'INSERT INTO TAREAS VALUES(NULL,"Lunes","{tarea}","{entrega}")')
            elif dia_op1==2:
                cursor.execute(f'INSERT INTO TAREAS VALUES(NULL,"Martes","{tarea}","{entrega}")')
            elif dia_op1==3:
                cursor.execute(f'INSERT INTO TAREAS VALUES(NULL,"Miercoles","{tarea}","{entrega}")')
            elif dia_op1==4:
                cursor.execute(f'INSERT INTO TAREAS VALUES(NULL,"Jueves","{tarea}","{entrega}")')
            elif dia_op1==5:
                cursor.execute(f'INSERT INTO TAREAS VALUES(NULL,"Viernes","{tarea}","{entrega}")')
            else:
                print("Opcion incorrecta, vuelva a intentarlo\n")
                start()
            conexion.commit()
            start()
        if opcion==2:
            dia_op1=int(input("En que dia desea eliminar:\n1-Lunes\n2-Martes\n3-Miercoles\n4-Jueves\n5-Viernes\n"))
            if dia_op1==1:
                cursor.execute('SELECT * FROM TAREAS WHERE DIA="Lunes"')
            elif dia_op1==2:
                cursor.execute('SELECT * FROM TAREAS WHERE DIA="Martes"')
            elif dia_op1==3:
                cursor.execute('SELECT * FROM TAREAS WHERE DIA="Miercoles"')
            elif dia_op1==4:
                cursor.execute('SELECT * FROM TAREAS WHERE DIA="Jueves"')    
            elif dia_op1==5:
                cursor.execute('SELECT * FROM TAREAS WHERE DIA="Viernes"')   
            else:
                print("Opcion incorrecta, vuelva a intentarlo\n")
                start()
            eliminar=cursor.fetchall()
            print(eliminar)
            id_eliminar=int(input('¿Que tarea desea eliminar? (seleccione la ID)'))
            cursor.execute(f'DELETE FROM TAREAS WHERE ID={id_eliminar}')
            conexion.commit()
            start()
        if opcion==3:
            cursor.execute('SELECT * FROM TAREAS WHERE DIA="Lunes"')
            ver=cursor.fetchall()
            print(f"Lunes:\n{ver}")
            cursor.execute('SELECT * FROM TAREAS WHERE DIA="Martes"')
            ver=cursor.fetchall()
            print(f"Martes:\n{ver}")
            cursor.execute('SELECT * FROM TAREAS WHERE DIA="Mieroles"')
            ver=cursor.fetchall()
            print(f"Miercoles:\n{ver}")
            cursor.execute('SELECT * FROM TAREAS WHERE DIA="Jueves"')
            ver=cursor.fetchall()
            print(f"Jueves:\n{ver}")
            cursor.execute('SELECT * FROM TAREAS WHERE DIA="Mieroles"')
            ver=cursor.fetchall()
            print(f"Viernes:\n{ver}")
            start()
start()  
conexion.close()
