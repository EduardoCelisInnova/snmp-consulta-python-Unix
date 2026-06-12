# Consulta SNMP con Python

Script en Python para consultar dispositivos de red mediante SNMP.

## ⚠️ Requisito importante

Este script **funciona en Linux y sistemas Unix**.

Para Windows, consultar la versión alternativa con `subprocess`.

## Requisitos

```bash
pip install pysnmp

Uso

bash
python consultarUnixSNMP.py

EJEMPLO:
Introduce la IP del equipo: demo.snmplabs.com
Introduce la comunidad SNMP: public

Nombre del sistema: myDevice
Descripcion: Linux 4.9.0-8-amd64

OIDs disponibles
OID	Descripción
1.3.6.1.2.1.1.5.0	sysName (Nombre del equipo)
1.3.6.1.2.1.1.1.0	sysDescr (Descripción del hardware)
1.3.6.1.2.1.1.6.0	sysLocation (Ubicación)
Autor

Eduardo Celis
