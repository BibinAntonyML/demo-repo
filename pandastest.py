import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9.1, 16.5, 12.77, 9.21, 20.22, 14.5, 11.34, 8.8, 19.13],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)
print("Original DataFrame:")
print(df)
print("\nData types of the columns of the said DataFrame:")
print(df.dtypes)
print("\nNow change the Data type of 'score' column from float to int:")
df.score = df.score.astype(int)
print(df)
print("\nData types of the columns of the DataFrame now:")
print(df.dtypes)