import matplotlib.pyplot as plt

def f(x):
    return x**2

a = 0
b = 10
n = 1000
dx = (b - a) / n
area = 0
x_values = []
y_values = []

for i in range(n):
    x_i = a + i * dx
    area += f(x_i) * dx
    x_values.append(x_i)
    y_values.append(f(x_i))

print("El valor aproximado de la integral es:", area)

plt.plot(x_values, y_values, label=r'$y = x^2$')
plt.fill_between(x_values, y_values, alpha=0.3, label=f"Área bajo la curva = {area:.2f}")
plt.title(r'Integral de $x^2$ entre 0 y 10')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()