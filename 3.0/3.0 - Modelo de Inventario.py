import math
from os import system
from random import random

class Inventory:

    def __init__(self, PARAMS) -> None:     #CONSTRUCTOR PARA INICIALIZAR ALGUNOS ATRIBUTOS USADOS MÁS ADELANTE
        self.PARAMS = PARAMS
        self.next_event_type = None
        self.amount = None
        self.smalls = None,
        self.bigs = None
        self.reports = []
        self.print_information = None



    #ESTE ES EL 'MAIN' Y ES EL ÚNICO MÉTODO PÚBLICO QUE ES USADO POR EL USUARIO, LOS DEMÁS SON PRIVADOS
    def simulate(self, printInformation = True) -> list:
        
        if(not isinstance(printInformation,bool)):
            raise Exception("printInformation debe ser booleano")

        self.print_information = printInformation

        if self.print_information:
            self.__print_headers()

        
        POSSIBLE_EVENTS = {
            1: self.__order_arrival,
            2: self.__demand,
            3: self.__report,
            4: self.__evaluate,
        }


        for i,policy in enumerate(self.PARAMS["policies"]):
            
            self.smalls = self.PARAMS["policies"][i][0]
            self.bigs = self.PARAMS["policies"][i][1]
            
            self.__initialize()
            
            self.next_event_type = None

            while self.next_event_type != 3:
                
                self.__timing()
                self.__update_time_avg_stats()

                POSSIBLE_EVENTS[self.next_event_type]()

        return self.reports



    #ENCABEZADO PARA MOSTRAR LOS PARÁMETROS
    def __print_headers(self) -> None:
        print(
f"""
Modelo de Inventario de Producto Simple
    
Nivel inicial de Inventario     {self.PARAMS["initial_inventory_level"]}

Tamaño de Demandas              {len(self.PARAMS["demands_function_distribution"])}

Distribución de las funciones de Tamaño de Demandas    {self.PARAMS["demands_function_distribution"]}

Tiempo Medio Entre Demandas     {self.PARAMS["mean_interdemand_time"]}

Rango de Retraso de Entrega     {self.PARAMS["delivery_lag_range"]}

Duración de la Simulación       {self.PARAMS["simulation_length"]}

K={self.PARAMS["setup_cost"]}    i = {self.PARAMS["incremental_cost"]}    h={self.PARAMS["holding_cost"]}    pi={self.PARAMS["shortage_cost"]}

Número de Políticas             {len(self.PARAMS["policies"])}

Política\t\tCosto Promedio Total\t\tCosto Promedio de Orden\t\tCosto Promedio de Mantenimiento\t\tCosto Promedio de Faltante

""");



    #INICIALIZAR VARIABLES
    def __initialize(self) -> None:

        #RELOJ DE SIMULACIÓN
        self.sim_time = 0 

        #VARIABLES DE ESTADO
        self.inv_level = self.PARAMS["initial_inventory_level"]
        self.time_last_event = 0

        #CONTADORES ESTADÍSTICOS
        self.total_ordering_cost = 0
        self.area_holding = 0
        self.area_shortage = 0

        #LISTA DE EVENTOS
        self.time_next_event = [   
        None,       #Agrego esta posición para que se alinee a las posiciones del arreglo que menciona en el libro y comience de 1
        1e+30,  
        self.sim_time + self.__expon(self.PARAMS["mean_interdemand_time"]), 
        self.PARAMS["simulation_length"],
        0
        ]



    def __timing(self) -> None:
        
        min_time_next_event = 1.0e+29

        self.next_event_type = 0

        for i in range(1, 5): # i VA DE 1 A 4(ES LA CANTIDAD DE EVENTOS POSIBLES)
            
            if self.time_next_event[i]  <  min_time_next_event:
                min_time_next_event = self.time_next_event[i]
                self.next_event_type = i

        if self.next_event_type == 0:
            raise Exception("next_event_type llegó a ser 0")

        self.sim_time = min_time_next_event



    
    def __update_time_avg_stats(self) -> None: 
        
        time_since_last_event = self.sim_time - self.time_last_event
        self.time_last_event = self.sim_time

        if self.inv_level < 0:
            self.area_shortage -= self.inv_level * time_since_last_event
        
        elif self.inv_level > 0:
            self.area_holding += self.inv_level * time_since_last_event


    #MÉTODOS QUE RESPONDEN CADA UNO A UN POSIBLE EVENTO

    def __order_arrival(self) -> None:

        self.inv_level += self.amount
        self.time_next_event[1] = 1.0e+30



    def __demand(self) -> None:
        self.inv_level -= self.__random_integer()
        self.time_next_event[2] = self.sim_time + self.__expon(self.PARAMS["mean_interdemand_time"])



    def __evaluate(self) -> None:
        
        if self.inv_level < self.smalls:
            
            self.amount = self.bigs - self.inv_level
            self.total_ordering_cost += ( self.PARAMS["setup_cost"] + self.PARAMS["incremental_cost"] * self.amount )

            self.time_next_event[1] = self.sim_time + self.__uniform(self.PARAMS["delivery_lag_range"][0], self.PARAMS["delivery_lag_range"][1]);

        self.time_next_event[4] = self.sim_time + 1



    def __report(self) -> None:
        
        avg_ordering_cost = round(self.total_ordering_cost / self.PARAMS["simulation_length"],3)
        avg_holding_cost = round(self.PARAMS["holding_cost"] * self.area_holding / self.PARAMS["simulation_length"],3)
        avg_shortage_cost = round(self.PARAMS["shortage_cost"] * self.area_shortage / self.PARAMS["simulation_length"],3)

        avg_total_cost = round(avg_ordering_cost + avg_holding_cost + avg_shortage_cost,3)

        self.reports.append({
            "avg_ordering_cost":avg_holding_cost, 
            "avg_holding_cost": avg_holding_cost, 
            "avg_shortage_cost": avg_shortage_cost,
            "avg_total_cost": avg_total_cost
            });

        if self.print_information:
            print(f"{self.smalls,self.bigs}\t\t{avg_total_cost}\t\t\t\t{avg_ordering_cost}\t\t\t\t{avg_holding_cost}\t\t\t\t\t{avg_holding_cost}\n")


    
    #DISTRIBUCIONES USADAS Y GENERACIÓN ALEATORIO DE ENTEROS
    
    def __expon(self,n) -> float:
        return -n * math.log(random())


    def __uniform(self,a,b) -> float:
        return a + random() * (b-a)


    def __random_integer(self) -> int:
        u = random()
        i = 1

        while u >= self.PARAMS["demands_function_distribution"][i - 1]:
            i+=1
        
        return i




