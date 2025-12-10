# Exoplanet Properties and Discovery
Final project for IS477: Elina Sharma &amp; Victor Liu

# Contributors:
## Elina:
- [x] Ethical data handling (Module 2)
- [x] Storage and organization (Modules 4/5)
- [x] Data quality (Module 9)
- [x] Data integration (Module 7/8)
- [x] Workflow automation and provenance (Module 11/12)
## Victor:
- [x] Data lifecycle (Module 1)
- [x] Data collection and acquisition (Module 3)
- [x] Data cleaning (Module 10)
- [x] Reproducibility and transparency (Module 13)
- [x] Metadata and data documentation (Module 15)

# Summary:
Our aim with this project is to study the relationships between host star properties and exoplanet parameters through integration of ESA’s data and NASA's exoplanet catalog. The catalogs were chosen because they complement one another in their information about exoplanet properties, and they draw from reputable sources that can be trusted. This can help us better understand planet formation in our own Solar System as well as in other galaxies. We know that we are biased towards the exoplanets that we are able to observe, so by having a better understanding of the characteristics of those specific exoplanets, we can be aware of our observational bias and potentially mitigate its effects on our inferences regarding exoplanets in general.

Specifically, our research was focused on two questions:
- Is there a relationship between host star effective temperature and exoplanet equilibrium temperature?
- How have exoplanet discovery methods changed over time, particularly in relation to discovery year?

By answering these questions we could learn more about how stellar properties affect exoplanet characteristics within their own system as well as the prevalence of certain exoplanet detection methods with time. We chose these two questions because they are important to exoplanet science, one about the exoplanet creation and environment and the other about the observational techniques.

For our file structure, both datasets have a raw csv file, a cleaned csv file, a SHA hash, and a json file documenting our OpenRefine cleaning history, located within their respective space agency folders in the data folder. The integrated exoplanets csv is located within the data folder but not in either of the space agency folders. The scripts for the SHA hash generation, hash verification, NASA data query, integration, and analysis/visualization are located within the scripts folder. There is also a results folder containing .pngs of the two visualizations associated with our research questions. The requirements.txt contain the software dependencies and records of packages used.

To briefly summarize our findings, we found a dense triangular region with some outliers surrounding the area of the scatterplot when observing relationships between planet equilibrium temperatures and stellar effective temperatures, likely indicating rough boundary conditions for the relationship between the two variables. Looking at discovery methods and counts by year we found that the number of exoplanets discovered started exponentially increasing around 15 to 20 years ago, indicating a rather recent development in exoplanet detection techniques and equipment. We found that the discovery method used to discover the most and majority of exoplanets by far was transit, which has only continued to increase since the jump in the number of discovered exoplanets around 15 to 20 years ago. The other methods can’t keep up and the next most prominent discovery method in this dataset is radial velocity which has comparatively been used to discover only a small portion of the total exoplanets in the dataset. All the other methods listed in the dataset were used to discover even smaller fractions of exoplanets compared to radial velocity. Together, the findings highlight both the physical conditions around exoplanets and the observational biases due to our current technology in exoplanet detection.

# Data Profile:
## Dataset 1: NASA exoplanet archive
The first dataset we used for this project is the NASA exoplanet dataset which is a catalog of confirmed and candidate exoplanets with physical and orbital parameters such as names, radius, host star, temperature etc. The confirmed exoplanet data includes parameters or calculations that are combined from different references, all peer reviewed and rigorously chosen. References are given for each value in the metadata. The archive is publicly accessible and operated under NASA’s data-use policies, which require proper acknowledgment and citation of the dataset and its DOI, so operated under Creative Commons license.
(https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars)

## NASA Acquisition:
We accessed this data set through astroquery in python, which is a freely accessible library for querying astronomical web forms and databases. Importing the Nasa exoplanet library, we can use the inbuilt functions of astroquery to choose the columns that we need. The dataset is accessible to view through its parent site: [NASA Exoplanets](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars), so we were able to look through and select the exoplanet name, host name, discovery method, discovery year, and planet equilibrium temperature columns which are named pl_name, hostname, discoverymethod, disc_year, and pl_eqt respectively. The code that we used to download the data as CSV is included in the scripts folder as nasa_query.py. We also needed the pandas library to convert the dataframe to a CSV that we could use.

## NASA License:
The NASA Exoplanet Archive datasets are public data provided by NASA and hosted by the California Institute of Technology / IPAC. The data can be freely used and shared for research and educational purposes, but users must provide proper acknowledgment and cite the archive (including the relevant DOI). We have cited them below in the reference section.

