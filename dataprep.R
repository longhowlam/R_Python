##############################################
##
## basic data prep with tidyverse

library(tidyverse)

huis = read_csv("huizen.csv")
PC = read_csv("postcodes.csv")

## join on postcodes
huis2 = huis %>%
  left_join(
    PC,
    by = c("PC6" = "Postcode_spatie")
  )

## gemiddelde prijs per provincie
Prov = huis2 %>%
  group_by(province_code) %>%
  summarise(
    minprice  = min(prijs, na.rm = TRUE),
    maxprice  = max(prijs, na.rm = TRUE),
    meanprice = mean(prijs, na.rm = TRUE)
  ) %>%
  arrange(meanprice)

Prov

## filter data
huis2 %>% filter(province_code == "ZE")