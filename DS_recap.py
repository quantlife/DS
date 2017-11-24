#Python
"""

 Variables and types:
  * variable
  * type(variable) - shows var type
  * bool, int, float, char
  * understanding pointers to vars
  * python lists: list of lists, subsetting lists, slising/dicing
    * copying lists
    * list methods
  * pyton dictionaries: create, access, manipulation
    * dictionary methods

 Logic control flow and filtering: and, or, not, if
 Loops: for, while

  Functions and packages:
   * Packages
   * different ways of importing
   * Functions
   * Methods

  NumPy:  -  great for doing vector arithmetic
   * NumPy Array
   * 2D NumPy Arrays  -  same datatype dataset
   * NumPy array stat methods

  Matplotlib:  -  plotting library
   * Line plot
   * Scatter plot
   * Histograms
   * Customization (labels, ticks, sizes, colors etc.)

  Pandas: - high level data manipulation tool, more high level compared to NumPy
    * importing pd.dataframe from csv, specifying index_col!!
    * indexing and selecting data from df
    * single brackets subsetting returns pandas.core.series.Series - 1D labelled array
    * double brackets subsetting returns proper DataFrame
    * loc/iloc

  Random walk simulation

"""
import pandas as pd
import numpy as np

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

my_dict = {'country': names, 'drives_right':dr, 'cars_per_cap':cpc }
print(my_dict)

df = pd.DataFrame({'cars_per_cap': [809, 731, 588, 18, 200, 70, 45],
                   'country': ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'],
                   'drives_right': [True, False, False, False, True, True, True]})
print(df)
df.index.names = [None]
df.set_index('country', inplace = True)
print(df)

print('____________________')
cars = pd.DataFrame(my_dict)
print(cars)
#cars.set_index('country', inplace = True)
cars.index = cars['country']
print(cars)

a = np.array([0, 1, 2])


print(a[:])
print(a.shape)
