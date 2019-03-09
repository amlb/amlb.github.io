# 12 Décembre 2018
- Animateur: Arnaud Gaillot
- Question concrète: Comment prédire la nature des sédiments marins avec le machine learning?
- Méthode machine learning: Random Forest
- Dataset formatté et benchmarké: Modèle hydrodynamique, bathymétrie et ses dérivées, réflectivité acoustique, prélèvements sédimentaires (Baie de Somme)

## Présentation
[alloha_20181212_classifsedim_randomforrest.pdf](https://github.com/amlb/amlb.github.io/blob/master/2018-12-12_RandomForests/alloha_20181212_classifsedim_randomforrest.pdf)

## Notebooks et fichiers data:
- [infos.txt](https://github.com/amlb/amlb.github.io/blob/master/2018-12-12_RandomForests/infos.txt) : un fichier readme, explicitant le contenu des champs du premier fichier, les paramètres de calculs des variables dérivées et les statistiques employées pour leur calcul.
- [prediction_sedimentaire_IFREMER.csv](https://github.com/amlb/amlb.github.io/blob/master/2018-12-12_RandomForests/prediction_sedimentaire_IFREMER.csv) : les données de prédiction.

**Détails :** le fichier **prediction_sedimentaire_IFREMER.csv**, contient autant de lignes que de prélèvements sédimentaires sur la zone (soit 67). En résumé, pour chaque prélèvement on a :
- les résultats d'analyse granulométrique (colonnes "FID" jusqu'à "CLAS_LARSO")
- les variables dérivées de la bathymétrie (colonnes "bathy" jusqu'à "VRM19")
- les variables dérivées de la réflectivité acoustique (colonnes "BSmn" jusqu'à "RatioRGsd")
- les variables dérivées des modèles d'océanographie physique (colonnes "hs_mean" jusqu'à "ubr_d_max")
- les variables à prédire ( colonnes "alrm" et "alrs")
