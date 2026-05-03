-- Créer une table temporaire pour l'import brut
DROP TABLE IF EXISTS cacao_temp;

CREATE TEMP TABLE cacao_temp (
    region TEXT,
    departement TEXT,
    localite TEXT,
    latitude TEXT,
    longitude TEXT,
    type TEXT,
    poids_regional_pct TEXT,
    capacite_production_tonnes TEXT,
    commentaire_rendement_transformation TEXT
);