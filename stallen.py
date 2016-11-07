import time
import datetime
def datumentijd():
    #geeft huidige datum en tijd
    huidigedatumentijd = datetime.datetime.now().strftime('%d-%m-%Y, %H:%M:%S')
    return huidigedatumentijd
print(datumentijd())
