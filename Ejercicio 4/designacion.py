class Designacion:
    __designacion_anio = None
    __justicia_federal_o_nacional = None
    __cargo_tipo = None
    __instancia_tipo = None
    __materia = None
    __cantidad_varones = None
    __cantidad_mujeres = None

    def __init__ (self,designacion_anio, justicia_federal_o_nacional, cargo_tipo, instancia_tipo, materia, cantidad_varones, cantidad_mujeres):
        self.__designacion_anio = designacion_anio
        self.__justicia_federal_o_nacional = justicia_federal_o_nacional
        self.__cargo_tipo = cargo_tipo
        self.__instancia_tipo = instancia_tipo
        self.__materia = materia
        self.__cantidad_varones = cantidad_varones
        self.__cantidad_mujeres = cantidad_mujeres

    def __str__(self):
        return self.__designacion_anio + self.__justicia_federal_o_nacional + self.__cargo_tipo + self.__instancia_tipo + self.__materia + self.__cantidad_varones + self.__cantidad_mujeres

    def getDesignacionAnio(self):
        return self.__designacion_anio

    def getJusticia(self):
        return self.__justicia_federal_o_nacional

    def getCargo(self):
        return self.__cargo_tipo

    def getInstancia(self):
        return self.__instancia_tipo

    def getMateria(self):
        return self.__materia

    def getCantV(self):
        return self.__cantidad_varones

    def getCantM(self):
        return self.__cantidad_mujeres