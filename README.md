
New in *FragScape 2.0* :
 - Raster mode
 - Algorithm to compare 2 results layers

# Overview

*FragScape* is a QGIS 3 plugin.

Its purpose is to compute landscape fragmentation metrics defined by Jaeger (Jaeger
2000). Among these metrics, effective mesh size has been widely used to quantify landscape fragmentation.

*FragScape* defines a 4 steps process from raw data to computed metrics and allow user to save configuration so that results can be reproduced with same context.

It has been developped by *Mathieu Chailloux* at [*INRAE*](http://www.inrae.fr), for the [*French ecological network resource center*](http://www.trameverteetbleue.fr/) 
(driven by [*French ministry of ecology*](https://www.ecologique-solidaire.gouv.fr/)).

# Installation

*FragScape* requires QGIS 3.
Go to plugins menu, install/manage plugins, activate experimental plugins and *FragScape* should be available.
Install it and a grid icon should appear. Otherwise, it is available in plugins menu.

# Documentation

Available documentation:
 - [FragScape User Guide](https://github.com/MathieuChailloux/FragScape/blob/master/docs/FragScape_UserGuide_en.pdf)

# Example

Sample data is provided with plugin [here](https://github.com/MathieuChailloux/FragScape/tree/qgis-lib-mc/sample_data/EPCI_Clermontais_2012)

Results with CUT method :

<img src="https://github.com/MathieuChailloux/FragScape/blob/master/docs/gifs/CUT.gif?raw=True" width="500"/>

Results with Cross-Boundary Connection method :

<img src="https://github.com/MathieuChailloux/FragScape/blob/master/docs/gifs/CBC.gif?raw=True" width="500"/>

To reproduce above results, see "Example" section of User Guide.
 
# Steps

FragScape is a **4 steps** plugin :
 1. Parameters setting
 2. Land cover elements selection and preprocessing
 3. Additional data selection and preprocessing
 4. Metrics computation
    
Each step is detailed in plugin help panel.

# Contact

Mathieu Chailloux (INRAE/UMR TETIS)- *mathieu.chailloux@inrae.fr*

Jennifer Amsallem(INRAE/UMR TETIS) - *jennifer.amsallem@inrae.fr*

Jean-Pierre Chéry (AgroParisTech/UMR TETIS) - *jean-pierre.chery@teledection.fr*

# Quotation

> Chailloux, M. & Chéry, J.P. & Amsallem, J. (2019) FragScape : a QGIS plugin to quantify landscape fragmentation
    
# Links
 - [FragScape git repository](https://github.com/MathieuChailloux/FragScape)
 - [INRAE](http://www.inrae.fr)
 - [AgroParisTech](http://www2.agroparistech.fr/)
 - [UMR TETIS](https://www.umr-tetis.fr)
 - [French ecological network resource center](http://www.trameverteetbleue.fr/)
 - [French ministry of ecology](https://www.ecologique-solidaire.gouv.fr/)

