# Administrador de Servidores, ASE.

URL Trello:

https://trello.com/useristradordeservidores1

Modelo Entidad-Relación

<img src="EntidadRelacionDB-ASE.png">

Diccionario de Datos.<br />
<br />
ips:<br />
<br />
ip: Dirección ip.<br />
interfaz: Interfaz física de la red.<br />
mac: Mac Address de la interfaz de red.<br />
<br />
maquinas:<br />
<br />
sistema_operativo:<br />
nombre:Nombre de la máquina (host)<br />
tipo:Es un servidor o un cliente<br />
activo:Si la máquina sigue en funcionamiento<br />
<br />
servidores:<br />
<br />
modo:<br />
nombre: El nombre del servidor (ejem: glassfish)<br />
version: La versión instalda del servidor<br />
host: O dominio, nombre del servidor<br />
puerto: puerto de escucha<br />
root: directorio de instalación<br />
puerto_administrativo: Puerto administrativo del servidor, si poseé, como glassfish<br />
<br />
aplicaciones:<br />
nombre: El nombre de la aplicación<br />
ruta_web: El path para acceder a la aplicación (Ejem: /)<br />
version: La última versión en producción<br />
repositorio: Url del repositorio del codigo fuente<br />
activo: Si la aplicación se encuentra activa<br />
host: En caso de ser un servidor virtual en base a un nombre de servidor<br />
puerto: En caso de que su servidor virtual esté sobre otro puerto<br />