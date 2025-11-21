{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0d1064b6",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\ielin\\AppData\\Local\\Temp\\ipykernel_1932\\989349743.py:1: DeprecationWarning: the ``nasa_exoplanet_archive`` module has been moved to astroquery.ipac.nexsci.nasa_exoplanet_archive, please update your imports.\n",
      "  from astroquery.nasa_exoplanet_archive import NasaExoplanetArchive\n"
     ]
    }
   ],
   "source": [
    "from astroquery.nasa_exoplanet_archive import NasaExoplanetArchive\n",
    "import pandas as pd\n",
    "\n",
    "table = NasaExoplanetArchive.query_criteria(table=\"pscomppars\",select=\"pl_name,hostname,discoverymethod,disc_year,pl_eqt\")\n",
    "df = table.to_pandas()\n",
    "\n",
    "df.to_csv(\"nasa_exoplanet.csv\", index=False)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25254ff6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
