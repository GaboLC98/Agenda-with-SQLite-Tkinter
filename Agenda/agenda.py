import sqlite3
from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry("250x200")
root.resizable(0,0)
root.title("Agenda")
root.config(bg="white")
conexion=sqlite3.connect("agenda.db")
cursor=conexion.cursor()
titulo_opciones=Label(root,text="¿Que desea realizar?",font=("Curier 12"),bg="white").pack()

def Agregar(): #Funcion para agregar tareas/cosas para hacer en X dia
    def Guardar_tarea():
        cursor.execute(f'INSERT INTO TAREAS VALUES(NULL,"{dias.get()}","{tarea.get()}","{entrega.get()}")')
        conexion.commit()
        root_agregar.destroy()
    tarea=StringVar()
    entrega=StringVar()
    dias=StringVar()
    root_agregar=Toplevel()
    root_agregar.geometry("500x250")
    root_agregar.config(bg="white")
    Label(root_agregar,text="¿Que tarea quiere agregar?",font=("Curier 10"),bg="white").pack(pady=5)
    Entry(root_agregar,textvariable=tarea,width=30,bd=2).pack()
    Label(root_agregar,text="¿Que dia desea guardar",font=("Curier 10"),bg="white").pack(pady=5)
    dias_op=["Lunes","Martes","Miercoles","Jueves","Viernes"]
    ttk.Combobox(root_agregar,width=27,values=dias_op,textvariable=dias).pack()
    Label(root_agregar,text="¿Que fecha se entrega?",font=("Curier 10"),bg="white").pack(pady=5)
    Entry(root_agregar,textvariable=entrega,width=30,bd=2).pack()
    Button(root_agregar,text="Guardar tarea",font=("Curier 10"),width=15,bg="snow",command=Guardar_tarea).pack(pady=10)

def Eliminar(): #Funcion para eliminar una tarea de un dia
    def Eliminar_commit():
        cursor.execute(f'DELETE FROM TAREAS WHERE ID={id.get()}')
        conexion.commit()
        root_eliminar.destroy()
    root_eliminar=Toplevel()
    root_eliminar.geometry("600x300")
    root_eliminar.config(bg="white")
    id=IntVar()
    cursor.execute('SELECT * FROM TAREAS WHERE DIA="Lunes"')
    ver_lunes=cursor.fetchall()
    cursor.execute('SELECT * FROM TAREAS WHERE DIA="Martes"')
    ver_martes=cursor.fetchall()
    cursor.execute('SELECT * FROM TAREAS WHERE DIA="Mieroles"')
    ver_miercoles=cursor.fetchall()
    cursor.execute('SELECT * FROM TAREAS WHERE DIA="Jueves"')
    ver_jueves=cursor.fetchall()
    cursor.execute('SELECT * FROM TAREAS WHERE DIA="Mieroles"')
    ver_viernes=cursor.fetchall()
    tareas=Listbox(root_eliminar,font=("Curier 10"))
    for i in ver_lunes:
        tareas.insert("anchor",f'ID.{i[0]}. CLASE: {i[1]}, {i[2]}, ENTREGA: {i[3]}')
    for i in ver_martes:
        tareas.insert("anchor",f'ID.{i[0]}. CLASE: {i[1]}, {i[2]}, ENTREGA: {i[3]}')
    for i in ver_miercoles:
        tareas.insert("anchor",f'ID.{i[0]}. CLASE: {i[1]}, {i[2]}, ENTREGA: {i[3]}')
    for i in ver_jueves:
        tareas.insert("anchor",f'ID.{i[0]}. CLASE: {i[1]}, {i[2]}, ENTREGA: {i[3]}')
    for i in ver_viernes:
        tareas.insert("anchor",f'ID.{i[0]}. CLASE: {i[1]}, {i[2]}, ENTREGA: {i[3]}')
    tareas.pack(fill="both")
    Label(root_eliminar,text="¿Que ID de tarea desea eliminar?",font=("Curier 10"),bg="white").pack(pady=10)
    Entry(root_eliminar,textvariable=id,width=30,bg="white",bd=2).pack()
    Button(root_eliminar,text="Eliminar",width=15,bg="snow",font=("Curier 10"),command=Eliminar_commit).pack(pady=10)

def Ver(): #Funcion para ver a lista de tareas. Si no aparece no hay tarea
    root_ver=Toplevel()
    root_ver.geometry("600x600")
    root_ver.config(bg="white")
    cursor.execute('SELECT * FROM TAREAS WHERE DIA="Lunes"')
    ver_lunes=cursor.fetchall()
    cursor.execute('SELECT * FROM TAREAS WHERE DIA="Martes"')
    ver_martes=cursor.fetchall()
    cursor.execute('SELECT * FROM TAREAS WHERE DIA="Mieroles"')
    ver_miercoles=cursor.fetchall()
    cursor.execute('SELECT * FROM TAREAS WHERE DIA="Jueves"')
    ver_jueves=cursor.fetchall()
    cursor.execute('SELECT * FROM TAREAS WHERE DIA="Mieroles"')
    ver_viernes=cursor.fetchall()
    tareas=Listbox(root_ver,font=("Curier 10"))
    for i in ver_lunes:
        tareas.insert("anchor",f'ID.{i[0]}. CLASE: {i[1]}, {i[2]}, ENTREGA: {i[3]}')
    for i in ver_martes:
        tareas.insert("anchor",f'ID.{i[0]}. CLASE: {i[1]}, {i[2]}, ENTREGA: {i[3]}')
    for i in ver_miercoles:
        tareas.insert("anchor",f'ID.{i[0]}. CLASE: {i[1]}, {i[2]}, ENTREGA: {i[3]}')
    for i in ver_jueves:
        tareas.insert("anchor",f'ID.{i[0]}. CLASE: {i[1]}, {i[2]}, ENTREGA: {i[3]}')
    for i in ver_viernes:
        tareas.insert("anchor",f'ID.{i[0]}. CLASE: {i[1]}, {i[2]}, ENTREGA: {i[3]}')
    tareas.pack(fill="both")

f1=Frame(root,bg="white")
add=PhotoImage(file="add.gif")
Label(f1,image=add,bg="white").pack(pady=5,side="left")
Button(f1,text="Agregar tarea",font=("Curier 9"),command=Agregar,width=15,bg="pale green").pack(pady=5,side="right")
f1.pack(pady=5)

f2=Frame(root,bg="white")
delete=PhotoImage(file="del.gif")
Label(f2,image=delete,bg="white",).pack(pady=5,side="left")
Button(f2,text="Eliminar tarea",font=("Curier 9"),width=15,command=Eliminar,bg="tomato").pack(pady=5,side="right")
f2.pack(pady=5)

f3=Frame(root,bg="white")
search=PhotoImage(file="search.gif")
Label(f3,image=search,bg="white").pack(pady=5,side="left")
Button(f3,text="Ver las tareas",font=("Curier 9"),width=15,command=Ver,bg="snow").pack(pady=5,side="right")
f3.pack(pady=5)

root.mainloop()
conexion.close()