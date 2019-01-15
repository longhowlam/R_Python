###############################################
##
## Some visualisation in R

#### first some data
library(tidyverse)
huis = read_csv("huizen.csv")

#### ggplot2

## scatterplot
ggplot(huis, aes(x = Oppervlakte, y = prijs)) + geom_point()

## kleur 
huis %>%
    filter(prijs < 1000000, kamers < 10, Oppervlakte < 500) %>%
    ggplot(aes(x = Oppervlakte, y = prijs, color = kamers)) +
    geom_point() + labs(title = "Oppervlakte vs Prijs met aantal kamers")

## histograms
ggplot(huis, aes(prijs)) + geom_histogram(bins = 20)

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
