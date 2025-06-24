#!/bin/bash

# Obtiene la fecha actual en el formato YYYY-MM-DD
fecha_actual=$(date +'%Y-%m-%d')
echo "Fecha actual: $fecha_actual"

# Define el contenido a escribir en el archivo
contenido="Este archivo se creó el $fecha_actual"
echo "Contenido: $contenido"

# Escribe el contenido en el archivo './reports/report_YYYY-MM-DD.csv'
echo "$contenido" > "${JMETER_FOLDER}reports/report_$fecha_actual.csv"
echo "Se escribió el contenido en el archivo ${JMETER_FOLDER}reports/report_$fecha_actual.csv"
echo "pwd: $(pwd)"
# correr Jmeter con parametros
jmeter -n -t Backend.jmx -l "jmeter_logs_$fecha_actual.jtl" -e -o "./reports/report_$fecha_actual.csv"
