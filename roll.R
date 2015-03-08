  library(reshape2)
  library(zoo)
  library(ggplot2)
  getRaw <- function(duration) {
    cmd <- paste0('ssh root@10.0.0.12 "python raw.py ', duration, ' && cat raw.csv"')
    data <- read.csv( pipe( cmd ), header = T )
    data
  }
  
  
  data <- getRaw(10)
  n <- 550
  f <- function(x,n) {
    mn <- mean(x)
    rollmean(x,n)
  }
  
  
  df <- data.frame(time=rollmax(data$time,n)-min(data$time),a0=f(data$a0,n),a1=f(data$a1,n),a4=f(data$a4,n),a5=f(data$a5,n))
  ml <- melt(df, "time")
  ml <- ml[ml$variable != "a1",]
  ggplot(data=ml,   aes(x=time, y=value, colour=variable)) +  geom_line()
