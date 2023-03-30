#1
'''
print("Hello World!")
'''
'''
a = int(input())
b = int(input())
X = a + b
print(f"X = {X}")
'''
#2
'''
R = float(input())
A = 3.14159 * R**2
print(f"A={A:.4f}")
'''
#3
'''
a = int(input())
b = int(input())
X = a + b
print(f"SOMA = {X}")
'''
#4
'''
a = int(input())
b = int(input())
X = a * b
print(f"PROD = {X}")
'''
#5
'''
A = float(input())
B = float(input())
average = (A*3.5 + B*7.5) / (3.5 + 7.5)
print(f"MEDIA = {average:.5f}")
'''
#6
'''
A = float(input())
B = float(input())
C = float(input())
average = (A*2 + B*3 + C*5) / (2 + 3 + 5)
print(f"MEDIA = {average:.1f}")
'''
#7
'''
A = int(input())
B = int(input())
C = int(input())
D = int(input())
difrensia = (A * B - C * D)
print(f"DIFERENCA = {difrensia}")
'''
#8
'''
A = float(input()) #banyak orang
B = float(input()) #waktu kerja
C = float(input()) #gaji/jam
NUMBER = A
print(f"NUMBER = {NUMBER:.0f}")
SALARY = B * C
print(f"SALARY = U$ {SALARY:.2f}")
'''
#9
'''
'''
#10
'''
Barang_A = input().split(" ")
Barang_B = input().split(" ")

code1, unit1, price1 = Barang_A
code2, unit2, price2 = Barang_B

total = (int(unit1)) * (float(price1)) + (int(unit2)) * (float(price2))
print(f"VALOR A PAGAR: R$ {total:.2f}")
'''
#11
'''
phi = 3.14159
r = int(input())
V = (4/3) * phi * r**3
print(f"VOLUME = {V:.3f}")
'''
#12
'''
a, b, c = input().split()
a, b, c = float(a).float(b).float(c)

triangle = float(a) * 3.14159 * float(c)
circle = float(a) *  float(c)
trapecium = float(a) *  float(c) + float(b)
square = b**2
rectangle = a * b

print(f"TRIANGULO: {triangle:.3f}\nCIRCULO: {circle:.3f}\nTRAPEZIO: {trapecium:.3f}\nQUADRADO: {square:.3f}\nRETANGULO: {rectangle:.3f}")
'''
#13
'''
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

Mab = (a + b + abs(a - b))/2
Mf = (Mab + c + abs(Mab - c))/2

print(f"{int(Mf)} eh o maior")
'''
#14
'''
A = float(input())
B = float(input())
consumption = A/B
print(f"{consumption:.3f} km/l")
'''
#15
'''
from math import sqrt
x1, x2 = input().split()
y1, y2 = input().split()
Distance = sqrt((float(x1) - float(x2))**2 + ((float(y1) - float(y2))**2
print(f"{Distance:.4f}")
'''
#16
'''
speed = int(input())
distance = speed*2
print(f"{distance} minutos")
'''