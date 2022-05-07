import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a[a < 5])
print(np.ones(2, dtype=np.int64))
print(np.array([1, 2, 3, 4, 5, 6])[np.newaxis, :])


# download numpy arr
# np.save('numpyArr', a)

# Вы можете использовать np.load()для восстановления массива.
# b = np.load('numpyArr.npy')

np.savetxt('new_file.csv', a)
