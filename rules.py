
def chooseRule(alFudVal, alSerVal):
    ruleResult = []

    # - Regla 1 -
    # if alFudVal == desagradable and alSerVal == pesimo then Propina = Nada
    if alFudVal[0] > 0 and alSerVal[0] > 0:
        ruleResult.append([1, ["Nada", 1]])

    # - Regla 2 -
    # if alFudVal == desagradable and alSerVal == promedio then Propina = Nada
    if alFudVal[0] > 0 and alSerVal[1] > 0:
        ruleResult.append([2, ["Nada", 1]])

    # - Regla 3 -
    # if alFudVal == desagradable and alSerVal == excelente then Propina = Poca
    if alFudVal[0] > 0 and alSerVal[2] > 0:
        ruleResult.append([3, ["Poca", min(alFudVal[0], alSerVal[2])]])

    # - Regla 4 -
    # if alFudVal == aceptable and alSerVal == pesimo then Propina = Nada
    if alFudVal[1] > 0 and alSerVal[0] > 0:
        ruleResult.append([4, ["Nada", 1]])

    # - Regla 5 -
    # if alFudVal == aceptable and alSerVal == promedio then Propina = Normal
    if alFudVal[1] > 0 and alSerVal[1] > 0:
        ruleResult.append([5, ["Normal", min(alFudVal[1], alSerVal[1])]])

    # - Regla 6 -
    # if alFudVal == aceptable and alSerVal == excelente then Propina = Normal
    if alFudVal[1] > 0 and alSerVal[2] > 0:
        ruleResult.append([6, ["Normal", min(alFudVal[1], alSerVal[2])]])

    # - Regla 7 -
    # if alFudVal == delicioso and alSerVal == pesimo then Propina = Nada
    if alFudVal[2] > 0 and alSerVal[0] > 0:
        ruleResult.append([7, ["Nada", 1]])

    # - Regla 8 -
    # if alFudVal == delicioso and alSerVal == promedio then Propina = Normal
    if alFudVal[2] > 0 and alSerVal[1] > 0:
        ruleResult.append([8, ["Normal", min(alFudVal[2], alSerVal[1])]])

    # - Regla 9 -
    # if alFudVal == delicioso and alSerVal == excelente then Propina = Generosa
    if alFudVal[2] > 0 and alSerVal[2] > 0:
        ruleResult.append([9, ["Generosa", min(alFudVal[2], alSerVal[2])]])

    return ruleResult