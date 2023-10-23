import defuzzification as defuzz
import rules
from foodQuality import *
from servicieQuality import *

foodValue, serviceValue, maxNada, maxPoca, maxNormal, maxGenerosa = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

while foodValue == 0:
    foodValue = float(input("Calificacion de la comida (1 - 10): "))

    if foodValue <= 0 or foodValue >= 11:
        print("Solo se permiten valores entre el rango permitido\nVuelva a intentarlo!\n")
        foodValue = 0

while serviceValue == 0:
    serviceValue = float(input("Calificacion del Servicio (1 - 10): "))

    if serviceValue <= 0 or serviceValue >= 11:
        print("Solo se permiten valores entre el rango permitido\nVuelva a intentarlo!\n")
        serviceValue = 0

foodObject = FoodQuality(foodValue)
serviceObject = ServiceQuality(serviceValue)

print("\n- - - Resultado de la membresia de la comida - - -\n\t\tDesagradable: \t" + str(foodObject.desagradable) +
      "\n\t\tAceptable: \t\t" + str(foodObject.aceptable) +
      "\n\t\tDelicioso: \t\t" + str(foodObject.delicioso) + "\n")

print("- - - Resultado de la membresia del servicio  - - -\n\t\tPesimo: \t\t" + str(serviceObject.pesimo) +
      "\n\t\tPromedio: \t\t" + str(serviceObject.promedio) +
      "\n\t\tExcelente: \t\t" + str(serviceObject.excelente) + "\n")

allFoodValues = [foodObject.desagradable, foodObject.aceptable, foodObject.delicioso]
allServiceValues = [serviceObject.pesimo, serviceObject.promedio, serviceObject.excelente]

partialResult = (rules.chooseRule(allFoodValues, allServiceValues))

for current in partialResult:
    if current[1][0] == "Nada":
        maxNada = max(maxNada, current[1][1])

    if current[1][0] == "Poca":
        maxPoca = max(maxPoca, current[1][1])

    if current[1][0] == "Normal":
        maxNormal = max(maxNormal, current[1][1])

    if current[1][0] == "Generosa":
        maxGenerosa = max(maxGenerosa, current[1][1])

membershipList = [0, maxPoca, 0, 0, maxNormal, 0, 0, maxGenerosa, 0]
rangesList = [2, 5, 8, 7, 10, 13, 15, 20, 20]

defuzzyResult = defuzz.defuzzificationCentroid(membershipList, rangesList)

print("================================================")
print("   No. Regla(s)  |    Porcentaje de Propina     ")
print("================================================")

# Imprimimos los resultados obtenidos con el respectivo tiempo.
for current in partialResult:
    print("\t    " + str(current[0]) + "\t\t | \t" + (str(defuzzyResult)))

print("================================================\n")

if 0 >= defuzzyResult <= 2:
    print(str("No se recibio nada de propina"))
elif defuzzyResult >= 2.1 and defuzzyResult <= 4.9:
    print(str("La propina esta entre poca y casi nada"))
elif defuzzyResult == 5:
    print(str("Se ha recibio solo poca propina"))
elif defuzzyResult >= 5.1 and defuzzyResult <= 9.9:
    print(str("La propina esta entre poca y una normal"))
elif defuzzyResult == 10:
    print(str("La propina ha sido normal"))
elif defuzzyResult >= 10.1 and defuzzyResult <= 19.9:
    print(str("La propina esta entre una normal y una generosa"))
elif defuzzyResult == 20:
    print(str("Se ha recibido una propina muy generosa"))

