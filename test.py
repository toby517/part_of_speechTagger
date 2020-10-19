# save numpy array as csv file
from numpy import asarray
from numpy import savetxt
import os
# define data
data = ('hello','hi','nice')
# save to csv file
#savetxt('data.txt', data, delimiter=',')

file = open('filetest.txt','w')

for i in data:
    file.write(i)
    file.write('\n')

