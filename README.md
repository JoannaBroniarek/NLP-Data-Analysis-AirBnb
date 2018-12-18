# Find the perfect place to stay in Texas!
Joanna Broniarek, Alice Shirinà, Daniele Sanna.

<p align="center">
<img src="https://hd.tudocdn.net/731085?w=646&h=284">
</p>

**The homework consists in analyzing the text of Airbnb property listings and building two different Search Engines that, given as input a query, return the houses that match the query.**

## Data Source
* Airbnb_Texas_Rentals.csv
```https://www.kaggle.com/PromptCloudHQ/airbnb-property-data-from-texas```

## Jupyter Notebooks Descriptions
1. **Homework_3.ipynb** - This jupyter notebook contains the implementation of Search_Engine_1,  Search_Engine_2 and the definition of scoring functions. Some of the used functions are located in the function.py file. 

  For correct working of Search Engines it is necessary to run Creating_Files.ipyn notebook. 
  Search Engine 1 is using "vocabulary.txt", "inv_indx.txt" files.
  Search Engine 2 is using "vocabulary.txt", "inv_indx_tfidf.txt" files.

2. **Creating_Files.ipynb** - In this notebook we create and save the following files "vocabulary.txt", "inv_indx.txt", "inv_indx_tfidf.txt" according to the data. 

3. **GeoMap.ipynb**  - There is an implementation of the Geomap for searching documents according to their locations. Example of the map is in the file **Visualization.html**

## Scripts
 1. functions.py - external file with definitions of functions used in the Homework_3 notebook.
 
 ## Technology
 + Python3
