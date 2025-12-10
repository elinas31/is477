import hashlib
import os

if os.path.exists('data/nasa/nasa_exoplanets_hash.sha'):
    with open("data/nasa/nasa_exoplanets.csv", "rb") as f:
        data = f.read()
        sha256hash = hashlib.sha256(data).hexdigest()
    with open("data/nasa/nasa_exoplanets_hash.sha", "rb") as f:
        hash = f.read().decode('utf-8')
        if hash != sha256hash:
            print("Hashes do not match")
        else:
            print("Hashes match")
else:
    print("Hash file for Nasa exoplanet data does not exist")

if os.path.exists('data/esa/esa_exoplanets_hash.sha'):
    with open("data/esa/esa_exoplanets.csv", "rb") as f:
        data = f.read()
        sha256hash = hashlib.sha256(data).hexdigest()
    with open("data/esa/cleaned_nasaexoplanets.sha", "rb") as f:
        hash = f.read().decode('utf-8')
        if hash != sha256hash:
            print("Hashes do not match")
        else:
            print("Hashes match")
else:
    print("Hash file for EU Exoplanet data does not exist")