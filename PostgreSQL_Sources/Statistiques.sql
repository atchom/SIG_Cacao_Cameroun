-- Statistiques générales
SELECT 
    COUNT(*) as total_enregistrements,
    COUNT(geom) as avec_coordonnees_gps,
    COUNT(*) - COUNT(geom) as sans_coordonnees,
    ROUND(COUNT(geom) * 100.0 / COUNT(*), 1) as pourcentage_geolocalise
FROM cacao_cameroun;

-- Afficher les 10 premiers enregistrements avec coordonnées
SELECT 
    id,
    region,
    departement,
    localite,
    ST_X(geom) as longitude,
    ST_Y(geom) as latitude,
    type,
    capacite_production_tonnes
FROM cacao_cameroun 
WHERE geom IS NOT NULL
LIMIT 10;

-- Afficher les enregistrements sans coordonnées
SELECT 
    region,
    departement,
    localite,
    type,
    capacite_production_tonnes
FROM cacao_cameroun 
WHERE geom IS NULL;

-- Résumé par région
SELECT 
    region,
    COUNT(*) as nb_localites,
    COUNT(geom) as nb_geolocalisees,
    SUM(capacite_production_tonnes) as production_totale_tonnes
FROM cacao_cameroun
GROUP BY region
ORDER BY production_totale_tonnes DESC NULLS LAST;