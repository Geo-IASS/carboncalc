# carboncalc
Tools to calculate growth statistics for individual urban trees such as for estimating carbon storage.

This repository contains code to calculate greenhouse gas and emissions 
benefits of individual urban trees given data on parameters such as tree species, 
geographic region, tree diameter, and tree height. This work comes from a project funded by CalFire and the US Forest Service
to assess the benefits of California's urban trees, and builds upon a set of allometric equations for urban tree growth published 
as a USFS General Technical Report ([McPherson, Van Doorn, and Peper 2016](https://www.treesearch.fs.fed.us/pubs/52933)).

There are three major pieces in this repository. The first is the core Python code (biomass.py and growth.py connecting to the
SQLite database UrbanForestCC.sqlite) containing the functions for calculating tree biomass and growth. The second piece, 
contained in the directory carboncalc, is a RESTful API for querying the core calculator code, written
using the Django REST framework. This API is described in the document ccAPI.pdf. Detailed instructions for installing and using 
the code are given below. The third piece is contained in the directory ccshiny and is a prototype of a user interface to this API 
developed using the R/Shiny platform. All contents of this repository are released into the public domain.

1. **Python carbon calculator code.**

   The key files here are biomass.py, growth.py, and UrbanForestCC.sqlite. To execute these Python modules, the libraries numpy
   scipy need to be installed. Also, the pathnames in both biomass.py and growth.py to the UrbanForestCC.sqlite database needs to 
   be changed to the correct location on one's system. Important functions in these modules are the following:

  * **biomass.py**: biomass_calc

  * **growth.py**: age_calc2, biomass_diff2, inv_age_calc2
  
2. **Django RESTful API**
   
   The files in the directory carboncalc contain the Python code for building a RESTful API to the functions in biomass.py and
   growth.py. Additionally the API supports calculating avoided emissions reductions from trees shading buildings. The API is
   described in the file ccAPI.pdf. This application has been developed using the Django REST framework, and Django experience 
   is needed to install and run this API. 