#---------------------------------------------SE COMIENZA A USAR LA CLASE IMPLEMENTADA--------------------------------------------

system("clear");

#SE DECLARAN LOS PARÁMETROS NECESARIOS
PARAMS = {
    #num_policies se obtiene a partir de la longitud del arreglo "policies"
    
    "policies" : [
        [20,40],
        [20,60],
        [20,80],
        [20,100],
        [40,60],
        [40,80],
        [40,100],
        [60,80],
        [60,100],
    ],
    
    "initial_inventory_level": 60,

    #demands_size se consigue a partir del arreglo "demands_function_distribution"  
    
    "demands_function_distribution": [0.167, 0.5, 0.833 , 1], 
    
    "mean_interdemand_time": 0.10, #En Meses
    
    "delivery_lag_range": [0.50, 1], #Intervalo en Meses
    
    "simulation_length": 120, #En Meses
    
    "setup_cost": 32,
    
    "incremental_cost": 3,
    
    "holding_cost": 1,
    
    "shortage_cost": 5,

}

#SE CREA LA INSTANCIA DE Inventory Y SE LA PASA AL CONSTRUCTOR LOS PARAMS DEFINIDOS ANTERIORMENTE

inventoryI = Inventory(PARAMS);

#SE EJECUTA EL ÚNICO MÉTODO PÚBLICO DE LA CLASE PARA SIMULAR EL MODELO DE INVENTARIO
#ESTE MÉTODO PUEDE RECIBIR UN ÚNICO PARÁMETRO BOOLEANO PARA DETERMINAR SI MOSTRAR O NO LA INFORMACIÓN GENERADA
#INDEPENDIENTEMENTE EL VALOR DEL PARÁMETRO EL MÉTODO SIEMPRE DEVOLVERÁ UNA LISTA DE REPORTES QUE PUEDEN USARSE PARA LAS PRUEBAS

reports = inventoryI.simulate(True) #SI PONEMOS EL PARÁMETRO EN FALSE VA A DESAPARECER LA INFORMACIÓN DE LA CONSOLA

print(reports)

#SE PUEDEN REALIZAR YA LAS PRUEBAS Y TESTEOS CON LO QUE DEVUELVE LA SIMULACIÓN (reports EN ESTE CASO)