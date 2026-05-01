import pandas as pd
import re

# ============================
# 1) Fonction de réparation UTF-8 → Latin1
# ============================
def fix_encoding(text):
    if pd.isna(text):
        return text
    try:
        return text.encode("latin1").decode("utf-8")
    except:
        return text

# ============================
# 2) Fonction de nettoyage des noms
# ============================
def clean_name(name):
    if pd.isna(name):
        return ""
    name = str(name).lower().strip()
    name = re.sub(r"[éèêë]", "e", name)
    name = re.sub(r"[àâä]", "a", name)
    name = re.sub(r"[ôö]", "o", name)
    name = re.sub(r"[ïî]", "i", name)
    name = re.sub(r"[ùûü]", "u", name)
    name = re.sub(r"[ç]", "c", name)
    return name

# ============================
# 3) Chargement des fichiers
# ============================
fichier_cacao = r"C:\Qgis\cacao_cmr_2025.csv"  # fichier sans colonnes de geolocalisation
fichier_test = r"C:\Qgis\test_cameroun.csv"   # fichier avec des colonnes geo partiellement chargees
fichier_sortie = r"C:\Qgis\cacao_cmr_2025_geolocalise.csv"

def charger_csv(path):
    try:
        return pd.read_csv(path, sep=";", encoding="latin1")
    except:
        return pd.read_csv(path, sep=";", encoding="utf-8-sig")

cacao = charger_csv(fichier_cacao)
test = charger_csv(fichier_test)

print("📥 Fichiers chargés.")

# ============================
# 4) Correction des caractères corrompus
# ============================
for col in cacao.select_dtypes(include=["object", "string"]).columns:
    cacao[col] = cacao[col].apply(fix_encoding)

for col in test.select_dtypes(include=["object", "string"]).columns:
    test[col] = test[col].apply(fix_encoding)

print("🔤 Caractères spéciaux réparés.")

# ============================
# 5) Nettoyage des noms
# ============================
cacao["Localite"] = cacao["Localite"].astype(str).str.strip()
test["Nom"] = test["Nom"].astype(str).str.strip()

cacao["Localite_clean"] = cacao["Localite"].apply(clean_name)
test["Nom_clean"] = test["Nom"].apply(clean_name)

# ============================
# 6) Déduplication des localités avec coordonnées
# ============================
test_unique = (
    test.dropna(subset=["Latitude", "Longitude"])
        .query("Latitude != '' and Longitude != ''")
        .drop_duplicates(subset="Nom_clean", keep="first")
)

print("📌 Localités uniques prêtes pour la fusion.")

# ============================
# 7) Fusion
# ============================
cacao_geo = cacao.merge(
    test_unique[["Nom_clean", "Latitude", "Longitude"]],
    left_on="Localite_clean",
    right_on="Nom_clean",
    how="left"
)

cacao_geo = cacao_geo.drop(columns=["Localite_clean", "Nom_clean"])

# Réorganisation des colonnes
cols = cacao_geo.columns.tolist()
if "Latitude" in cols and "Longitude" in cols:
    idx = cols.index("Localite")
    cols.insert(idx + 1, cols.pop(cols.index("Latitude")))
    cols.insert(idx + 2, cols.pop(cols.index("Longitude")))
    cacao_geo = cacao_geo[cols]

# ============================
# 8) Export
# ============================
cacao_geo.to_csv(fichier_sortie, sep=";", index=False, encoding="utf-8-sig")

# ============================
# 9) Statistiques
# ============================
nb_geo = cacao_geo["Latitude"].notna().sum()
total = len(cacao_geo)
pct = nb_geo / total * 100

print("\n🎉 Fusion terminée !")
print(f"📍 Localités géolocalisées : {nb_geo} / {total} ({pct:.1f}%)")
print(f"📁 Fichier généré : {fichier_sortie}")

print("\n=== Aperçu des premières lignes géolocalisées ===")
print(cacao_geo[cacao_geo["Latitude"].notna()][["Localite", "Latitude", "Longitude"]].head(10).to_string())
