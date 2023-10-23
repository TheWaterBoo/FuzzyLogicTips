#Funcion para realizar la defuzzificacion por centroide
def defuzzificationCentroid(membershipList, rangeList):
    numerator = sum(membershipList[i] * rangeList[i] for i in range(len(membershipList)))
    denominator = sum(membershipList)
    if denominator > 0:
        centroid = numerator / denominator
    else:
        centroid = 0

    return centroid
