-- Adapter le chemin vers votre fichier
COPY cacao_temp(region, departement, localite, latitude, longitude, type, poids_regional_pct, capacite_production_tonnes, commentaire_rendement_transformation)
FROM 'C:\atchom\cacao_cmr_2025_geocodeB.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8'
NULL 'À renseigner';