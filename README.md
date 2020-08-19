print ("Resultados de PyMySQL:")
import pymysql
miConexion = pymysql.connect(host='127.0.0.1', user= 'root', password='Spartaco07', database='Proyecto')
cur = miConexion.cursor()
numero = input("Eliga una opcion: ")
while(numero in ["1", "2", "3", "4"]):
    if numero == "1":
        cur.execute("ALTER TABLE cliente MODIFY telefono INT DEFAULT NULL;")
        cur.execute("INSERT INTO cliente (IDcliente, Nombre_C, Direccion, Dinero) VALUES(527498160, 'Bruno', 'VillaClub', 50);")
        cur.execute("SELECT IDcliente, Nombre_C, Direccion, Telefono, Dinero FROM cliente;")
        for IDcliente, Nombre_C, Direccion, Telefono, Dinero in cur.fetchall():
            print(IDcliente, Nombre_C, Direccion, Telefono, Dinero)
        cur.execute("DELETE FROM cliente WHERE IDcliente = 527498160;")
        cur.execute("SELECT IDcliente, Nombre_C, Direccion, Telefono, Dinero FROM cliente;")
        print()
        for IDcliente, Nombre_C, Direccion, Telefono, Dinero in cur.fetchall():
            print(IDcliente, Nombre_C, Direccion, Telefono, Dinero)
        numero = input("Eliga una opcion: ")
    if numero == "2":
        cur.execute("ALTER TABLE ebanista MODIFY calificacion INT DEFAULT NULL;")
        cur.execute("INSERT INTO ebanista (IDebanista, Direccion) VALUES(876543212, 'VillaClub');")
        cur.execute("SELECT IDebanista, calificacion, direccion, bosquejo FROM ebanista;")
        for IDebanista, calificacion, direccion, bosquejo in cur.fetchall():
            print(IDebanista, calificacion, direccion, bosquejo)
        cur.execute("DELETE FROM ebanista WHERE IDebanista = 876543212;")
        cur.execute("SELECT IDebanista, calificacion, direccion, bosquejo FROM ebanista;")
        print()
        for IDebanista, calificacion, direccion, bosquejo in cur.fetchall():
            print(IDebanista, calificacion, direccion, bosquejo)
        numero = input("Eliga una opcion: ")
    if numero == "3":
        cur.execute("ALTER TABLE pedido MODIFY Color_madera VARCHAR(50) DEFAULT 'Cafe';")
        cur.execute("INSERT INTO pedido (IDcliente, Tipo_madera, Objeto) VALUES(098765432, 'Roble', 'Cama');")
        cur.execute("SELECT IDcliente, Tipo_madera, Color_madera, Objeto, Bosquejo FROM pedido;")
        for IDcliente, Tipo_madera, Color_madera, Objeto, Bosquejo in cur.fetchall():
            print(IDcliente, Tipo_madera, Color_madera, Objeto, Bosquejo)
        cur.execute("DELETE FROM pedido WHERE (IDcliente = 098765432 AND Objeto = 'Cama');")
        cur.execute("SELECT IDcliente, Tipo_madera, Color_madera, Objeto, Bosquejo FROM pedido;")
        print()
        for IDcliente, Tipo_madera, Color_madera, Objeto, Bosquejo in cur.fetchall():
            print(IDcliente, Tipo_madera, Color_madera, Objeto, Bosquejo)
        numero = input("Eliga una opcion: ")
    if numero == "4":
        cur.execute("ALTER TABLE factura MODIFY codigo INT AUTO_INCREMENT NOT NULL;")
        cur.execute("INSERT INTO factura (IDcliente, IDebanista, Dinero, Fecha_entrega) VALUES(987654321, 432109877, 25, '2020-08-08');")
        cur.execute("SELECT codigo, IDcliente, IDebanista, Dinero, Fecha_Entrega FROM factura;")
        for codigo, IDcliente, IDebanista, Dinero, Fecha_Entrega in cur.fetchall():
            print(codigo, IDcliente, IDebanista, Dinero, Fecha_Entrega)
        cur.execute("DELETE FROM factura WHERE codigo = 11;")
        cur.execute("SELECT codigo, IDcliente, IDebanista, Dinero, Fecha_Entrega FROM factura;")
        print()
        for codigo, IDcliente, IDebanista, Dinero, Fecha_Entrega in cur.fetchall():
            print(codigo, IDcliente, IDebanista, Dinero, Fecha_Entrega)
        numero = input("Eliga una opcion: ")
miConexion.close()
