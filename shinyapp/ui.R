library(shiny)

shinyUI(pageWithSidebar(
  headerPanel('Record and plot vibrations'),
  sidebarPanel(
    sliderInput("foo",
                "Duration:",
                min = 0,
                max = 60,
                value = 5)
  ),
  mainPanel(
    plotOutput(outputId='plot')
  )
))