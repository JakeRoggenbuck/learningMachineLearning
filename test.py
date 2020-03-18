import numpy
from scipy import stats

db = [99,86,87,88,111,86,103,87,94,78,77,85,86]

print("db: ",db)
print("Mean: ",numpy.mean(db))
print("Median: ",numpy.median(db))
print("Mode: ",stats.mode(db))
print("Standard Deviation:",numpy.std(db))
print("Variance:",numpy.var(db))

