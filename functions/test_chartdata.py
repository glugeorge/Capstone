from import_libraries import *
from common_functions import *
import random

filename = initiate_file()

while True:
    x, y = random.random(), random.random()
    save_to_file(filename, x, y)
    time.sleep(0.5)