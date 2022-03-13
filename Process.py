
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
        print(f'{name} tiene {Instructions} tareas oara realizar')
        with CPU.request() as resource:
            yield resource #solicitar espacio de procesador
            instructions -= 2*req #se asume que puede hacer 2 instrucciones por nucleo
            yield env.timout(Timetoact) #simular tiempo de realizacion del proceso
    yield RAM.put(Resource) #regresar la memoria usada
    print (f'{name} ha sido completado, tiempo de uso {(env.now) - Start}')
    
random.seed(10)            
    
    
    
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