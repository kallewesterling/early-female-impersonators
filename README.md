# Early Female Impersonators

My current research examines boylesque, a contemporary genre of neo-burlesque performance. In a part of the project, I conduct inquiries into historical data, attempting to find queer foundational structures in popular entertainment through social network analysis.

The beginnings of this project was funded through a Connect New York (CNY) research grant in Summer 2018:[“Mapping Female Impersonators in _Billboard_’s and _Variety_’s Archives”](connectny.commons.gc.cuny.edu/2018/08/20/kalle-westerling). With the funding, I was able to begin creating a dataset that linked drag and “pansy” performers in New York City to burlesque theatres and nightclubs in the 1920s–30s. The research was primarily based on the archives of _Billboard_ and _Variety_ as they exist in their entire runs in ProQuest’s Entertainment Archive database. I also started mapping theatres and other venues where such performers regularly appeared.

## Processing ProQuest Data

To be able to sift through the search results in a database format without interruption, I constructed a script that created a local database consisting of the metadata from the thousands of articles in the search result files. The documentation for that script is available here: https://github.com/kallewesterling/process-entertainment-archive

## Datasets

I have for intention to make available my datasets in this repository on GitHub. However, moving the data from my local storage to GitHub is still in progress. In this repository's [`data`](https://github.com/kallewesterling/early-female-impersonators/tree/master/data) directory, I have made some of the raw data available. Note that it is messy and not readily available for automated data analysis if that is what you're looking for.

### Musicals101's historical theatres

During this project, I have also had to create datasets of historical theatres. One reliable source of information is Musicals101.com, a website that contains data on historical and Demolished Broadway Theatres, among much else. I created a script that takes the unstructured HTML information from the website and using some simple regular expressions, parses the data into different columns in a pandas DataFrame, which can then be exported to a CSV.

This repository contains [instructions](https://github.com/kallewesterling/early-female-impersonators/blob/master/README-Musicals101.md) for how to work with the package, the [package](https://github.com/kallewesterling/early-female-impersonators/blob/master/Musicals101.py) itself, as well as [a Jupyter notebook](https://github.com/kallewesterling/early-female-impersonators/blob/master/Musicals101%20worksheet.ipynb) that helps navigate the code and makes it easy to test it.

## Concerns

I have concerns with the privacy of the performers in the dataset. Regardless of whether they are still alive or not, there are prejudiced opinions about professions in art forms such as female impersonations, burlesque, and striptease. I want to make sure that the project provides some context to the data. The dataset, above all, will live in the digital component of my dissertation, which is still under construction.

As soon as the digital component of my dissertation is available, it will be linked here for easy access.