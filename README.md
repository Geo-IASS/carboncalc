# carboncalc
Tools to calculate growth statistics for individual urban trees such as for estimating carbon storage.

This repository contains code to calculate greenhouse gas and emissions 
benefits of individual urban trees given data on parameters such as tree species, 
geographic region, tree diameter, and tree height. This work comes from a project funded by CalFire and the US Forest Service
to assess the benefits of California's urban trees, and builds upon a set of allometric equations for urban tree growth published 
as a USFS General Technical Report ([McPherson, Van Doorn, and Peper 2016](https://www.treesearch.fs.fed.us/pubs/52933)).

There are three major pieces in this repository. The first is the core Python code (biomass.py and growth.py connecting to the
SQLite database UrbanForestCC.sqlite) containing the functions for calculating tree biomass and growth. The second piece is
is contained in the directory ccshiny and is a prototype of a user interface to this calculator code developed using the R/Shiny 
platform. The third piece, contained in the directory carboncalc, is a RESTful API for querying the core calculator code, written
using the Django REST framework. This API is described in the document ccAPI.pdf.