import hashlib

with open("data/nasa/nasa_exoplanet.csv", "rb") as f:
    data = f.read()

nasa_value = hashlib.sha256(data).hexdigest()

with open("data/esa/esa_exoplanet.csv", "rb") as f:
    data1 = f.read()

nasa_value = hashlib.sha256(data).hexdigest()
esa_value = hashlib.sha256(data1).hexdigest()

with open("data/nasa/nasa_exoplanets_hash.sha", "w") as f:
    f.write(nasa_value)

with open("data/esa/esa_exoplanets_hash.sha", "w") as f:
    f.write(esa_value)