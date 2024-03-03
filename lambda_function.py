import pandas as pd

def lambda_handler(event, context):
    d = {'col1': [5,2], 'col2': [10,4]}
    df = pd.DataFrame(data=d)
    print(df)
