#%%
import pandas as pd
import time
import requests

# ============================
# 1) Fonction de géocodage OSM
# ============================
def geocode_osm(localite, departement=None, region=None, pays="Cameroon"):
    query = localite

    if departement:
        query += f", {departement}"
    if region:
        query += f", {region}"
    query += f", {pays}"

    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": query, "format": "json", "limit": 1}

    try:
        response = requests.get(url, params=params, headers={"User-Agent": "GeoCoder-CMR-2025"})
        data = response.json()
        if len(data) == 0:
            return None, None
        return float(data[0]["lat"]), float(data[0]["lon"])
    except:
        return None, None

# ============================
# 2) Charger le fichier
# ============================
fichier = r"C:\Qgis\cacao_cmr_2025_geolocalise222.csv"
df = pd.read_csv(fichier, sep=";", encoding="utf-8-sig")

print("Colonnes détectées :", df.columns.tolist())

# ============================
# 3) Identifier les noms de colonnes corrects
# ============================
col_region = None
col_departement = None

for col in df.columns:
    col_low = col.lower()
    if "region" in col_low:
        col_region = col
    if "depart" in col_low:
        col_departement = col

if col_region is None:
    print("⚠️ Aucune colonne 'Region' trouvée. Géocodage sans région.")
if col_departement is None:
    print("⚠️ Aucune colonne 'Departement' trouvée. Géocodage sans département.")

# ============================
# 4) Localités à géocoder
# ============================
df_missing = df[df["Latitude"].isna() | df["Longitude"].isna()].copy()
print(f"📌 Localités à géocoder : {len(df_missing)}")

# ============================
# 5) Géocodage automatique
# ============================
for idx, row in df_missing.iterrows():
    loc = row["Localite"]
    dep = row[col_departement] if col_departement else None
    reg = row[col_region] if col_region else None

    print(f"🌍 Géocodage : {loc} ({dep}, {reg})...")

    lat, lon = geocode_osm(loc, dep, reg)

    df.loc[idx, "Latitude"] = lat
    df.loc[idx, "Longitude"] = lon

    time.sleep(1)

# ============================
# 6) Remplacer les valeurs manquantes
# ============================
df["Latitude"] = df["Latitude"].fillna("À renseigner")
df["Longitude"] = df["Longitude"].fillna("À renseigner")

# ============================
# 7) Export
# ============================
fichier_sortie = r"C:\Qgis\cacao_cmr_2025_geocode_complet.csv"
df.to_csv(fichier_sortie, sep=";", index=False, encoding="utf-8-sig")

print("\n🎉 Géocodage terminé !")
print(f"📁 Fichier généré : {fichier_sortie}")

# ============================
# 8) Localités introuvables
# ============================
introuvables = df[df["Latitude"] == "À renseigner"]["Localite"].unique()

print("\n❌ Localités introuvables :")
for loc in introuvables:
    print(" -", loc)

#%%

#%%
