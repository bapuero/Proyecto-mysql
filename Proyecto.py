print ("Resultados de PyMySQL:")
import pymysql
miConexion = pymysql.connect(host='127.0.0.1', user= 'root', password='Spartaco07', database='Proyecto')
cur = miConexion.cursor()
numero = input("Eliga una opcion: ")
while(numero in ["1", "2", "3", "4"]):
    if numero == "1":
        '''Ingresar un nuevo cliente con su id, nombre, direccion y dinero'''
        cur.execute("INSERT INTO cliente (IDcliente, Nombre_C, Direccion, Dinero) VALUES(527498160, 'Bruno', 'VillaClub', 50);")
        '''Consultar a el nombre de los clientes que viven en "VillaClub"'''
        cur.execute("SELECT Nombre_C FROM cliente WHERE Direccion = 'VillaClub';")
        for Nombre_C in cur.fetchall():
            print(Nombre_C)
        '''Actualizar la direccion del cliente ingresado'''
        cur.execute("UPDATE cliente SET Direccion = 'LaJoya' WHERE IDcliente = 527498160;")
        '''Consultar a el nombre de los clientes que viven en "LaJoya"'''
        cur.execute("SELECT Nombre_C FROM cliente WHERE Direccion = 'LaJoya';")
        print()
        for Nombre_C in cur.fetchall():
            print(Nombre_C)
        '''Eliminar al cliente recien registrado'''
        cur.execute("DELETE FROM cliente WHERE IDcliente = 527498160;")
        numero = input("Eliga una opcion: ")
    if numero == "2":
        '''Ingresar un nuevo ebanista con su id, direccion y bosquejo'''
        cur.execute("INSERT INTO ebanista (IDebanista, Direccion, Bosquejo) VALUES(876543212, 'VillaClub', null);")
        '''Actualizar la calificacion del ebanista recien registrado'''
        cur.execute("UPDATE ebanista SET calificacion = 6 WHERE IDebanista = 876543212;")
        '''Mostrar las direcciones de los ebanistas que tiene una calificacion de 6'''
        cur.execute("SELECT direccion FROM ebanista WHERE calificacion = 6;")
        for direccion in cur.fetchall():
            print(direccion)
        '''Eliminar al ebanista recien registrado'''
        cur.execute("DELETE FROM ebanista WHERE IDebanista = 876543212;")
        numero = input("Eliga una opcion: ")
    if numero == "3":
        '''Ingresar un nuevo pedido con su idcliente, tipo de madera y objeto a realizar'''
        cur.execute("INSERT INTO pedido (IDcliente, Tipo_madera, Objeto) VALUES(098765432, 'Roble', 'Cama');")
        '''Actualizar el color del nuevo pedido'''
        cur.execute("UPDATE pedido SET Color_madera = 'Negro' WHERE IDcliente = 098765432 AND Objeto = 'Cama';")
        '''Mostrar los objetos que tienen el color de madera "Negro"'''
        cur.execute("SELECT Objeto FROM pedido WHERE Color_madera = 'Negro';")
        for Objeto in cur.fetchall():
            print(Objeto)
        '''Eliminar el pedido recien registrado'''
        cur.execute("DELETE FROM pedido WHERE (IDcliente = 098765432 AND Objeto = 'Cama');")
        numero = input("Eliga una opcion: ")
    if numero == "4":
        '''Ingresar una nueva factura con su idcliente, idebanista, dinero, fecha de entrega'''
        cur.execute("INSERT INTO factura (IDcliente, IDebanista, Dinero, Fecha_entrega) VALUES(987654321, 432109877, 25, '2020-08-08');")
        '''Actualizar al ebanista de una factura'''
        cur.execute("UPDATE factura SET IDebanista = '765432100' WHERE codigo = 12;")
        '''Mostrar a los ebanistas con su total de factura'''
        cur.execute("SELECT IDebanista, count(*) AS Total FROM factura GROUP BY IDebanista;")
        for IDebanista, Total in cur.fetchall():
            print(IDebanista, Total)
        '''Eliminar la factura recien registrado'''
        cur.execute("DELETE FROM factura WHERE codigo = 12;")
        numero = input("Eliga una opcion: ")
miConexion.close()
