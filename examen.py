#Modulo que utilizamos para descomprimir archivos
from enum import unique
from zipfile import ZipFile

#Libreria para leer un archivo de excel 
#import openpyxl 
#import xlrd
import pandas as pd

#Libreria para conectar con la bd
import pymysql



#función para descomprimir archivos 
def descomprimir():
    archivozip = "C:\\Users\\omar_\\OneDrive\\Documentos\\examen\\Examen.zip"
    
    with ZipFile(file = archivozip, mode = "r", allowZip64=True) as file:
        archivo = file.open(name = file.namelist()[0], mode =  "r")
        print(archivo.read())
        archivo.close()

        navegacion = "C:\\Users\\omar_\\OneDrive\\Documentos\\examen"
        print("Descomprimiendo archivos...")
        file.extractall(path = navegacion)
        print("Archivo descomprimido")

#Función para leer archivos del archivo -3 2DPEA
def datos1():
        #Leer el archivio

        filePath = "-3 2DPEA.xls"
        hoja = "Sheet1"

        dataFrame1 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="D", header = 2, nrows=0)
        dataFrame1 = dataFrame1.columns.values[0]

        dataFrame2 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="D", header = 3, nrows=0)
        dataFrame2 = dataFrame2.columns.values[0]

        dataFrame3 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="D", header = 4, nrows=0)
        dataFrame3 = dataFrame3.columns.values[0]

        dataFrame4 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="J", header = 2, nrows=0)
        dataFrame4 = dataFrame4.columns.values[0]

        dataFrame5 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 27, nrows=0)
        dataFrame5 = dataFrame5.columns.values[0]

        dataFrame6 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 32, nrows=0)
        dataFrame6 = dataFrame6.columns.values[0]

        dataFrame7 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 49, nrows=0)
        dataFrame7 = dataFrame7.columns.values[0]

        dataFrame8 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 50, nrows=0)
        dataFrame8 = dataFrame8.columns.values[0]

        dataFrame9 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 49, nrows=0)
        dataFrame9 = dataFrame9.columns.values[0]

        dataFrame10 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 50, nrows=0)
        dataFrame10 = dataFrame10.columns.values[0]

        print("\nArchivo: -3 2DPEA.xls")
        print("\nPanel number: ",dataFrame1)
        print("\nJob number: ",dataFrame2)
        print("\nJob name: ",dataFrame3)
        print("\nSeal: ",dataFrame4)
        print("\nType: ",dataFrame5)
        print("\nModbus Id: ",dataFrame6)
        print("\nSerial number: ",dataFrame7, dataFrame8)
        print("\nMeter No.: ",dataFrame9, dataFrame10)
        print("------------------------")

        #Una vez leido los datos los guardamos en nuestra base de datos ya creada
        connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "Omar1998<",
        db = "examen1"
        )

        cursor = connection.cursor()

        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('1', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame7, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame9)
        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('2', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame8, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame10)

        cursor.execute(sql)
        connection.commit()

#Función para leer archivos del archivo -5 6DPEA
def datos2():

    #Leer el archivio

        filePath = "-5 6DPEA.xls"
        hoja = "Sheet1"

        dataFrame1 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="D", header = 2, nrows=0)
        dataFrame1 = dataFrame1.columns.values[0]

        dataFrame2 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="D", header = 3, nrows=0)
        dataFrame2 = dataFrame2.columns.values[0]

        dataFrame3 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="D", header = 4, nrows=0)
        dataFrame3 = dataFrame3.columns.values[0]

        dataFrame4 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="J", header = 2, nrows=0)
        dataFrame4 = dataFrame4.columns.values[0]

        dataFrame5 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 27, nrows=0)
        dataFrame5 = dataFrame5.columns.values[0]

        dataFrame6 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 32, nrows=0)
        dataFrame6 = dataFrame6.columns.values[0]

        dataFrame7 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 49, nrows=0)
        dataFrame7 = dataFrame7.columns.values[0]

        dataFrame8 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 49, nrows=0)
        dataFrame8 = dataFrame8.columns.values[0]


        print("\nArchivo: -5 6DPEA.xls")
        print("\nPanel number: ",dataFrame1)
        print("\nJob number: ",dataFrame2)
        print("\nJob name: ",dataFrame3)
        print("\nSeal: ",dataFrame4)
        print("\nType: ",dataFrame5)
        print("\nModbus Id: ",dataFrame6)
        print("\nSerial number: ",dataFrame7)
        print("\nMeter No.: ",dataFrame8)
        print("------------------------")

        
        #Una vez leido los datos los guardamos en nuestra base de datos ya creada
        connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "Omar1998<",
        db = "examen1"
        )

        cursor = connection.cursor()

        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('3', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame7, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame8)
        cursor.execute(sql)
        connection.commit()

