from models import growthVisualizer as GV
from matplotlib import pyplot as plt
#Testing the models
v1 = GV('resources/covid19_asia.csv', 'Asia')
v2 = GV('resources/covid19_africa.csv', 'Africa')
v3 = GV('resources/covid19_europe.csv', 'Europe')
v4 = GV('resources/covid19_northamerica.csv', 'North America')
v4 = GV('resources/covid19_southamerica.csv', 'South America')

v2.show()