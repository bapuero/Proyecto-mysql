print ("Resultados de PyMySQL:")
import pymysql
miConexion = pymysql.connect(host='127.0.0.1', user= 'root', password='Spartaco07', database='Proyecto')
cur = miConexion.cursor()
numero = input("Eliga una opcion: ")
while(numero in ["1", "2", "3", "4"]):
    if numero == "1":
        cur.execute("INSERT INTO cliente (IDcliente, Nombre_C, Direccion, Dinero) VALUES(527498160, 'Bruno', 'VillaClub', 50);")
        cur.execute("SELECT Nombre_C FROM cliente WHERE Direccion = 'VillaClub';")
        for Nombre_C in cur.fetchall():
            print(Nombre_C)
        cur.execute("UPDATE cliente SET Direccion = 'LaJoya' WHERE IDcliente = 527498160;")
        cur.execute("SELECT Nombre_C FROM cliente WHERE Direccion = 'LaJoya';")
        print()
        for Nombre_C in cur.fetchall():
            print(Nombre_C)
        cur.execute("DELETE FROM cliente WHERE IDcliente = 527498160;")
        numero = input("Eliga una opcion: ")
    if numero == "2":
        cur.execute("INSERT INTO ebanista (IDebanista, Direccion, Bosquejo) VALUES(876543212, 'VillaClub', null);")
        cur.execute("UPDATE ebanista SET calificacion = 6 WHERE IDebanista = 876543212;")
        cur.execute("SELECT direccion FROM ebanista WHERE calificacion = 6;")
        for direccion in cur.fetchall():
            print(direccion)
        cur.execute("DELETE FROM ebanista WHERE IDebanista = 876543212;")
        numero = input("Eliga una opcion: ")
    if numero == "3":
        cur.execute("INSERT INTO pedido (IDcliente, Tipo_madera, Objeto) VALUES(098765432, 'Roble', 'Cama');")
        cur.execute("UPDATE pedido SET Color_madera = 'Negro' WHERE IDcliente = 098765432 AND Objeto = 'Cama';")
        cur.execute("SELECT Objeto FROM pedido WHERE Color_madera = 'Negro';")
        for Objeto in cur.fetchall():
            print(Objeto)
        cur.execute("DELETE FROM pedido WHERE (IDcliente = 098765432 AND Objeto = 'Cama');")
        numero = input("Eliga una opcion: ")
    if numero == "4":
        cur.execute("INSERT INTO factura (IDcliente, IDebanista, Dinero, Fecha_entrega) VALUES(987654321, 432109877, 25, '2020-08-08');")
        cur.execute("UPDATE factura SET IDebanista = '765432100' WHERE codigo = 12;")
        cur.execute("SELECT IDebanista, count(*) AS Total FROM factura GROUP BY IDebanista;")
        for IDebanista, Total in cur.fetchall():
            print(IDebanista, Total)
        cur.execute("DELETE FROM factura WHERE codigo = 12;")
        numero = input("Eliga una opcion: ")
miConexion.close()
