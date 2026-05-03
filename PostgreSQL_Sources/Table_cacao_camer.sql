-- Creation de la base de donnees
Create database Sig_Cacao_cmr;
-- Activer l'extension PostGIS (si pas déjà fait)
CREATE EXTENSION IF NOT EXISTS postgis;

-- Supprimer la table si elle existe
DROP TABLE IF EXISTS cacao_cameroun;

-- Créer la table avec une colonne géométrique POINT
CREATE TABLE cacao_cameroun (
    id SERIAL PRIMARY KEY,
    region VARCHAR(50),
    departement VARCHAR(50),
    localite VARCHAR(100),
    geom GEOMETRY(POINT, 4326),  -- Colonne unique pour latitude/longitude
    type VARCHAR(20),
    poids_regional_pct DECIMAL(5,2),
    capacite_production_tonnes INTEGER,
    commentaire_rendement_transformation TEXT
);

