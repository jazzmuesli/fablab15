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
    return "empty"
print stddev(numbers)

arx = []
ary = []
old_time = 0
#print (mraa.getVersion())
print "a0.len,a0.mean,a0.sd,a5.len,a5.mean,a5.sd"
try:
    x = mraa.Aio(0)
    y = mraa.Aio(5)
    while True:
      if time.time() - old_time > 1:
        print report(arx) + "," + report(ary)
        arx = []
        ary = []
        old_time = time.time()  
      arx.append(x.read())
      ary.append(y.read())
except Exception,e: 
  print str(e)
