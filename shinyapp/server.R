library(shiny)

library(reshape2)
library(zoo)
library(ggplot2)
getRaw <- function(duration) {
  cmd <- paste0('ssh root@10.0.0.12 "python raw.py ', duration, ' && cat raw.csv"')
  data <- read.csv( pipe( cmd ), header = T )
  data
}


f <- function(x,n) {
  mn <- mean(x)
  rollmean(x,n)
}


fakeData <- function(duration) {
  tx <- seq(0,duration,by = 0.001)
  data <- data.frame(time=tx,a0=rnorm(length(tx)),a1=rnorm(length(tx)),a4=rnorm(length(tx)),a5=rnorm(length(tx)))
  data  
}
chartPlot <- function(data) {
  n <- 550
  df <- data.frame(time=rollmax(data$time,n)-min(data$time),a0=f(data$a0,n),a1=f(data$a1,n),a4=f(data$a4,n),a5=f(data$a5,n))
  ml <- melt(df, "time")
  ml <- ml[ml$variable != "a1",]
  ggplot(data=ml,   aes(x=time, y=value, colour=variable)) +  geom_line()
}


shinyServer(function(input, output) {
  mydata <- reactive({
    getRaw(input$foo)
  })
  output$plot <- renderPlot({
    chartPlot(mydata())
  })
  output$table <- renderTable(summary(mydata()))
})