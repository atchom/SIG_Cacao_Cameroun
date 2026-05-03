
-- Supprimer la table temporaire
DROP TABLE IF EXISTS cacao_temp;

-- Index spatial (essentiel pour les requêtes géographiques)
CREATE INDEX idx_cacao_geom ON cacao_cameroun USING GIST (geom);

-- Index sur les colonnes fréquemment utilisées
CREATE INDEX idx_cacao_region ON cacao_cameroun(region);
CREATE INDEX idx_cacao_type ON cacao_cameroun(type);
CREATE INDEX idx_cacao_production ON cacao_cameroun(capacite_production_tonnes);