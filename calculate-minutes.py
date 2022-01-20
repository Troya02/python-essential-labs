####La tarea es preparar un código simple para evaluar o encontrar el tiempo
##final de un periodo de tiempo dado, expresándolo en horas y minutos.
#Las horas van de 0 a 23 y los minutes de 0 a 59.
#El resultado debe ser mostrado en la consola.

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
mins = ((dura+mins)%60)
dura /= 60
while dura > 0:
    hour+= 1
    dura-= 1
    while hour > 23:
        hour -= 24
        
        print(str(hour) + ":" + str(mins))
