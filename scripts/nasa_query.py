from astroquery.nasa_exoplanet_archive import NasaExoplanetArchive
import pandas as pd

table = NasaExoplanetArchive.query_criteria(table="pscomppars",select="pl_name,hostname,discoverymethod,disc_year,pl_eqt")
df = table.to_pandas()

df.to_csv("nasa_exoplanet.csv", index=False)


