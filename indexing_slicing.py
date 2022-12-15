#indexing and slicing
import numpy as np

grades = np.array([[87,96,70],[100,87,90],[94,77,90],[108,81,82]])
grades_1 = grades[0,1]
grades_2 = grades[1]
grades_3 = grades[[1,3]]

print(grades, grades_1, grades_2)
