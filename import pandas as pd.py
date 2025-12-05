import pandas as pd

class_data = pd.read_csv("C:/Users/Patri/Downloads/class_data - Sheet1.csv")
class_data.head()

class_data['undergrad_major'].str.lower()

class_data['things_you_like'].unique()

class_data['things_you_like'].value_counts()

class_data.explode('things_you_like')
  

steve = class_data['things_you_like'].str.split(", ")


steve.explode('things_you_like')['things_you_like'].value_counts().head(10)
