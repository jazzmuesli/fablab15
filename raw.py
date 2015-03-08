import sys
import time
import mraa


f = open('raw.csv','w')
f.write("time,a0,a1,a4,a5\n")
stime = time.time()
duration = float(sys.argv[1])

i = 0
try:
    ar = [mraa.Aio(x) for x in [0,1,4,5]]
    flag = True
    while flag:
      line = str(time.time()) + "," + ",".join([str(x.read()) for x in ar])
      f.write(line + "\n")
      i = i + 1
      since = time.time() - stime
      if i % 1000 == 0:
        f.flush()
      flag = since < duration
except Exception,e: 
  print str(e)
