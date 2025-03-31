# retotecnico-cobol
# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Descripción  
Este reto técnico consiste en desarrollar una aplicación de línea de comandos (CLI) para procesar transacciones bancarias. La aplicación debe analizar y generar información clave a partir de un conjunto de transacciones.  

## Requerimientos  

### 📌 Cálculo del Balance Final  
- Se debe calcular la diferencia entre la suma de los montos de las transacciones de tipo **"Crédito"** y la suma de los montos de las transacciones de tipo **"Débito"**.  

### 📌 Transacción de Mayor Monto  
- Identificar la transacción con el monto más alto, mostrando su **ID** y **valor**.  

### 📌 Conteo de Transacciones  
- Determinar el **número total de transacciones** para cada tipo:  
  - **"Crédito"** 🟢  
  - **"Débito"** 🔴  

## Instrucciones de Uso  
1. Ejecutar la aplicación en la terminal.  
2. Ingresar el archivo de transacciones o introducir los datos manualmente.  
3. Obtener los cálculos requeridos de manera inmediata.  

## Ejemplo de Entrada  
```txt
T001,Crédito,1500.0
T002,Débito,500.0
T003,Crédito,1200.5
