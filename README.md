# Piscine Data Science - Analyse complète des 5 modules

## MODULE 0 - Création de base de données
**Rôle**: Data Engineer - Infrastructure

**Objectif**: Setup PostgreSQL et import CSV  
**Contexte**: Premier jour en e-commerce, analyser 4 mois de ventes (Oct 2022 - Fév 2023)

### Exercices
- **Ex00**: PostgreSQL via Docker Compose ou VM
- **Ex01**: Outil de visualisation DB (pgAdmin, DBeaver...)
- **Ex02**: Créer table depuis CSV (≥6 types de données, DATETIME obligatoire)
- **Ex03**: Script automatique pour tous les CSV du dossier `customer/`
- **Ex04**: Table items depuis `items.csv` (≥3 types de données)

**Livrables**: `docker-compose.yml`, `table.*`, `automatic_table.*`, `items_table.*`

---

## MODULE 1 - Data Warehouse
**Rôle**: Data Engineer - ETL

**Objectif**: Fusionner et nettoyer les données

### Exercices
- **Ex00**: Outil de visualisation (répété)
- **Ex01**: Fusionner toutes les tables `data_202*` → table unique `customers`
- **Ex02**: Supprimer doublons exacts + doublons à 1 seconde d'intervalle (bug serveur)
- **Ex03**: Joindre `customers` + `items` **sans perte d'information**

**Avertissement critique** (répété 3×): "Attention, mauvais nettoyage = bloqué plus tard"

**Livrables**: `customers_table.*`, `remove_duplicates.*`, `fusion.*`

---

## MODULE 2 - Data Viz
**Rôle**: Data Analyst - Reporting et visualisation

**Objectif**: Analyser et segmenter les clients  
**Période**: Oct 2022 - Fév 2023 (ajout février vs versions initiales)

### Exercices
- **Ex00**: Pie chart des `event_type`
- **Ex01**: 3 graphiques sur achats uniquement (`event_type='purchase'`)
  - Line: nombre de clients
  - Bar: total ventes en millions Â (Altairian Dollars)
  - Area: panier moyen
- **Ex02**: Statistiques descriptives + 2 box plots (prix items, panier moyen)
- **Ex03**: 2 bar charts (fréquence commandes, dépenses par segment)
- **Ex04**: Elbow method pour clustering (justifier nombre de clusters)
- **Ex05**: Clustering clients (≥4 groupes: nouveaux, inactifs, tiers fidélité)  
  Minimum 2 visualisations

**Livrables**: `pie.*`, `chart.*`, `mustache.*`, `Building.*`, `elbow.*`, `Clustering.*`

---

## MODULE 3 - The Present
**Rôle**: Data Scientist - Exploration

**Objectif**: Analyse exploratoire et preprocessing  
**Contexte**: Star Wars - prédire Jedi vs Sith depuis compétences des chevaliers

### Exercices
- **Ex00**: Histogrammes multi-features sur `Test_knight.csv`
- **Ex00 (suite)**: Histogrammes avec séparation Jedi/Sith sur `Train_knight.csv`
- **Ex01**: Corrélation features vs target (ranking)
- **Ex02**: 4 scatter plots (Train + Test) × (clusters séparés + mélangés)
- **Ex03**: Standardization (z-score) + print + graphique
- **Ex04**: Normalization (min-max) + print + graphiques
- **Ex05**: Split `Train_knight.csv` → `Training_knight.csv` + `Validation_knight.csv`  
  Justifier le ratio choisi

**Livrables**: `Histogram.*`, `Correlation.*`, `points.*`, `standardization.*`, `Normalization.*`, `split.*`

---

## MODULE 4 - The Future
**Rôle**: Data Scientist - Machine Learning

**Objectif**: Prédiction supervisée Jedi/Sith  
**Dépendances**: Fichiers du Module 3 (`Training_knight.csv`, `Validation_knight.csv`)

### Exercices
- **Ex00**: **BLOQUANT** - Confusion matrix (calculs manuels, pas de lib)  
  Output: precision, recall, f1-score, accuracy, matrice 2×2
- **Ex01**: Heatmap de corrélation entre features
- **Ex02**: PCA - Variance par composante + cumulative (objectif 90%)
- **Ex03**: VIF (Variance Inflation Factor) - Feature selection pour VIF < 5
- **Ex04**: Decision Tree ou Random Forest  
  - Graphique de l'arbre
  - `Tree.txt` avec prédictions
  - **F1-score ≥ 90%**
- **Ex05**: K-Nearest Neighbors  
  - Graphique accuracy vs k-values
  - `KNN.txt` avec prédictions
  - **F1-score ≥ 92%**
- **Ex06**: Voting Classifier (combiner 3 modèles)  
  - `Voting.txt` avec prédictions
  - **F1-score ≥ 94%**

**Livrables**: `Confusion_Matrix.*`, `Heatmap.*`, `variances.*`, `Feature_Selection.*`, `Tree.*`, `KNN.*`, `democracy.*`

---

## PIPELINE COMPLET

```
MODULE 0: PostgreSQL setup + CSV import
    ↓
MODULE 1: ETL (merge, deduplicate, join)
    ↓
MODULE 2: Analytics (viz, clustering, segmentation)
    ↓
MODULE 3: EDA (correlation, scaling, split)
    ↓
MODULE 4: ML (classification, ensemble, 90→94% f1-score)
```

## POINTS CRITIQUES

**Module 0-1**: Nettoyage essentiel pour la suite  
**Module 2**: Premier contact avec segmentation métier  
**Module 3**: Preprocessing obligatoire pour Module 4  
**Module 4 Ex00**: Échec = fin d'évaluation  
**Progression**: Performance ML croissante (90% → 92% → 94%)
