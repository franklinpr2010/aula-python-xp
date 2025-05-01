import numpy as np

# Criando arrays com NumPy
array1d = np.array([1, 2, 3])
array2d = np.array([[1, 2], [3, 4]])

print("1D Array:", array1d)
print("2D Array:", array2d)


array = np.array([[1, 2, 3], [4, 5, 6]])

# Transposição
transposto = array.T

# Redimensionamento
array_reshape = array.reshape(3, 2)

print("Transposto:\n", transposto)
print("Redimensionado:\n", array_reshape)

array = np.array([10, 20, 30, 40, 50])

# Selecionar um elemento
print("Elemento na posição 2:", array[2])

# Fatiar o array
print("Fatiado:", array[1:4])
