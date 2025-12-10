rule run_all:
    input:
        "data/esa/esa_exoplanets.csv",
        "data/nasa/nasaexoplanets.csv"
    output:
        "data/merged_exoplanets.csv",
        "results/discoverybymethod.png",
        "results/st_eff_v_pl_eqt.png"

rule nasa_query:
    output:
        "data/nasa/nasa_exoplanets.csv"
    shell:
        "python scripts/nasa_query.py"

rule obtain_eu_data:
    output:
        "data/esa/esa_exoplanets.csv"

rule clean_data:
    input:
        "data/esa/esa_exoplanets.csv",
        "data/nasa/nasa_exoplanets.csv"
    output:
        "data/nasa/nasa_exoplanet_cleaned.csv",
        "data/esa/esa_exoplanet_cleaned.csv",
        "data/nasa/nasa_cleaning_history.json",
        "data/esa/esa_cleaning_history.json"

rule check_hash:
    input:
        "data/nasa/nasa_exoplanets.csv",
        "data/esa/esa_exoplanets.csv"
    shell:
        "python scripts/check_hash.py"

rule merge:
    input:
        "data/nasa/nasa_exoplanet_cleaned.csv",
        "data/esa/esa_exoplanet_cleaned.csv"
    output:
        "data/merged_exoplanets.csv"
    shell:
        "python scripts/merge.py"

rule plot_data:
    input:
        "data/merged_exoplanets.csv",
	    "data/nasa/nasa_exoplanet_cleaned.csv"
    output:
        "results/discoverybymethod.png",
        "results/st_eff_v_pl_eqt.png"
    shell:
        "python scripts/visualize.py"