import pandas
import math

def calculator(path, index):
    df = pandas.read_excel(path)
    x = float(df['Price'][index])
    y = float(input('Enter y:'))
    result = math.pow((x / y), 2)
    return round(result)