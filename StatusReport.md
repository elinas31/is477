# IS477
Final project for IS477: Elina Sharma &amp; Victor Liu

# Updated Overview: 
To study relationships between host star properties and exoplanet parameters, through integration of ESA’s data and NASA's exoplanet catalog. This can help us better understand planet formation in our own Solar System as well as in other galaxies. We know that we are biased towards the exoplanets that we are able to observe, so by having a better understanding of the characteristics of those specific exoplanets, we can be aware of our observational bias and potentially mitigate its effects on our inferences regarding exoplanets in general.

# Updated Research Question(s): 
The relationship between host star temperature and planet equilibrium temperature. 
The relationship between exoplanet discovery methods and their discovery year.

# Team: 
## Elina:
- [x] Ethical data handling (Module 2)
- [x] Storage and organization (Modules 4/5)
- [x] Data quality (Module 9)
- [ ] Data integration (Module 7/8)
- [ ] Workflow automation and provenance (Module 11/12)
## Victor:
- [x] Data lifecycle (Module 1)
- [x] Data collection and acquisition (Module 3)
- [x] Data cleaning (Module 10)
- [ ] Reproducibility and transparency (Module 13)
- [ ] Metadata and data documentation (Module 15)

# Data Lifecycle:
How this project relates to the FAIR data lifecycle: Findable, Accessible, Interoperable, Reusable
## Findable:
- Using datasets with persistent identifiers such as DOIs
- Maintaining clear filenames and folder structure in the Github repository
## Accessible:
- Providing download links for each dataset
- Including conditions such as attribution or licensing for use
## Interoperable:
- Storing processed data in a widely used scientific format such as CSV
- Will include column descriptions and data types in metadata for final report
## Reusable:
- Documenting software environment and necessary packages with requirements.txt
- Including extensive documentation regarding each processing step (acquisition, cleaning, eventually integration, analysis, etc.)

# Updated Datasets: 
## Dataset 1: NASA exoplanet archive
Catalog of confirmed and candidate exoplanets with physical and orbital parameters. The confirmed planet data includes parameters or calculations that are combined from different references. References are given for each value in the metadata. Operated under Creative Commons license.
(https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars)

