print ("Resultados de PyMySQL:")
import pymysql
miConexion = pymysql.connect(host='127.0.0.1', user='root', password='Spartaco07', database='proyecto')
cur = miConexion.cursor()
print("1.- Realizar un pedido")
print("2.- Seleccionar un pedido")
print("3.- Ingresar la puntuacion")
print("4.- Reportes")
print("5.- Consulta")
print("6.- Busqueda")
numero = input("Eliga una opcion: ")
while(numero in ["1", "2", "3", "4", "5", "6"]):
    if numero == "1":
        codigo = input("Codigo: ")
        idcliente = input("Id cliente:")
        objeto = input("Objeto: ")
        cur.execute("INSERT INTO pedido (codigo, idcliente, objeto) VALUES("+codigo+","+idcliente+",'"+objeto+"');")
        numero = input("Eliga una opcion: ")
    if numero == "2":
        codigo = input("Codigo: ")
        idebanista = input("Id ebanista: ")
        cur.execute("UPDATE pedido SET idebanista = "+idebanista+" where codigo = "+codigo+";")
        cur.execute("SELECT codigo, puntuacion FROM factura where codigo = "+codigo+";")
        for c1, p1 in cur.fetchall():
            print(c1, p1)
        numero = input("Eliga una opcion: ")
    if numero == "3":
        codigo = input("Codigo: ")
        calificacion = input("Puntuacion: ")
        cur.execute("UPDATE factura SET puntuacion = " + calificacion + " where codigo = " + codigo + ";")
        numero = input("Eliga una opcion: ")
    if numero == "4":
        print("1.- Desempeño de ebanista")
        print("2.- Ebanistas faltantes")
        print("3.- Pedidos de clientes")
        print("4.- Clientes faltantes")
        n1 = input("Ingrese una opcion: ")
        if n1 == "1":
            'cur.execute("create view desempeño_ebanista as select idebanista, nombre, avg(puntuacion) as puntuacion, count(*) as trabajos from pedido join factura using (codigo) join ebanista using (idebanista) group by idebanista, nombre order by idebanista;")'
            cur.execute("SELECT idebanista, nombre, puntuacion FROM desempeño_ebanista")
            for idebanista, nombre, puntuacion in cur.fetchall():
                print(idebanista, nombre, puntuacion)
        if n1 == "2":
            'cur.execute("create view ebanistas_faltantes as select idebanista, nombre from ebanista e where not exists (select idebanista from factura join pedido p using (codigo) where e.idebanista = p.idebanista) order by idebanista;")'
            cur.execute("SELECT idebanista, nombre FROM ebanistas_faltantes")
            for idebanista, nombre in cur.fetchall():
                print(idebanista, nombre)
        if n1 == "3":
            'cur.execute("create view pedidos_clientes as select idcliente, nombre, count(codigo) as total from cliente join pedido using (idcliente) join factura using (codigo) group by idcliente, nombre order by idcliente;")'
            cur.execute("SELECT idcliente, nombre, total FROM pedidos_clientes")
            for idcliente, nombre, total in cur.fetchall():
                print(idcliente, nombre, total)
        if n1 == "4":
            'cur.execute("create view faltantes_clientes as select idcliente, nombre from cliente c where not exists (select idcliente from factura join pedido p using (codigo) where c.idcliente = p.idcliente) order by idcliente;")'
            cur.execute("SELECT idcliente, nombre FROM faltantes_clientes")
            for idcliente, nombre in cur.fetchall():
                print(idcliente, nombre)
        numero = input("Eliga una opcion: ")
    if numero == "5":
        print("1.- Informacion de los trabajos del ebanista")
        print("2.- Objetos realizados por ebanistas")
        n2 = input("Ingrese una opcion: ")
        if n2 == "1":
            id = input("Id ebanista: ")
            cur.execute("select idebanista, nombre, objeto, puntuacion from pedido join ebanista using (idebanista) join factura using (codigo) where idebanista = "+id+";")
            for idebanista, nombre, objeto, puntuacion in cur.fetchall():
                print(idebanista, nombre, objeto, puntuacion)
        if n2 == "2":
            objeto = input("Objeto: ")
            cur.execute("select nombre, direccion, calificacion from pedido join ebanista using (idebanista) where objeto = '"+objeto+"';")
            for nombre, direccion, calificacion in cur.fetchall():
                print(nombre, direccion, calificacion)
        numero = input("Eliga una opcion: ")
    if numero == "6":
        print("1.- Direccion")
        print("2.- Calificacion")
        print("3.- Objeto")
        print("4.- Tipo de madera")
        n3 = input("Ingrese una opcion: ")
        if n3 == "1":
            direccion = input("Direccion: ")
            cur.execute("explain select * from cliente where direccion = '"+direccion+"';")
            for i in cur.fetchall():
                print(i)
            cur.execute("explain select * from ebanista where direccion = '" + direccion + "';")
            for i in cur.fetchall():
                print(i)
        if n3 == "2":
            calificacion = input("Calificacion del ebanista: ")
            cur.execute("explain select * from ebanista where calificacion >" + calificacion + ";")
            for i in cur.fetchall():
                print(i)
        if n3 == "3":
            objeto = input("Objeto: ")
            cur.execute("explain select * from pedido where objeto = '"+objeto+"';")
            for i in cur.fetchall():
                print(i)
        if n3 == "4":
            tipo = input("Tipo de madera: ")
            cur.execute("explain select * from pedido where tipo_madera = '" + tipo + "';")
            for i in cur.fetchall():
                print(i)
        numero = input("Eliga una opcion: ")
miConexion.close()
