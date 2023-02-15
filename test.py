from SCF import *
import numpy as np

f = np.array([x**2 for x in range(10)])

# serie = SerieComplejaFourierDiscreta(f)
#
# # marca error correctamente
# #print(serie.SerieFourierArray(2))
# print(serie.SerieFourierArray(1))
# print()
# print(np.round(serie.SerieFourierArray(1),3))
# print()
# print(serie.SerieFourier(1))

serie2 = SerieComplejaFourierDiscreta(f,k=50)

# marca error correctamente
# print(serie.SerieFourierArray(2))

# print(serie2.SerieFourierArray(1))
# print()
# print(np.round(serie2.SerieFourierArray(1),3))
# print(np.round(serie2.SerieFourierArray(1)[50],3))
# print()
# print(serie2.SerieFourier(1))

print(np.round(serie2.SerieFourierArray(0.3)[50],3))
print(np.round(serie2.SerieFourierArray(0.5)[50],3))
print(np.round(serie2.SerieFourierArray(.1)[50],3))
