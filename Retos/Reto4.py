import array
import random
tamaño = random.randint(10,30)
aux = array.array('i',[random.randint(1,100) for _ in range(tamaño)])
print(aux)