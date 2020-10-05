import math

pi = 3.1415926
D = 1.12
sumforce = 0.0
R = float(input("吹口半徑:"))
r = float(input("乒乓球半徑:"))
deg = float(input("漏斗半角"))
rate = float(input("風速:"))
phi = float(input("分割度數:"))
d_unit = 90 / phi
area = (R*R - r*r) * pi
raddeg = math.radians(deg)
radphi = math.radians(phi)

def Area(angle):
    t = R - r * math.tan(raddeg) * math.sin(angle)
    A = (t * t - (r * math.cos(angle))*(r * math.cos(angle))) * pi
    return A

def Bernoulli(v):
    return 1/2 * D * v * v

for i in range (1,6,1):
        print (Area(radphi/2 + (i-1)*radphi))
for i in range (1,int(d_unit)+1,1):
    P = Bernoulli(area * rate / Area(radphi/2 + (i-1) * radphi ))
    surface = ((r * math.cos(radphi * (i-1))) * (r * math.cos(radphi * (i-1)))- (r * math.cos(radphi * i)) * (r * math.cos(radphi * i)) ) * pi
    sumforce = sumforce + P * surface
print(sumforce)
