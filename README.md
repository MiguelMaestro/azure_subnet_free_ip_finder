# Azure Subnet IP Finder

Este script de Python interactúa con Azure para ayudarte a encontrar las primeras cinco direcciones IP disponibles en una subnet específica dentro de una red virtual (VNet) y suscripción de Azure.

## Requisitos

- Python 3.6 o superior
- Azure CLI instalado y configurado
- Paquete `tabulate` de Python

## Instalación

1. Asegúrate de tener Python 3.6 o superior instalado en tu sistema. Puedes verificar la versión de Python ejecutando `python --version` o `python3 --version` en la terminal.

2. Instala Azure CLI siguiendo las instrucciones en la [documentación oficial](https://docs.microsoft.com/es-es/cli/azure/install-azure-cli).

3. Instala el paquete `tabulate` de Python ejecutando:

```shell
pip install tabulate
```
o 

```shell
pip3 install tabulate
```


## Uso

1. Ejecuta el script en la terminal con el siguiente comando:

```shell
python3 azure_subnet_ip_finder.py
```


2. Sigue las instrucciones en pantalla para seleccionar la suscripción, VNet y subnet de Azure de la cual deseas obtener las primeras cinco direcciones IP disponibles.

3. El script mostrará las primeras cinco direcciones IP disponibles y te permitirá elegir otra suscripción, VNet o subnet, o salir del programa.

## Nota

Este script utiliza la CLI de Azure y requiere que hayas iniciado sesión en tu cuenta de Azure. Si no has iniciado sesión, el script te pedirá que lo hagas al principio.