## (CHANGED) Dataset 2: ESA exoplanet catalog
This dataset provides the latest detections and data announced by professional astronomers on exoplanetary systems. It contains objects lighter than 60 masses of Jupiter, which orbit stars or are free-floating. It also provides an exhaustive bibliography and links to other resources on the subject. It is licensed under a Creative Commons Attribution 4.0 International license.
(https://exoplanet.eu/catalog/)

Why we changed: We initially wanted to integrate the two datasets based on the host star name, but we quickly found out that star names aren’t completely standardized across datasets and surveys. More frequently than not, survey datasets would create independent IDs for stars based on what was observed which made it unfeasible to integrate the two datasets that way. Then we thought about integrating by numerical similarity between the right ascension and declination measurements for determining the star’s location in the sky, but implementing that was complicated. We eventually settled on the ESA’s exoplanet catalog which actually shares exoplanet names with the NASA exoplanet archive which drastically simplifies the integration process. Another problem we encountered was that our initial source had too much data, more than a million stars. It was out of our scope to deal with that much data, especially because most of it did not pertain to our other dataset about exoplanets. We would still be able to answer the same research questions with planet temperature and star temperature.

# Obtaining datasets:
## NASA dataset:
We accessed this data set through astroquery in python, which is a freely accessible library for querying astronomical web forms and databases. Importing the Nasa exoplanet library, we can use the inbuilt functions of astroquery to choose the columns that we need. The dataset is accessible to view through its parent site: [NASA Exoplanets](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars), so we were able to look through and select the planet name, host name, discovery method, discovery year, and planet equilibrium temperature columns which are named pl_name, hostname, discoverymethod, disc_year, and pl_eqt respectively. The code that we used to download the data as CSV is included in the scripts folder as nasa_query.py. We also needed the pandas library to convert the dataframe to a CSV that we could use.

## ESA dataset:
We accessed this dataset by directly downloading the catalog as a CSV from the website: [ESA Exoplanets](https://exoplanet.eu/catalog/). 

To ensure that no data was altered during the acquisition process, we computed a SHA256 hash for the raw data of both datasets to enable integrity verification and support the reproducibility of our results. The code needed to create the hashes is located in the scripts folder as generating_hash.py. We will make code to compare the hashes in the final report.

# Data Quality:
## NASA:
- Accuracy: Very accurate because all sources for the dataset are peer-reviewed and well documented. Values that are recomputed are chosen from the best available paper/source. 
- Completeness: It only includes planets and their parameters when validated and published. They do not include parameters if formally confirmed.
- Timeliness: Updated very frequently, as and when new publications are available. Data is thoroughly reviewed before adding, so there is some delay.
- Consistency: Parameter definitions follow scientific standards, and it uses uniform units and metadata. Rich metadata also links each parameter to its reference source. 

## ESA:
- Accuracy: Relatively accurate because some sources can include preliminary measurements. Also includes some older parameters for legacy reasons. 
- Completeness: It includes confirmed, unconfirmed and controversial exoplanets, as opposed to the only conformed exoplanets in the NASA dataset. It mentions the parameters for the above exoplanets so easy to remove or focus on. It thus has a broader coverage.
- Timeliness: Updated very frequently, as and when new publications, including preprints are available. So the updates are faster but with a little less reliability.
- Consistency: Not as strictly uniform with units and parameter names, since the sources and their respective definitions are different. 

# Cleaning data:
Both datasets were cleaned using OpenRefine
## NASA dataset: 
We cleaned the dataset in OpenRefine. The main cleaning done was removing null values for the planet equilibrium temperature column, pl_eqt. This was done by faceting by blank (null or empty string) for the pl_eqt column, selecting the rows that were True, then removing the matching rows. Turning the column into numerical data and looking at the spread, there were some large outliers. But researching the few outliers showed that they were indeed true values. For example, a planet with a temperature of 4000 K seemed too high, but researching it, we found out that it was the hottest discovered exoplanet, backed up by research. (https://en.wikipedia.org/wiki/KELT-9b). We thus decided to keep all the outliers. The rest of the columns did not have null values so no more cleaning was required. The cleaned dataset was then exported as nasa_exoplanet_cleaned.csv. The OpenRefine history is provided.

## ESA dataset: 
We uploaded the dataset, esaexoplanets.csv, into OpenRefine and created a new project. Then we made a facet by blank (null or empty string) for the star effective temperature variable, star_teff. Since there weren’t many blanks in the dataset, we decided to remove the rows where there were blanks by selecting “True” in the facet, going to “All”, then “Edit Rows”, and finally “Remove matching rows”. This way the rows with blanks in the star_teff column were removed and the remaining rows all had values. Looking at the spread of star_teff values after transforming the column into numerical data, we weren’t too worried about outliers as star temperatures can vary drastically depending on the type, age, luminosity, etc. The range of temperatures present is realistic so we didn’t remove any apparent outliers. The cleaned dataset was then exported as esaexoplanet_cleaned.csv, and the OpenRefine Undo/Redo history extracted as esa_cleaning_history.json.

# License Compliance: 
The NASA Exoplanet Archive datasets are public data provided by NASA and hosted by the California Institute of Technology / IPAC. The data can be freely used and shared for research and educational purposes, but users must provide proper acknowledgment and cite the archive (including the relevant DOI).
- Data source / Creator: NASA Exoplanet Archive (Planetary Systems Composite Parameters - PSCompPars)  
- Copyright / Ownership: © 2025 NASA / California Institute of Technology / IPAC  
- License / Terms of Use: Public data from NASA Exoplanet Archive, usage governed by archive policies.  
- Disclaimer: The dataset is a composite table. Parameter values may be drawn from multiple literature sources, and some values are computed by the archive. Users should exercise judgment regarding reliability.  
- Data modified by the users: cleaned thus far.
- DOI / Reference: (https://doi.org/10.26133/NEA13)

The ESA dataset has a Creative Commons Attribution 4.0 International license which means that we can share the data in any medium or format and that we can modify the data as long as appropriate credit is given and indicate how the data was changed or modified. (https://creativecommons.org/licenses/by/4.0/)
- Data source / Creator: exoplanet TEAM (Extrasolar Planets Encyclopaedia)
- Copyright notice: © 1995-2025 Exoplanet TEAM / exoplanet.eu
- License: Licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0)
- Disclaimer: Users should make their own judgment on the reliability of individual entries according to their readme.
- Data modified by the users: cleaned thus far.
- DOI / Reference: (https://doi.org/10.1051/0004-6361/201116713)

# Reproducibility:
The packages used thus far in this project are listed in the system_info.txt file. This included general system information and the like. An updated version will be provided for the final version if required.

# Update Timeline: 
## Completed Tasks:
Victor:
- Data lifecycle relation
- Acquisition of ESA dataset
- Selecting storage/organization strategy
- ESA dataset cleaning and documentation
- License compliance for both datasets
- Updated timeline, dataset, overview
- Worked on status report formatting/structuring

 Elina:
- Data quality assessments
- Acquisition of Nasa dataset (nasa_query.py)
- Generating hashes for both datasets (generating_hash.py)
- NASA dataset cleaning and documentation 
- Creating the requirements file
- Updated some parts of status report


## New Timeline Dates:
### November
- Data integration (Victor/Elina)
- Data analysis (Victor/Elina)
- Creating automated end-to-end workflow (Elina)
- Full data documentation (provenance, reproducibility/transparency, metadata, update requirements.txt) (Victor)
### December
- Final checks and submission (Victor/Elina)
