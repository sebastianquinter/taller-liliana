"""
    Realizar un procedimiento que realice la conversión de coordinadas polares(r,0) a coordenadas caterianas x,y

    X= r. cos(0)
    Y= r. sen(0)’
"""

import math

def polares_a_cartesianas(r, theta_deg):
    theta_rad = math.radians(theta_deg)
    x = r * math.cos(theta_rad)
    y = r * math.sin(theta_rad)
    return x, y

r = float(input("Ingrese el valor de r: "))
theta_deg = float(input("Ingrese el valor de θ en grados: "))

x, y = polares_a_cartesianas(r, theta_deg)
print(f"Las coordenadas cartesianas correspondientes a (r={r}, θ={theta_deg} grados) son (x={x}, y={y})")