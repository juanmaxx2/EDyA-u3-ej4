import csv
from designacion import Designacion
from lista import Lista

if __name__ == "__main__":
    unaLista = Lista()
    archivo = open('estadistica-designacion-magistrados-federal-nacional-por-genero-20220323.csv')
    reader = csv.reader(archivo, delimiter = ',')
    bol=True
    pos = 1
    for fila in reader:
        if bol:
            bol = False
        else:
            unaDesignacion = Designacion(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
            unaLista.Insertar(unaDesignacion, pos)
            pos += 1
    cargo = input("\nIngrese el cargo a buscar:")
    print("\nLa cantidad de mujeres designadas en el cargo {} por año:".format(cargo))
    unaLista.cargo(cargo)
    print("\nPara buscar la cantidad de agentes ingrese:")
    materia = input("Ingrese la materia:")
    cargo = input("Ingrese el cargo:")
    anio = input("Ingrese el año:")
    print("La cantidad de agentes fue:{}".format(unaLista.agente(materia,cargo,anio)))