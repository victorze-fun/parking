## Requerimientos

Como dueño de un estacionamiento yo quiero...

- ...poder registrar el ingreso de un vehículo.
- ...poder registrar la salida de un vehículo y cobrar el costo del servicio.
- ...poder ingresar el costo por hora, el redondeo y el tiempo de tolerancia.
- ...poder ver un reporte por rango de tiempo, y poder filtrar por placa.
- ...(opcional) poder imprimir el ticket de ingreso y salida.

## Páginas

- `/entry`: Muestra un formulario donde registramos la placa y el tipo de vehículo.
Se mostrará la hora y el tiempo actual.

- `/search`: Muestra un formulario con dos campos: buscar por placa y buscar por
número de ticket.

- `/exit`: Si el vehículo es encontrado en la página `/search`, se mostrará un formulario
donde registramos la hora de salida del vehículo y el costo del servicio.

- `/rates`: Muestra un formulario donde podemos el costo por hora, el tiempo de redondeo
(en minutos minutos) y el tiempo de tolerancia (en minutos).

- `/report`: Muestra la relación de vehículos  filtrados por un rango de tiempo.

## Esquema de datos
https://youtu.be/NtMvNh0WFVM?t=1154