#Función para leer archivos del archivo -8 2PP3BT
def datos3():
        #Leer el archivio

        filePath = "-8 2PP3BT.xls"
        hoja = "Sheet1"

        dataFrame1 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="D", header = 2, nrows=0)
        dataFrame1 = dataFrame1.columns.values[0]

        dataFrame2 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="D", header = 3, nrows=0)
        dataFrame2 = dataFrame2.columns.values[0]

        dataFrame3 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="D", header = 4, nrows=0)
        dataFrame3 = dataFrame3.columns.values[0]

        dataFrame4 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="J", header = 2, nrows=0)
        dataFrame4 = dataFrame4.columns.values[0]

        dataFrame5 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 27, nrows=0)
        dataFrame5 = dataFrame5.columns.values[0]

        dataFrame6 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 32, nrows=0)
        dataFrame6 = dataFrame6.columns.values[0]

        dataFrame7 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 49, nrows=0)
        dataFrame7 = dataFrame7.columns.values[0]
        dataFrame8 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 50, nrows=0)
        dataFrame8 = dataFrame8.columns.values[0]
        dataFrame9 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 51, nrows=0)
        dataFrame9 = dataFrame9.columns.values[0]
        dataFrame10 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 52, nrows=0)
        dataFrame10 = dataFrame10.columns.values[0]
        dataFrame11 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 53, nrows=0)
        dataFrame11 = dataFrame11.columns.values[0]
        dataFrame12 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 54, nrows=0)
        dataFrame12 = dataFrame12.columns.values[0]
        dataFrame13 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 55, nrows=0)
        dataFrame13 = dataFrame13.columns.values[0]
        dataFrame14 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 56, nrows=0)
        dataFrame14 = dataFrame14.columns.values[0]
        dataFrame15 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 57, nrows=0)
        dataFrame15 = dataFrame15.columns.values[0]
        dataFrame16 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 58, nrows=0)
        dataFrame16 = dataFrame16.columns.values[0]
        dataFrame17 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 59, nrows=0)
        dataFrame17 = dataFrame17.columns.values[0]
        dataFrame18 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 60, nrows=0)
        dataFrame18 = dataFrame18.columns.values[0]
        dataFrame19 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 61, nrows=0)
        dataFrame19 = dataFrame19.columns.values[0]
        dataFrame20 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 62, nrows=0)
        dataFrame20 = dataFrame20.columns.values[0]
        dataFrame21 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="C", header = 63, nrows=0)
        dataFrame21 = dataFrame21.columns.values[0]


        
        dataFrame22 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 49, nrows=0)
        dataFrame22 = dataFrame22.columns.values[0]
        dataFrame23 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 50, nrows=0)
        dataFrame23 = dataFrame23.columns.values[0]
        dataFrame24 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 51, nrows=0)
        dataFrame24 = dataFrame24.columns.values[0]
        dataFrame25 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 52, nrows=0)
        dataFrame25 = dataFrame25.columns.values[0]
        dataFrame26 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 53, nrows=0)
        dataFrame26 = dataFrame26.columns.values[0]
        dataFrame27 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 54, nrows=0)
        dataFrame27 = dataFrame27.columns.values[0]
        dataFrame28 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 55, nrows=0)
        dataFrame28 = dataFrame28.columns.values[0]
        dataFrame29 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 56, nrows=0)
        dataFrame29 = dataFrame29.columns.values[0]
        dataFrame30 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 57, nrows=0)
        dataFrame30 = dataFrame30.columns.values[0]
        dataFrame31 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 58, nrows=0)
        dataFrame31 = dataFrame31.columns.values[0]
        dataFrame32 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 59, nrows=0)
        dataFrame32 = dataFrame32.columns.values[0]
        dataFrame33 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 60, nrows=0)
        dataFrame33 = dataFrame33.columns.values[0]
        dataFrame34 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 61, nrows=0)
        dataFrame34 = dataFrame34.columns.values[0]
        dataFrame35 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 62, nrows=0)
        dataFrame35 = dataFrame35.columns.values[0]
        dataFrame36 = pd.read_excel(filePath, sheet_name = hoja, index_col= None, usecols="B", header = 63, nrows=0)
        dataFrame36 = dataFrame36.columns.values[0]


        print("\nArchivo: -3 2DPEA.xls")
        print("\nPanel number: ",dataFrame1)
        print("\nJob number: ",dataFrame2)
        print("\nJob name: ",dataFrame3)
        print("\nSeal: ",dataFrame4)
        print("\nType: ",dataFrame5)
        print("\nModbus Id: ",dataFrame6)
        print("\nSerial number: ",dataFrame7, dataFrame8, dataFrame9, dataFrame10, dataFrame11, dataFrame12, dataFrame13, dataFrame14, dataFrame15, dataFrame16, dataFrame17, dataFrame18, dataFrame19, dataFrame20, dataFrame21)
        print("\nMeter No.: ",dataFrame22, dataFrame23, dataFrame24, dataFrame25, dataFrame26, dataFrame27, dataFrame28, dataFrame29, dataFrame30, dataFrame31, dataFrame32, dataFrame33, dataFrame34, dataFrame35, dataFrame36)
        print("------------------------")

        
        #Una vez leido los datos los guardamos en nuestra base de datos ya creada
        connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "Omar1998<",
        db = "examen1"
        )

        cursor = connection.cursor()

        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('4', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame7, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame22)
        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('5', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame8, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame23)
        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('6', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame9, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame24)
        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('7', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame10, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame25)
        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('8', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame11, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame26)
        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('9', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame12, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame27)
        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('10', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame13, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame28)
        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('11', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame14, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame29)
        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('12', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame15, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame30)
        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('13', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame16, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame31)
        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('14', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame17, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame32)
        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('15', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame18, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame33)
        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('16', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame19, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame34)
        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('17', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame20, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame35)
        sql = "INSERT INTO job_traveler(id_traveler, Serial_number, Panel_Number, Job_Number, Job_Name, Seal, Type, Modbus_id, Meter_No) VALUES('18', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dataFrame21, dataFrame1, dataFrame2, dataFrame3, dataFrame4, dataFrame5, dataFrame6, dataFrame36)


        cursor.execute(sql)
        connection.commit()






datos1()
#datos2()
#datos3()
#descomprimir()