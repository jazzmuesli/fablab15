getRaw <- function(duration) {
  cmd <- paste0('ssh root@10.0.0.12 "python raw.py ', duration, ' && cat raw.csv"')
  data <- read.csv( pipe( cmd ), header = T )
  data
}

data <- getRaw(30)
data$time <- data$time-min(data$time)
ml <- melt(data,"time")
ggplot(data=ml, aes(x=time,y=value,colour=variable))+stat_smooth()
