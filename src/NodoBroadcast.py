import simpy
import time
from Nodo import *
from Canales.CanalBroadcast import *

# La unidad de tiempo
TICK = 1
class NodoBroadcast(Nodo):
    ''' Implementa la interfaz de Nodo para el algoritmo de Broadcast.'''

    def __init__(self, id_nodo, vecinos, canal_entrada, canal_salida, mensaje=None):
	#Tu codigo aqui
        self.id_nodo=id_nodo
        self.vecinos=vecinos
        self.canal_entrada=canal_entrada
        self.canal_salida=canal_salida
        self.mensaje=mensaje
        self.seen_message = False 

    def broadcast(self, env):
        ''' Algoritmo de Broadcast. Desde el nodo distinguido (0)
            vamos a enviar un mensaje a todos los demás nodos.'''
        #Tu codigo aqui    
        if self.id_nodo==0: # 3
            self.seen_message=True #4
            self.mensaje="Mensaje"
            if self.vecinos:  #5
                self.canal_salida.envia(('BROADCAST', self.mensaje), self.vecinos)
                yield env.timeout(TICK)
        
        while True: #7
            #Recibir mensajes
            mensaje = yield self.canal_entrada.get()
            tipo, contenido=mensaje
            if tipo == 'BROADCAST' and not self.seen_message: #8
                self.seen_message = True #9 
                self.mensaje = contenido 
                if self.vecinos:  #10
                    self.canal_salida.envia(('BROADCAST', self.mensaje), self.vecinos)
                    yield env.timeout(TICK)