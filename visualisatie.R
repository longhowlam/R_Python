###############################################################################
##
## Some visualisation in R

#### first import some data
library(tidyverse)
huis = read_csv("huizen.csv")

######## ggplot2 ##############################################################

# The grammar of graphics: ggplot2. Een plot wordt gemaakt door layers op elkaar te leggen,
# elke laag kan worden beschreven met zogenaamde *aesthetics* (stijlen). Elke laag kan in een
# variabele opgeslagen worden en deze kunnen bij elkaar 'opgeteld' worden tot een uiteindelijke plot. 

## scatterplot
ggplot(huis, aes(x = Oppervlakte, y = prijs)) + geom_point()

## kleur, haal wat data weg voor estetische redenen
## let op de overgang %>% naar +
huis %>%
    filter(prijs < 1000000, kamers < 10, Oppervlakte < 500) %>%
    ggplot(aes(x = Oppervlakte, y = prijs, color = kamers)) +
    geom_point() + labs(title = "Oppervlakte vs Prijs met aantal kamers")

## histograms
huis %>%
    filter(prijs < 1000000, kamers < 10, Oppervlakte < 500) %>%
    ggplot(aes(prijs)) +
    geom_histogram(bins = 20) +
    labs(x = "prijs in Euros")

## bar plots
huis %>%
    group_by(Type) %>%
    summarise(n = n()) %>%
    filter( n > 1000) %>%
    ggplot(aes(x = Type, weight = n)) + geom_bar()


## boxplots
PC = read_csv("postcodes.csv")

## join on postcodes
huis %>%
  left_join(
    PC,
    by = c("PC6" = "Postcode_spatie")
  ) %>%
  filter(prijs < 1000000, kamers < 10, Oppervlakte < 500) %>%
  ggplot(aes(x = province_code, y = prijs)) +
  geom_boxplot()

## werkt niet in VSC maar in RStudio komt de plot in een interactive viewer

library(plotly)
plot_ly(z = ~volcano)
plot_ly(z = ~volcano) %>% add_surface()

mtcars = mtcars
mtcars$naampjes = row.names(mtcars)

plot_ly(data = mtcars, x=~mpg, y = ~wt)
plot_ly(data = mtcars, x=~mpg, y = ~wt, color = ~cyl)
plot_ly(data = mtcars, x=~mpg, y = ~wt, text = ~naampjes)
