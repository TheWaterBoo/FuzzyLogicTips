#Triangular
def funcionMembresiaTriangular(x0, x1, x2, x):
    if x < x0 or x > x2:
        return 0.0
    elif x >= x0 and x <= x1:
        return (x - x0) / (x1 - x0)
    elif x >= x1 and x <= x2:
        return (x2 - x) / (x2 - x1)
    return 0.0

#Trapezoide
def funcionMembresiaTrapezoidal(x0, x1, x2, x3, x):
    # if x == 1:
    #     return 0.0
    if x <= x0 or x >= x3:
        return 0.0
    elif x0 < x <= x1:
        return float((x - x0) / (x1 - x0))
    elif x1 < x <= x2:
        return 1.0
    elif x2 < x <= x3:
        return float((x3 - x) / (x3 - x2))