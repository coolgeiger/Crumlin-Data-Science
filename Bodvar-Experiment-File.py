# Bodvar test file to be sent via Github to Stefan.

import pandas as pd

python_list = [['Dog', 'Bailey', 0],
                ['Dog', 'Noodles', 45],
                ['Bulldog', 'Luigi', 40],
                ['Dog', 'Pickles', 100],
                ['Dog', 'Badger', 15],
                ['Dog', 'Rex', 30],
                ['Bird', 'Anastasia', 11],
                ['Cat', 'Sugar', 0]]

pandas_pets = pd.DataFrame(python_list, columns = ['Pet', 'Name', 'Height'])

# print(pandas_pets.head())
# print(pandas_pets.describe())
print(pandas_pets[['Name','Height']])