""" Consulta SNMP """

print("Script de consulta de dispositivos por medio del SNMP")

from pysnmp.hlapi import *

def consultaSNMP(ip, comunidad, oid):
    """ Consulta un OID SNMP y devuelve el valor """

    iterator = getCmd(  # ← getCmd con C mayúscula
        SnmpEngine(),
        CommunityData(comunidad),
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(f"Error: {errorIndication}")
        return None
    elif errorStatus:
        print(f"Error: {errorStatus.prettyPrint()}")
        return None
    else:
        for varBind in varBinds:
            return str(varBind[1])

# Programa principal
ip = input("Introduce la IP del equipo: ")
comunidad = input("Introduce la comunidad SNMP (ej. public): ")

# sysName
oidsysName = "1.3.6.1.2.1.1.5.0"
nombre = consultaSNMP(ip, comunidad, oidsysName)
print(f"Nombre del sistema: {nombre}")

# sysDescr
oidsysDescr = "1.3.6.1.2.1.1.1.0"
descripcion = consultaSNMP(ip, comunidad, oidsysDescr)
print(f"Descripcion: {descripcion}")
