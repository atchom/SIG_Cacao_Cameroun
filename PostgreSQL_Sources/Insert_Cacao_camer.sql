-- Insertion avec conversion des coordonnées en format POINT PostGIS
INSERT INTO cacao_cameroun (
    region, 
    departement, 
    localite, 
    geom, 
    type, 
    poids_regional_pct, 
    capacite_production_tonnes, 
    commentaire_rendement_transformation
)
SELECT 
    region,
    departement,
    localite,
    -- Création du point (longitude, latitude) avec SRID 4326 (WGS84)
    CASE 
        WHEN latitude IS NOT NULL 
         AND latitude != ''
         AND latitude != 'À renseigner'
         AND longitude IS NOT NULL 
         AND longitude != ''
         AND longitude != 'À renseigner'
        THEN ST_SetSRID(ST_MakePoint(longitude::NUMERIC, latitude::NUMERIC), 4326)
        ELSE NULL
    END AS geom,
    type,
    -- Conversion du pourcentage (champ peut être vide)
    CASE 
        WHEN poids_regional_pct IS NOT NULL 
         AND poids_regional_pct != ''
        THEN poids_regional_pct::NUMERIC
        ELSE NULL
    END AS poids_regional_pct,
    -- Conversion de la capacité
    CASE 
        WHEN capacite_production_tonnes IS NOT NULL 
         AND capacite_production_tonnes != ''
        THEN capacite_production_tonnes::INTEGER
        ELSE NULL
    END AS capacite_production_tonnes,
    commentaire_rendement_transformation
FROM cacao_temp;