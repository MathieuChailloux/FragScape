
[TODO] est un plugin QGIS qui permet de calculer des indicateurs de fragmentation comme la taille effective de maille.

Ces indicateurs correspondent aux définitions proposées dans les articles 
"Jaeger, J. (2000). Landscape division, splitting index, and effective mesh size: New measures of landscape fragmentation. Landscape Ecology. 15. 115-130. 10.1023/A:1008129329289. 
"Moser, B. & al. (2007). Modification of the effective mesh size for measuring landscape fragmentation to solve the boundary problem. Landscape Ecology. 22. 447-459. 10.1007/s10980-006-9023-0. "

Le plugin inclut la préparation des données et se déroule donc en plusieurs étapes :
 1) Définition des paramètres généraux (territoire d'étude, projection, dossier de sortie, ...)
 2) Sélection et aggrégation des espaces étudiés (espaces naturels par exemple)
 3) Sélection des éléments fragmentants, application d'un tampon pour les éléments linéaires, 
    découpage du résultat de l'étape 2 par ces éléments fragmentants
 4) Calcul des indicateurs
 
