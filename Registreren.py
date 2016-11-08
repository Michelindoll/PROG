import random
import string
import csv

def id_Generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

print(id_Generator())



