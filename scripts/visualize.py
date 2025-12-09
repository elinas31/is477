import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

merged = pd.read_csv('data/merged_exoplanets.csv')

plt.figure(figsize = (10, 6))
plt.scatter(merged["pl_eqt"], merged["st_teff"], s = 20)
plt.ylabel("Star Effective Temperature (K)")
plt.xlabel("Planet Equilibrium Temperature (K)")
plt.title("Star Temperature vs. Planet Temperature")
plt.savefig("results/st_eff_v_pl_eqt.png")
plt.close()

df_counts = df_nasa.groupby(["discoverymethod", "disc_year"]).size().reset_index(name = "count")

df_pivot = df_counts.pivot(index = "disc_year", columns = "discoverymethod", values = "count")

df_cum = df_pivot.cumsum()

df_cum.plot.area(figsize=(10,6))

plt.xlabel("Discovery Year")
plt.ylabel("Cumulative Number of Planets")
plt.title("Cumulative Exoplanet Discoveries by Method")
plt.legend(title = "Discovery Method", bbox_to_anchor = (1.01, 1), loc = "upper left")
plt.tight_layout()
plt.savefig("results/discoverybymethod.png")
plt.close()
