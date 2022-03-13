
#realizar los imports
import simpy
import random

#proceso del programa
def programa(name,env,CPU, RAM,RunTimer):
    #Tiempo de espera
    yield env.timeout(RunTimer)
    #tiempo de llegada
    Start = env.now
    print(f'{name} inicia en {Start}')
    
    #simular cantidad de tiempo requerido 
    Timetoact = random.randint(1, 10)
    #cantidad de memoria requerida para funcionar
    Resource = random.randint(1, 10) #de 1 a 10 espacios
    instructions = random.randint(1, 10) #de 1 a 10 instruciones puede requerir
    yield RAM.get(Resource) #esperar hasta haber cantidad de memoria disponible
    while instructions > 0:
        #iniciar proceso, si hay mas procesos antes, debe de esperar
        print(f'{name} tiene {instructions} tareas oara realizar')
        with CPU.request() as resource:
            yield resource #solicitar espacio de procesador
            instructions -= 2 #se asume que puede hacer 2 instrucciones a la vez
            yield env.timeout(Timetoact) #simular tiempo de realizacion del proceso
    yield RAM.put(Resource) #regresar la memoria usada
    global tiempo_total
    tiempo_total += (env.now) - Start
    print (f'{name} ha sido completado, tiempo de uso {(env.now) - Start}')
    
    
random.seed(10)
env = simpy.Environment()  # crear ambiente de simulacion
RAM = simpy.Container(env, 30, init=30)  # crea el container de la ram
CPU = simpy.Resource(env, capacity=1)  # se crea el procesador con capacidad establecida
procesos = 50  # cantidad de procesos a generar
tiempo_total = 0
for i in range(procesos):
    env.process(programa(f'Programa {i}', env ,CPU, RAM,0))
env.run()
print(f'tiempo total {tiempo_total}')
print(f'tiempo promedio {(tiempo_total/procesos)}')
    
    
'''
          _____                    _____             _____                    _____                    _____                   _______         
         /\    \                  /\    \           /\    \                  /\    \                  /\    \                 /::\    \        
        /::\    \                /::\    \         /::\    \                /::\____\                /::\    \               /::::\    \       
       /::::\    \              /::::\    \        \:::\    \              /:::/    /               /::::\    \             /::::::\    \      
      /::::::\    \            /::::::\    \        \:::\    \            /:::/    /               /::::::\    \           /::::::::\    \     
     /:::/\:::\    \          /:::/\:::\    \        \:::\    \          /:::/    /               /:::/\:::\    \         /:::/~~\:::\    \    
    /:::/__\:::\    \        /:::/__\:::\    \        \:::\    \        /:::/    /               /:::/__\:::\    \       /:::/    \:::\    \   
   /::::\   \:::\    \      /::::\   \:::\    \       /::::\    \      /:::/    /               /::::\   \:::\    \     /:::/    / \:::\    \  
  /::::::\   \:::\    \    /::::::\   \:::\    \     /::::::\    \    /:::/    /      _____    /::::::\   \:::\    \   /:::/____/   \:::\____\ 
 /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\   /:::/\:::\    \  /:::/____/      /\    \  /:::/\:::\   \:::\____\ |:::|    |     |:::|    |
/:::/  \:::\   \:::\____\/:::/  \:::\   \:::|    | /:::/  \:::\____\|:::|    /      /::\____\/:::/  \:::\   \:::|    ||:::|____|     |:::|    |
\::/    \:::\  /:::/    /\::/   |::::\  /:::|____|/:::/    \::/    /|:::|____\     /:::/    /\::/   |::::\  /:::|____| \:::\    \   /:::/    / 
 \/____/ \:::\/:::/    /  \/____|:::::\/:::/    //:::/    / \/____/  \:::\    \   /:::/    /  \/____|:::::\/:::/    /   \:::\    \ /:::/    /  
          \::::::/    /         |:::::::::/    //:::/    /            \:::\    \ /:::/    /         |:::::::::/    /     \:::\    /:::/    /   
           \::::/    /          |::|\::::/    //:::/    /              \:::\    /:::/    /          |::|\::::/    /       \:::\__/:::/    /    
           /:::/    /           |::| \::/____/ \::/    /                \:::\__/:::/    /           |::| \::/____/         \::::::::/    /     
          /:::/    /            |::|  ~|        \/____/                  \::::::::/    /            |::|  ~|                \::::::/    /      
         /:::/    /             |::|   |                                  \::::::/    /             |::|   |                 \::::/    /       
        /:::/    /              \::|   |                                   \::::/    /              \::|   |                  \::/____/        
        \::/    /                \:|   |                                    \::/____/                \:|   |                   ~~              
         \/____/                  \|___|                                     ~~                       \|___|                                   
                                                                                                                                        
'''