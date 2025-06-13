library(tidyverse)
library(magrittr)

patients <- read_csv(
  "data/patient.csv",
  col_types = cols(
    MRN = col_character(),
    DOB = col_datetime(format = "%m/%d/%Y"),
    race = col_factor(),
    financialclass = col_factor(),
    ethnicity = col_factor(),
    hypertension = col_factor(),
    CHF = col_factor(),
    diabetes = col_factor()
  )
)

encounters <- read_csv(
  "data/encounter.csv",
  col_types = cols(
    MRN = col_character(),
    contact_date = col_datetime(format = "%m/%d/%Y"),
    enc_type = col_factor(),
    temp = col_double(),
    distress_score = col_double(),
    WBC = col_double(),
    BMI = col_double()
  )
)

inner_join(x = patients, y = encounters, by = "MRN") %>% 
  write_csv(., "data/merged_df.csv")

cat("Wrote merged CSV file as \"data/merged_df.csv\"")
