#shallow copies
import numpy as np

numbers_1 = np.arange(1,5)
numbers_1 = numbers_1[1]*20
numbers_2 = numbers_1.view() #use .view for shallow copy

print(numbers_2)
