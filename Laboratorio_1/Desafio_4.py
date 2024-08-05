"""Desafío 4: Sistema de Gestión de Cuentas Bancarias
    Objetivo: Desarrollar un sistema para administrar cuentas bancarias de clientes.

    Requisitos:

        Crear una clase base CuentaBancaria con atributos como número de cuenta, saldo, titular de la cuenta, etc.
        Definir al menos 2 clases derivadas para diferentes tipos de cuentas bancarias (por ejemplo, CuentaBancariaCorrientes, CuentaBancariaAhorro) con atributos y métodos específicos.
        Implementar operaciones CRUD para gestionar las cuentas bancarias.
        Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
        Persistir los datos en archivo JSON"""


import json

class Titular:

    def __init__(self, nombre, apellido, edad, cuil):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = self.validar_edad(edad)
        self.__cuil = self.Validar_Cuil(cuil)

    @property
    def info_titular(self):
        print(f"Nombre:{self.nombre}\nApellido:{self.apellido}\nEdad:{self.edad}\nCuil:{self.__cuil}")

    @property
    def getCuil(self):
        return self.__cuil
    
    @property
    def setCuil(self,cuil):
            self.__cuil = self.Validar_Cuil(cuil)    

    def Validar_Cuil(self,cuil):
        try:
            cuil_num = int(cuil)
            if 9 > len(cuil_num) > 11:
                raise ValueError('El Cuil debe tener entre 10 y 11 caracteres.')
            return cuil
        except ValueError:
            raise ValueError("El cuil es incorrecto...")
        
    def validar_edad(self,edad):
        try:
            edad_num = int(edad)
            if edad_num < 16:
                raise ValueError("No tienes la edad necesaria para Crearte una cuanta Bancaria.")
            return edad
        except ValueError:
            raise ValueError("Ingrese un numero valido...")


class CuentaBancaria(Titular):
    def __init__(self, nombre_titular, apellido_titular, edad, cuil, numero_de_cuenta, saldo):
        Titular.__init__(self, nombre_titular, apellido_titular, edad, cuil)
        self.__numero_de_cuenta = numero_de_cuenta
        self.__saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"el depocito de {monto} fue realizado con exito.\n Su saldo actual es de {self.__saldo}")
        else:
            print("La cantidad ingresada es menos a 0.")

    def retirar(self,retiro):
        if retiro <= self.__saldo:
            self.__saldo -= retiro
            print(f"El retiro de {retiro} feu realizado con exito.\n Su saldo actual es de {self.__saldo}")
        else:
            print("Saldo insuficiente.")


class CajaDeAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, apellido_titular, edad, cuil, numero_de_cuenta, saldo =0):
        CuentaBancaria.__init__(self,nombre_titular, apellido_titular, edad, cuil, numero_de_cuenta, saldo)


    
class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_titular, apellido_titular, edad, cuil, numero_de_cuenta, saldo =0):
        CuentaBancaria.__init__(self,nombre_titular, apellido_titular, edad, cuil, numero_de_cuenta, saldo)

