# 🗺️ Système d’information géographique (SIG) des bassins cacaoyers camerounais
---
![Carte SIG des bassins cacaoyers du Cameroun](https://raw.githubusercontent.com/atchom/SIG_Cacao_Cameroun/54abd439ed675a48cca819ee990766b603ab3664/images/Map_cmr_SIG.png)

## 📌 Présentation du projet 

Le cacao représente une culture de rente majeure pour l'économie camerounaise, classant le Cameroun parmi les principaux producteurs mondiaux. Pourtant, les données géolocalisées précises sur les zones de production restent fragmentées, incomplètes ou difficilement accessibles.

**SIG_Cmr_Cacao** a pour ambition de combler cette lacune en proposant un recensement cartographique des localités productrices de cacao au Cameroun.

### Objectifs principaux

- 📍 **Recenser** les zones de production cacaoyère à partir de sources disponibles
- 🗺️ **Produire une carte géolocalisée** visualisant l'ensemble des localités identifiées
- 📊 **Structurer les données** dans un format SIG réutilisable
- 🔍 **Faciliter** l'analyse spatiale des bassins de production

---

## 📂 Structure des données

Le projet s'appuie sur un fichier CSV contenant une liste de localités camerounaises avec leurs coordonnées géographiques :

| Nom | Latitude | Longitude |
|-----|----------|-----------|
| Mamfe | 5.7897 | 9.3164 |
| Yaoundé | 3.8480 | 11.5021 |
| Kribi | 2.9500 | 9.9100 |
| Akwaya | 6.392 | 9.525 |
| Limbe | 4.083582 | 9.355073 |
| Kumba | 4.6443 | 9.4434 |

> ⚠️ **Note** : Le tableau ci-dessus présente un aperçu des données. L'intégralité des coordonnées géographiques des localités est disponible dans les documents sources en annexe.
---
### Visuel de l'Architecture Technique
![Architecture technique du projet](https://raw.githubusercontent.com/atchom/SIG_Cacao_Cameroun/92d8573100e6223ada07581c972f5214af1a2059/images/Architec.png)
## 🛠️ Technologies utilisées

### 1️⃣ Collecte des données

| Source | Description |
|--------|-------------|
| 📱 **UTM Geo Map** | Application mobile pour la capture des coordonnées GPS sur le terrain (localisation des parcelles cacaoyères) |
| 🛰️ **Données satellitaires** | Imagerie satellite pour l'identification des zones agricoles |
| 🔌 **Bases de données & API** | Sources externes (OpenStreetMap, données climatiques, etc.) |

### 2️⃣ Stockage & traitement
| Ordre | Outil | Usage |
|-------|-------|-------|
| 1 |🗄️ **UTM Geo Map** | Collecte des coordonnées GPS sur le terrain |
| 2 |📄 **CSV** | Format de stockage des données brutes |
| 3 |🐍 **Scripts Python** | Automatisation du nettoyage, géocodage et transformation des données |
| 4 | 🗄️ **PostgreSQL / PostGIS** | Base de données spatiale pour la gestion avancée des géodonnées |
| 5 | **QGIS** / **ArcGIS** | Logiciel SIG pour la manipulation et l'édition des données spatiales |

### 3️⃣ Analyse & visualisation

| Livrable | Description |
|----------|-------------|
| 📊 **Tableaux de bord** | Indicateurs clés sur la production cacaoyère par zone |
| 🗺️ **Cartes interactives** | Visualisations dynamiques (Folium, Leaflet) accessibles en ligne |
| 🌐 **Web SIG** | Publication interactive des cartes sur le web |
---
> 📁 **Accès aux sources** : L'ensemble des fichiers sources (scripts Python, données CSV, projet QGIS) nécessaire à l'implémentation de ce projet est disponible en **annexe**.
---
## 🗺️ Résultat : Carte finale des bassins cacaoyers
![Carte des zones cacaoyères du Cameroun](https://raw.githubusercontent.com/atchom/SIG_Cacao_Cameroun/main/images/Cameroun_Cacao_Map.png)
---
## 📝 Conclusion

Le projet **SIG_Cacao_Cameroun** a permis de recenser et de géolocaliser les principales zones de production cacaoyère au Cameroun. À partir de données terrain collectées via **UTM Geo Map**, enrichies par des scripts **Python** et structurées dans une base **PostgreSQL/PostGIS**, une carte finale a été produite sous **QGIS**.

### Principaux acquis

- ✅ **Base de données géolocalisée** : plus de 40 localités cacaoyères identifiées et cartographiées
- ✅ **Pipeline de traitement automatisé** : du CSV brut à la base de données spatiale
- ✅ **Carte exploitable** : visualisation claire des bassins de production
- ✅ **Documentation complète** : architecture, technologies, données

### Limites et axes d'amélioration

| Limite | Piste d'amélioration |
|--------|----------------------|
| Coordonnées manquantes pour certaines localités | Enrichissement via géocodage complémentaire ou enquêtes terrain |
| Données statiques (pas de mise à jour automatique) | Mise en place d'un flux ETL automatisé |
| Carte en version statique uniquement | Développement d'une carte interactive (Folium / Leaflet) |

### Perspectives

- 🌐 **Publication en ligne** : déployer la carte sur une plateforme Web SIG
- 📊 **Tableaux de bord** : ajouter des indicateurs (superficies, rendements, etc.)
- 🔄 **Mise à jour participative** : permettre aux producteurs et ONG d'enrichir la base

---

🌱 **Contribuer au projet** : Les contributions sont les bienvenues ! N'hésitez pas à proposer des compléments de données ou des améliorations techniques.
