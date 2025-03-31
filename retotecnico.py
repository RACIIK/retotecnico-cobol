import csv                      #libreria csv para el manejo de archivos csv
import sys                      # sys para manejar errores
from typing import List, Dict   #librerias necesarias para el manejo de listas y diccionarios

#Requerimientos 
# 01 Balance Final: #01 Suma de los montos de las transacciones de tipo "Crédito " 
# menos la suma de los montos de las transacciones de tipo "Débito".
#02 Transacción de Mayor Monto: #Identificar el ID y el monto de la transacción con el valor más alto.
#Conteo de Transacciones:
#03 Número total de transacciones para cada tipo ("Crédito" y "Débito").

#Definimos la clase transaccion con los 03 atributos de una transaccion bancaria
class Transaccion:
    def __init__(self, transaccion_id: str, tipo: str, monto: float):
        self.transaccion_id = transaccion_id
        self.tipo = tipo
        self.monto = monto

# Definimos la clase ProcesadorTransacciones que se encargara de procesar el archivo csv 
# y realizar los calculos  para el reporte
class ProcesadorTransacciones:
    def __init__(self, archivo_csv: str):
        self.archivo_csv = archivo_csv  #Ruta del archivo CSV que contiene las transacciones.
        self.transacciones: List[Transaccion] = [] #Lista que almacenará objetos de tipo Transaccion.


    def cargar_transacciones(self):
        # Carga las transacciones desde el archivo CSV y las almacena en la lista de transacciones.
        # Maneja errores comunes como archivo no encontrado o formato incorrecto.
        try:
            with open(self.archivo_csv, newline='', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)

                #Bucle for: Recorre cada fila del CSV. / creamos el objetos que va tener la siguiente estructura.
                for fila in lector:
                    self.transacciones.append(Transaccion(fila['transaccion_id'], fila['tipo'], float(fila['monto'])))
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{self.archivo_csv}'.")
            sys.exit(1)
        except KeyError:
            print("Error: El archivo CSV no tiene el formato esperado.")
            sys.exit(1)
        except ValueError:
            print("Error: Hay valores no válidos en el archivo CSV.")
            sys.exit(1)

    # Calcula el balance final sumando los montos de las transacciones de tipo "Crédito" y restando los montos de las transacciones de tipo "Débito".
    def calcular_balance_final(self) -> float:
        return sum(t.monto if t.tipo == "Crédito" 
                   else -t.monto 
                   for t in self.transacciones)
    #Buscamos el monto mayor de las transacciones y lo retornamos.
    #Se compara los objetos Transaccion por su atributo monto. 
    def obtener_transaccion_mayor_monto(self) -> Transaccion:
        return max(self.transacciones, key=lambda t: t.monto, default=None)

    #Contamos las transacciones de tipo "Crédito" y "Débito" y retornamos un diccionario con el conteo. | diccionario 
    def contar_transacciones(self) -> Dict[str, int]:
        conteo = {"Crédito": 0, "Débito": 0}
        for t in self.transacciones:
            if t.tipo in conteo:
                conteo[t.tipo] += 1
        return conteo

    def generar_reporte(self):
        balance_final = self.calcular_balance_final()
        transaccion_max = self.obtener_transaccion_mayor_monto()
        conteo_transacciones = self.contar_transacciones()

        print("===========Reporte de Transacciones===========")
        print("----------------------------------------------")
        print(f"Balance Final: {balance_final:.2f}")
        if transaccion_max:
            print(f"Transacción de Mayor Monto: ID {transaccion_max.transaccion_id} | {transaccion_max.monto:.2f}")
        print(f"Conteo de Transacciones: Crédito: {conteo_transacciones['Crédito']} Débito: {conteo_transacciones['Débito']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py archivo.csv")
        sys.exit(1)
    
    procesador = ProcesadorTransacciones(sys.argv[1])
    procesador.cargar_transacciones()
    procesador.generar_reporte()
