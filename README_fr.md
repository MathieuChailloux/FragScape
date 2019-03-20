


# Aperçu

*FragScape* est un plugin QGIS 3.

Cet outil permet de calculer les indicateurs de fragmentation du paysage définis par Jaeger (Jaeger 2000). Parmi ces indicateurs, la taille effective de maille est très largement utilisée pour quantifier la fragmentation du paysage.

*FragScape* définit une procédure en 4 étapes depuis les données brutes jusqu’au calcul des indicateurs et permet de sauvegarder la configuration de l’outil afin de pouvoir reproduire les résultats.

*FragScape* a été développé par *Mathieu Chailloux* au sein d'[*IRSTEA*](http://www.irstea.fr), pour le [*centre de ressources Trame Verte et Bleue*](http://www.trameverteetbleue.fr/) 
(piloté par le [*Ministère de la Transition Écologique et Solidaire*](https://www.ecologique-solidaire.gouv.fr/)).

# Installation

Pour installer *FragScape*, QGIS 3.4 ou plus est nécessaire.
Aller dans le menu *Extension*, *Installer/Gérer les extensions*, activer les options expérimentales (onglet Paramètres) et *FragScape* doit être disponible. Une fois installé, une icône en forme de grille doît appraître dans la barre d'outils QGIS. Sinon, le plugin est disponible dans le menu *Extension*.

# Documentation

Documentation disponible:
 - [Notice d'utilisation de FragScape](https://drive.google.com/open?id=1OaOkH5cwcagcuvIPy10o6EhDiug8fAWG)

# Exemple

Des données d'exemple sont fournies avec le plugin ([lien](https://github.com/MathieuChailloux/FragScape/tree/qgis-lib-mc/sample_data/EPCI_Clermontais_2012))

Résultats avec la méthode CUT :

![CUT_GIF](https://drive.google.com/open?id=1e3Rr3ZzV1qeBwfKQevP-Tj9KtKbI68ZU)

Résultats avec la méthode CBC :

![CBC_GIF](https://drive.google.com/open?id=1e3Rr3ZzV1qeBwfKQevP-Tj9KtKbI68ZU)

Pour reproduire les résultats, cf section "Exemple" de la notice d'utilisation.
 
# Étapes

*FragScape* définit une procédure en 4 étapes :
 1. Définition des paramètres généraux
 2. Sélection des éléments d'occupation du sol
 3. Sélection des éléments fragmentants
 4. Calcul des indicateurs
    
Chaque étape est détaillé dans le panneau d'aide du plugin.

# Citation

> Chailloux, M. & Chéry, J.P. & Amsallem, J. (2019) FragScape : a QGIS plugin to quantify landscape fragmentation
    
# Liens
 - [Répertoire git de FragScape](https://github.com/MathieuChailloux/FragScape)
 - [IRSTEA](http://www.irstea.fr)
 - [AgroParisTech](http://www2.agroparistech.fr/)
 - [UMR TETIS](https://www.umr-tetis.fr)
 - [Centre de ressources Trame Verte et Bleue](http://www.trameverteetbleue.fr/)
 - [Ministère de la Transition Écologique et Solidaire](https://www.ecologique-solidaire.gouv.fr/)
