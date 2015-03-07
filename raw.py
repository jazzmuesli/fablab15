import sys
import time
import mraa
#import numpy

from math import sqrt

def mean(lst):
    """calculates mean"""
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return (sum / len(lst))

def stddev(lst):
    """calculates standard deviation"""
    sum = 0
    mn = mean(lst)
    for i in range(len(lst)):
        v = lst[i] - mn
        sum += v*v #(lst[i]-mn),2)
    sz = len(lst) - 1 
#    print "sum: " + str(sum) + ", len: " + str(sz)
    
    s = sqrt(sum/sz)
    return s

numbers = [120,112,131,211,312,90]

def report(ar):
  if len(ar) > 1:
    return str(len(ar)) + "," + str(mean(ar)) + "," + str(stddev(ar))
  else:
    return "NA,NA,NA"
#print stddev(numbers)

arx = []
ary = []
old_time = 0
#print (mraa.getVersion())
f = open('raw.csv','w')
f.write("time,a0,a5")
stime = time.time()
duration = float(sys.argv[1])

i = 0
try:
    x = mraa.Aio(0)
    y = mraa.Aio(5)
    flag = True
    while flag:
      line = str(time.time()) + "," + str(x.read()) + "," + str(x.read())
      f.write(line + "\n")
      i = i + 1
      since = time.time() - stime
      if i % 1000 == 0:
        f.flush()
      flag = since < duration
except Exception,e: 
  print str(e)
