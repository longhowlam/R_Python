#######################################################
##
## Enkele voorbeelden machine learning in R

library(tidyverse)

huis = read_csv("huizen.csv")
PC = read_csv("postcodes.csv")

## join on postcodes en haal wat outliers weg
huis2 = huis %>%
  left_join(
    PC,
    by = c("PC6" = "Postcode_spatie")
  ) %>%
  filter(prijs > 50000, prijs < 2000000)


## fit rgeressie model met lm
outlm = lm(prijs ~ kamers + Oppervlakte, data = huis2)

summary(outlm)

plot(outlm)

##### dummy variables, gaat 'vanzelf' in R
outlm = lm(prijs ~ kamers + Oppervlakte + province_code, data = huis2)

## province DR is als reference weggelaten
summary(outlm)
# Wat betekend dit voor bijvoorbeeld province NH met parameter 178679.24
# Het betekend dat de huizenprijs gemiddeld 178679.24 hoge rligt dan DR

######### sum contrast
outlm = lm(
  prijs ~ kamers + Oppervlakte + province_code,
  data = huis2,
  contrasts = list(province_code = "contr.sum")
)
summary(outlm)

# De laatste coefficient is weggelaten, maar deze is de negatieve som van de overige
# exclusief intercept, kamers en oppervlakte
sum(coef(outlm)[c(-1,-2,-3)])

# nu kan je de paramters interpreteren als verschillen van het totale gemiddelde


#######  Amsterdam effect

huis2 = huis2 %>% mutate(
  Amsterdam = str_detect(city, "Amsterdam")
)

outlm = lm(
  prijs ~ kamers + Oppervlakte + province_code + Amsterdam, 
  data = huis2
)

summary(outlm)

















########################################################################################
##
## classification model

library(rpart)

# titanic passenger data
titanic = readr::read_csv("titanic.csv")

## decsion tree
tree.out = rpart(
  Survived ~ Sex + Age + Pclass, 
  data = titanic
)

plot(tree.out)
text(tree.out, use.n = TRUE)

library(rattle)
fancyRpartPlot(tree.out)

### larger trees with complexity parameter
tree.outComplex = rpart(
  Survived ~ Sex + Age + Pclass,
  data = titanic,
  control = list(cp=0.005)
)
fancyRpartPlot(tree.outComplex)