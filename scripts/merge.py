import pandas as pd

df_nasa = pd.read_csv("data/nasa/nasa_exoplanet_cleaned.csv")
df_esa = pd.read_csv("data/esa/esa_exoplanet_cleaned.csv")

df_esa = df_esa[["name", "star_teff"]]
df_esa.columns = ['pl_name', 'st_teff']

merged = pd.merge(df_nasa, df_esa, on = ["pl_name"], how = "inner")
merged.to_csv("data/merged_exoplanets.csv", index=False)
