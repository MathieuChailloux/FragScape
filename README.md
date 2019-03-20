


# Overview

*FragScape* is a QGIS 3 plugin.

Its purpose is to compute landscape fragmentation metrics defined by Jaeger (Jaeger
2000). Among these metrics, effective mesh size has beenwidely used to quantify landscape fragmentation.

*FragScape* defines a 4 steps process from raw data to computed metrics and allow user to save configuration so that results can be reproduced with same context.

[comment]: <> (Below is an example of dispersal map created by *FragScape* :)
[comment]: <> (![dispEx](/docs/pictures/FragScapeExamplePicture.png))

It has been developped by *Mathieu Chailloux* at [*IRSTEA*](http://www.irstea.fr), 
on mission for the [*French ecological network resource center*](http://www.trameverteetbleue.fr/) 
(driven by [*French ministry of ecology*](https://www.ecologique-solidaire.gouv.fr/)).

# Installation

*FragScape* requires QGIS 3.
Go to plugins menu, install/manage plugins, activate experimental plugins and *FragScape* should be available.
Install it and a grid icon should appear. Otherwise, it is available in plugins menu.

# Documentation

Available documentation:
 - [FragScape User Guide](https://drive.google.com/open?id=1VxrRMjfpa1Kdf0ahqw9kWqvzhSLmAYDI)

# Example

Sample data is provided with plugin [here](https://github.com/MathieuChailloux/FragScape/tree/qgis-lib-mc/sample_data/EPCI_Clermontais_2012)

Results with CUT method :

![CUT_GIF](https://drive.google.com/open?id=1e3Rr3ZzV1qeBwfKQevP-Tj9KtKbI68ZU)

Results with Cross-Boundary Connection method :

![CBC_GIF](https://drive.google.com/open?id=1e3Rr3ZzV1qeBwfKQevP-Tj9KtKbI68ZU)

To reproduce above results, see "Example" section of User Guide.
 
# Steps

FragScape is a **4 steps** plugin :
 1. Parameters setting
 2. Land cover elements selection and preprocessing
 3. Fragmentation elements selection and preprocessing
 4. Metrics computation
    
Each step is detailed in plugin help panel.

# Quotation

> Chailloux, M. & Chéry J.P. & Amsallem, J. (2019) FragScape : a QGIS plugin to quantify landscape fragmentation
    
# Links
 - [FragScape git repository](https://github.com/MathieuChailloux/FragScape)
 - [IRSTEA](http://www.irstea.fr)
 - [AgroParisTech](http://www2.agroparistech.fr/)
 - [UMR TETIS](https://www.umr-tetis.fr)
 - [French ecological network resource center](http://www.trameverteetbleue.fr/)
 - [French ministry of ecology](https://www.ecologique-solidaire.gouv.fr/)

