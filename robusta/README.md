## python-pandas-dataframe-sample
*Generating 25% sample of data frame. In this example, 25% random sample data is generated out of the Data frame.*
```python
# importing pandas package
import pandas as pd
  
# making data frame from csv file 
data = pd.read_csv("employees.csv")
  
# generating one row 
rows = data.sample(frac =.25)
  
# checking if sample is 0.25 times data or not
  
if (0.25*(len(data))== len(rows)):
    print( "Cool")
    print(len(data), len(rows))
  
# display
rows
```
Refer: [python-pandas-dataframe-sample](https://www.geeksforgeeks.org/python-pandas-dataframe-sample/)


Refer: [python-call-function-from-another-file/](https://www.geeksforgeeks.org/python-call-function-from-another-file/)
Refer: [linear-regression-on-boston-housing-dataset-f409b7e4a155](https://towardsdatascience.com/linear-regression-on-boston-housing-dataset-f409b7e4a155)
