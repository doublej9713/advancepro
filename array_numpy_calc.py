#numpy calculation method
import numpy ass np

grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])

grades_sum = grades.sum()
grades_min = grades.min()
grades_max = grades.max()
grades_mean = grades.mean()
grades_std = grades.std()

print(grades_sum,grades_min ,grades_max ,grades_mean ,grades_std )
