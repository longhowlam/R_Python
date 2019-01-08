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
        by = c("PC6"="Postcode_spatie")
    )

## gemiddelde prijs per provincie
Prov = huis2 %>%
    group_by(province_code) %>%
    summarise(
        min  = min(prijs),
        max  = max(prijs),
        mean = mean(prijs)
    ) %>%
    arrange(mean)

Prov