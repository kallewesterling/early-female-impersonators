# Musicals101 Parser script

This script is made to parse the data on historical and Demolished Broadway Theatres available on [Musicals101.com](https://www.musicals101.com/bwaypast.htm).

It takes the unstructured HTML information from the website and using some simple regular expressions, is able to parse the data into different columns in a pandas DataFrame, which can then be exported to a CSV.

Here is an example of how I work with the script ([`Musicals101.py`](https://github.com/kallewesterling/early-female-impersonators/blob/master/Musicals101.py)):

## 1. Import packages

We need a couple of packages to be able to work with this script:

```python
import requests
import pandas as pd
from bs4 import BeautifulSoup
```

*If you do not have those installed, you can install them by running `pip install pandas` and `pip install beautifulsoup4`*

Next, we want to make sure to import the Musicals101 package:

```python
from Musicals101 import ParseTheatreInfo
```

## 2. List the URLs containing information

```python
urls = [
    'https://www.musicals101.com/bwaypast.htm',
    'https://www.musicals101.com/bwaypast1b.htm',
    'https://www.musicals101.com/bwaypast2.htm',
    'https://www.musicals101.com/bwaypast3.htm',
    'https://www.musicals101.com/bwaypast3b.htm',
    'https://www.musicals101.com/bwaypast4.htm',
    'https://www.musicals101.com/bwaypast5.htm',
    'https://www.musicals101.com/bwaypast6.htm'
]
```

## 3. Set up an empty list container

```python
_ = []
```

## 4. Loop through the URLs and get all the content

```python {.line-numbers}
for url in urls:
  # Download all the contents
  q = requests.get(url)

  # Let BeautifulSoup handle the HTML content
  soup = BeautifulSoup(q.content)

  # Search for all headings <h3> in the code
  h3 = soup.find_all('h3')

  # Loop through each heading:
  for h in h3:
    # As we know that the <p> element that follows each <h3> contains our info, we assign that to our variable
    info = h.find_next_sibling()

    # Make sure we have information; otherwise exit the loop
    if info is None: continue

    # Here is where we get the data from the `Musicals101` package
    theatre = ParseTheatreInfo(info.text)

    # theatre.data is the dictionary that contains all the parsed information. We will add to it three additional key-value pairs:
    theatre.data['name'] = h.text # The name of the theatre
    theatre.data['reference'] = theatre.reference # In case the block refers to another theatre
    theatre.data['original_text'] = info.text # All the original plain text from the block

    # Finally, add the data onto the list of dictionaries set up under (3)
    _.append(theatre.data)
```

## 5. Create a DataFrame and export the CSV

Using `pandas`, we take the list of dictionaries created in (4) above and use their native function for exporting a CSV file:
```python
df = pd.DataFrame.from_dict(_)
df.to_csv('musicals101.csv')
```

**The resulting file is available [here](https://github.com/kallewesterling/early-female-impersonators/blob/master/data/musicals101.csv) for reference.**

# Entire code

I have made the entire code for the instructions above available as an [Jupyter notebook](https://jupyter.org/) here:

https://github.com/kallewesterling/early-female-impersonators/blob/master/Musicals101%20worksheet.ipynb

Feel free to fork this repository and play around with it, if you would like.