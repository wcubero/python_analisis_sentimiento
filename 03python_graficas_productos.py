import matplotlib.pyplot as plt

# Datos de ejemplo: nombres de productos y cantidades vendidas
productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E']
cantidades_vendidas = [150, 200, 50, 300, 120]

# Crear la figura y el eje
fig, ax = plt.subplots()

# Crear la gráfica de barras
ax.bar(productos, cantidades_vendidas, color='skyblue')

# Añadir etiquetas y título
ax.set_xlabel('Productos')
ax.set_ylabel('Cantidad Vendida')
ax.set_title('Productos Más Vendidos')

# Mostrar la gráfica
plt.show()