import math

print('Input the radius of the circle which you want to know the area of:')

radius = float(input('Radius (cm) \n'))
area = float((radius ** 2) * math.pi)

print('The area of the circle is: %s' % area)


