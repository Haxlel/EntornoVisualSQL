from pymysql import *

class consultas:

    def __init__(self):
        self.cnn = connect(host="localhost", user="root", 
        passwd="", database="clientes")

    def __str__(self):
        datos=self.consulta_datos()
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
    
    def consulta_datos(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM HOJA1")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def insertar_datos(self,NombreCompleto,
                            FechaDeNacimiento,
                            Direccion,
                            LocalidadyCodigoPostal,
                            Telefono,
                            CorreoElectronico,
                            FechaDeAlta,
                            GrupoDeClientes):
        cur = self.cnn.cursor()
        sql=f'''INSERT INTO hoja1 (`Nombre Completo`,`Fecha De Nacimiento`,`Direccion`,`Localidad y Codigo Postal`,`Telefono`,`Correo Electronico`,`Fecha De Alta`,`Grupo De Clientes`) 
            VALUES('{NombreCompleto}', '{FechaDeNacimiento}', '{Direccion}', '{LocalidadyCodigoPostal}','{Telefono}','{CorreoElectronico}','{FechaDeAlta}','{GrupoDeClientes}')'''
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def eliminar_datos(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM hoja1 WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modificar_datos(self,Id,
                            NombreCompleto,
                            FechaDeNacimiento,
                            Direccion,
                            LocalidadyCodigoPostal,
                            Telefono,
                            CorreoElectronico,
                            FechaDeAlta,
                            GrupoDeClientes):
        
        cur = self.cnn.cursor()
        sql=f'''UPDATE hoja1 SET `Nombre Completo`='{NombreCompleto}',
                                     `Fecha De Nacimiento`='{FechaDeNacimiento}',
                                     `Direccion`='{Direccion}',
                                     `Localidad y Codigo Postal`='{LocalidadyCodigoPostal}',
                                     `Telefono`='{Telefono}',
                                     `Correo Electronico`='{CorreoElectronico}',
                                     `Fecha De Alta`='{FechaDeAlta}',
                                     `Grupo De Clientes`='{GrupoDeClientes}'
                WHERE Id={Id}'''
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def column (self):
        cur = self.cnn.cursor()
        cur.execute(f'SHOW COLUMNS FROM HOJA1')
        data = cur.fetchall()
        cur.close
        lstColumn=[]
        for row in data:
            lstColumn.append(row[0])
        return lstColumn
