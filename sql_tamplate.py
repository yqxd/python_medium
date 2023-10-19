import pandas as pd
from pandasql import sqldf

data = {
    'id': [1, 2, 3],
    'salary': [100, 200, 300]
}
df = pd.DataFrame(data)

##
query = """
select * from df;
"""

print(sqldf(query))