## Dataset 2: ESA exoplanet catalog
The second dataset used is the ESA exoplanet catalog. This dataset provides the latest detections and data announced by professional astronomers on exoplanetary systems. Unlike NASA’s curated list of confirmed planets, this catalog adopts a broader and more inclusive scope by listing confirmed, unconfirmed, and controversial exoplanet candidates, along with free-floating planetary-mass objects. It contains objects lighter than 60 masses of Jupiter, which orbit stars or are free-floating. It also provides an exhaustive bibliography and links to other resources on the subject. It is licensed under a Creative Commons Attribution 4.0 International license.
(https://exoplanet.eu/catalog/)

## ESA Acquisition:
We accessed this dataset by directly downloading the catalog as a CSV from the website: [ESA Exoplanets](https://exoplanet.eu/catalog/).  Direct download ensures that we are working with the most current version of the dataset at the time of analysis. This can be different from the time of reading this report because the site is updated frequently. We have cited them below in the reference section.

## ESA License:
The ESA dataset has a Creative Commons Attribution 4.0 International license which means that we can share the data in any medium or format and that we can modify the data as long as appropriate credit is given and indicate how the data was changed or modified. (https://creativecommons.org/licenses/by/4.0/)

## Checking Integrity:
To ensure that no data was altered during the acquisition process, we computed a SHA256 hash for the raw data of both datasets to enable integrity verification and support the reproducibility of our results. The code needed to create the hashes is located in the scripts folder as generating_hash.py. Generating hashes is not in the automated workflow because we are ensuring the data has not changed after downloading and making sure our results are reproducible regardless of when the data is downloaded. After creating the hashes the hashes can be conformed by running the check_hash.py. 

# Data Quality and Cleaning:
## NASA Quality:
- Accuracy: The NASA dataset has a high level of accuracy because all sources for the dataset are peer-reviewed and well documented. When multiple measurements exist for the same parameter, the catalog applies a rigorous selection process to choose the most reliable value, generally prioritizing results from the most recent studies.  In the cases where values are recomputed, they are done using well known astrophysical methods and have full documentation of their methods. 
- Completeness: It only includes exoplanets and their parameters when validated and published. No parameters are included if they do not pass NASA’s strict criteria. While this results in an incomplete dataset, it endures the reliability and trustworthiness of the data.
- Timeliness: The timeliness is very strong for this dataset since it is updated very frequently, as and when new publications are available. However, because all data goes through a thorough vetting process there are some delays in adding new data to the dataset. 
- Consistency: The dataset is also very consistent. Parameter definitions follow scientific standards, and it uses uniform units and metadata. Each parameter is completely defined with formulae and sources through rich metadata also links each parameter to its reference source. 

## NASA Cleaning: 
We cleaned the dataset in OpenRefine. The main cleaning done was removing null values for the planet equilibrium temperature column, pl_eqt. This was done by faceting by blank (null or empty string) for the pl_eqt column, selecting the rows that were True, then removing the matching rows. Turning the column into numerical data and looking at the spread, there were some large outliers. But researching the few outliers showed that they were indeed true values. For example, an exoplanet with a temperature of 4000 K seemed too high, but researching it, we found out that it was the hottest discovered exoplanet, backed up by research. (https://en.wikipedia.org/wiki/KELT-9b). We thus decided to keep all the outliers. The rest of the columns did not have null values so no more cleaning was required. The cleaned dataset was then exported as nasa_exoplanet_cleaned.csv. The OpenRefine history is provided.

## ESA Quality:
- Accuracy: The ESA dataset shows moderate accuracy. Like the NASA dataset, it combines data from many sources. The data is relatively accurate because some sources can include preliminary measurements, rather than the peer reviewed final ones. It may also include some older parameters for legacy reasons. So some values may require confirmation against newer publications to ensure correctness.
- Completeness: It is a complete dataset as it includes confirmed, unconfirmed and controversial exoplanets, as opposed to the only confirmed exoplanets in the NASA dataset. However, it mentions the parameters (confirmed, unconfirmed and controversial) for every exoplanet in the dataset so it is easy to remove  them if required. This allows for more flexibility  due to the broader coverage.
- Timeliness: It is very timely because it is updated very frequently, as and when new publications, including preprints are available. So the updates are faster than the NASA catalog but with a little less reliability. The rapid updates can also lead to data being revised or withdrawn frequently.
- Consistency: The consistency for this dataset is not as good as the NASA dataset because the catalog is not as strict with units and parameter names, since the sources and their respective definitions are different. Rich metadata is provided on the site, so users can trace the sources and confirm values.

## ESA Cleaning: 
We uploaded the dataset, esaexoplanets.csv, into OpenRefine and created a new project. Then we made a facet by blank (null or empty string) for the star effective temperature variable, st_teff . Since there weren’t many blanks in the dataset, we decided to remove the rows where there were blanks by selecting “True” in the facet, going to “All”, then “Edit Rows”, and finally “Remove matching rows”. This way the rows with blanks in the st_teff column were removed and the remaining rows all had values. Looking at the spread of st_teff values after transforming the column into numerical data, we weren’t too worried about outliers as star temperatures can vary drastically depending on the type, age, luminosity, etc. The range of temperatures present is realistic according to our research, so we didn’t remove any apparent outliers. The cleaned dataset was then exported as esaexoplanet_cleaned.csv, and the OpenRefine Undo/Redo history extracted as esa_cleaning_history.json.

# Findings:
## Data Integration:
To integrate the data, we started with both the nasa_exoplanet_cleaned.csv and the esa_exoplanet_cleaned.csv datasets. The cleaned NASA dataset already contains the columns that we’re interested in performing analysis on, so it didn’t require any further processing for integration. The cleaned ESA dataset was of the entire database from the website, but we were only interested in performing analysis on two of the variables, so we isolated the two columns for use. The column we merged on was pl_name or the exoplanet names. We decided to do an inner merge so that only the rows that successfully merged would be left which reduced our dataset to 3443 rows. We decided to continue with our analysis but our smaller sample size reduces the extent to which our conclusions can be applied to the general exoplanet population. After the merge, we’re left with pl_name, hostname, discoverymethod, disc_year, pl_eqt, and st_teff.

## Data Analysis/Visualization:
For the data analysis, to answer our two research questions, we made two plots. For the first research question regarding the relationship between planet equilibrium temperature and star effective temperature, we created a scatter plot between the two variables. From the plot we can see that there is a triangular region in the graph from around 250 to 1750 K planet equilibrium temperature to around 3000 to 6500 K star effective temperature where the majority of the data points are located. There are relatively few outliers outside of this region.

For the second research question regarding the relationship between exoplanet discovery year and their discovery method, we decided to use a cumulative plot to visualize this relationship and see the increase in detections and distribution of detection methods over time. Since both columns already existed inside the NASA dataset, we used it instead of the merged dataset. We first grouped by discovery method and year and got counts of the number of exoplanet detections per discovery method each year. We then got cumulative sums for each of the discovery methods with time and plotted that. The output we got shows us that the total number of exoplanets discovered has roughly exponentially increased with time starting from about 2005 to 2006. In terms of the distribution for each discovery method per year, we can see that initially, each discovery method was used to discover a roughly similar amount of exoplanets. After about 2009, we can see that the number of exoplanets discovered using transit drastically increased and continues to increase even now. The number of exoplanets discovered by radial velocity have also slightly increased, but much slower than the increase in exoplanets discovered by transit. The remaining four discovery methods haven’t majorly changed over time as the number of exoplanets discovered by transit timing variations, orbital brightness modulation, and imaging have barely widened. The exoplanets discovered by microlensing are so few that they don’t really show up on the graph.

The output data can be found at this [Box link](https://uofi.box.com/s/63t6eiomos8yq6g6trmub0kwd98771na). It also contains the raw csv data that was manually downloaded from the ESA exoplanet catalog. The two plot .png files located in the results folder in the box link should already be in a results folder in the GitHub repository. The raw ESA csv is also already located in the esa folder which is the data folder.

# Future Work:
We were able to integrate the NASA and ESA exoplanet datasets and compare some of the features between host star properties, equilibrium temperatures, and discovery trends, but there is potential for further scientific analysis. We only used some columns of the many many stellar and exoplanet properties provided in the datasets. Further research can include more information into the integrated dataset to explore more relations between them and draw out interesting conclusions. 

One direction to extend the analysis, like mentioned above, is to use different properties such as stellar radius, luminosity, age etc to find multivariable relations. Some of these properties strongly influence  This would allow more understanding of what influences exoplanet occurrence and properties. Different methods for investigation could be used, like machine learning or regression models. This would allow us to maybe make predictions or discover new properties of the data. We also lost quite a few rows while merging our datasets, so using more available and easily measurable properties will give a more complete analysis. Another extension of our analysis is to pursue the time evolution aspect, like we showed in our discovery methods, but to other attributes in the dataset, especially since both NASA and ESA continuously update their catalogs to include new observations as observatories all around the world take more measurements. This could reveal biases and trends due to observational methods, which would in turn explain how important instrument and mechanical observations are to scientific analysis.

When we were choosing datasets, we considered many different datasets like the GAIA DR3 star dataset. We did not use it because we initially wanted to integrate the two datasets based on the host star name, but we quickly found out that star names aren’t completely standardized across datasets and surveys. More frequently than not, survey datasets would create independent IDs for stars based on what was observed which made it unfeasible to integrate the two datasets that way. Then we thought about integrating by numerical similarity between the right ascension and declination measurements for determining the star’s location in the sky, but implementing that was complicated. We eventually settled on the ESA’s exoplanet catalog which actually shares exoplanet names with the NASA exoplanet archive which drastically simplifies the integration process. Another problem we encountered was that our initial source had too much data, more than a million stars. It was out of our scope to deal with that much data, especially because most of it did not pertain to our other dataset about exoplanets. We would still be able to answer the same research questions with planet temperature and star temperature. So, another avenue for future work is using those datasets. It is still possible to use the initial dataset, but it was just out of our current scope and didn't align with our timeline. The initial dataset allows for deeper analysis because it contains more information and details about stars. They have higher precision measurements and therefore create opportunities for precise analysis and refinement of the values in the NASA and ESA dataset.

# Reproducibility:
The packages used thus far in this project are listed in the requirements.txt file. This included general system information and the like. ‘requirements.txt’ contains the exact libraries required to run all code provided in this repository. This is also an output of the command ‘pip freeze’ from the virtual environment used in this exploration.

## Workflow Automation:
To ensure full reproducibility for all stages of the project, we implemented an automated end-to-end workflow using Snakemake. The automated workflow can be run by snakemake using the provided snakefile. To run it, simply use the code: 
     snakemake –cores 1
Snakemake will automatically figure out which steps to execute, check the required inputs and give out the necessary outputs.

## Metadata and Documentation:
### Data Dictionary:
- pl_name (string) - Exoplanet name as designated in discovery literature
- hostname (string) - Host star name as designated in discovery literature
- discoverymethod (string) - Exoplanet discovery method
- disc_year (integer) - The year the specific exoplanet was discovered
- pl_eqt (float) - Planet equilibrium temperature assuming zero albedo, a proportion parameter ranging from 0 (no reflectivity) to 1 (full reflectivity) that determines how much light from the star is reflected back from the planet, measured in Kelvin
- st_teff (float) - Effective surface temperature of the host star, measured in Kelvin

### Metadata:
```json
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "NASA Exoplanet Archive — Confirmed Planets Table",
  "url": "https://exoplanetarchive.ipac.caltech.edu/",
  "sameAs": "https://doi.org/10.3847/PSJ/ade3c2",
  "creator": "NASA Exoplanet Science Institute",
  "description": "Planetary, orbital, and stellar parameters for confirmed exoplanets.",
  "dateModified": "2025-11-18"
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Exoplanet.eu Encyclopaedia",
  "url": "https://exoplanet.eu/catalog",
  "sameAs": "https://doi.org/10.1051/0004-6361/201116713",
  "creator": "Paris Observatory",
  "description": "A curated and continuously updated database of exoplanet parameters."
  "dateModified": "2025-11-20"
}
```

# Reference:
## License Compliance: 
NASA:
- Data source / Creator: NASA Exoplanet Archive (Planetary Systems Composite Parameters - PSCompPars)  
- Copyright / Ownership: © 2025 NASA / California Institute of Technology / IPAC  
- License / Terms of Use: Public data from NASA Exoplanet Archive, usage governed by archive policies.  
- Disclaimer: The dataset is a composite table. Parameter values may be drawn from multiple literature sources, and some values are computed by the archive. Users should exercise judgment regarding reliability.  
- Data modified by the users: cleaned thus far.
- DOI / Reference: (https://doi.org/10.3847/PSJ/ade3c2)

ESA:
- Data source / Creator: exoplanet TEAM (Extrasolar Planets Encyclopaedia)
- Copyright notice: © 1995-2025 Exoplanet TEAM / exoplanet.eu
- License: Licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0)
- Disclaimer: Users should make their own judgment on the reliability of individual entries according to their readme.
- Data modified by the users: cleaned thus far.
- DOI / Reference: (https://doi.org/10.1051/0004-6361/201116713)

## Citation:
Christiansen, Jessie L., et al. “The NASA Exoplanet Archive: Data, Tools, and Services for Exoplanet Research.” The Planetary Science Journal, 2025, https://doi.org/10.3847/PSJ/ade3c2

Schneider, Jean, et al. “Defining and Cataloguing Exoplanets: The Exoplanet.eu Database.” Astronomy & Astrophysics, 2011, https://doi.org/10.1051/0004-6361/201116713

Mölder, F., Jablonski, K.P., Letcher, B., Hall, M.B., Tomkins-Tinch, C.H., Sochat, V., Forster, J., Lee, S., Twardziok, S.O., Kanitz, A., Wilm, A., Holtgrewe, M., Rahmann, S., Nahnsen, S., Köster, J., 2021. Sustainable data analysis with Snakemake. F1000Res 10, 33.

## Acknowledgment:
This project makes use of the NASA Exoplanet Archive, which is operated by the California Institute of Technology, under contract with the National Aeronautics and Space Administration under the Exoplanet Exploration Program.

This project makes use of the Exoplanet Encyclopaedia, a regularly updated catalog of extrasolar planets, under the Creative Commons Attribution 4.0 International license. Data retrieved on 2025-11-20 from https://exoplanet.eu/catalog/.

