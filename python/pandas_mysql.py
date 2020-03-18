import pandas as pd
import sqlalchemy as sa
import mysql.connector as myconn

# DB setting
# url = 'localhost:3306'
url = 'mysql+pymysql://root:@localhost:3306/sakila?charset=UTF8MB4'
engine = sa.create_engine(url, echo=False)

# set query
# query = "select * from sakila.actor"

# read data
# df = pd.read_sql(query, con = engine)

# prepare df
df = pd.DataFrame({ 'id' : 2.,
                    'name' : 'harayama',
                    'price' : 200. },
                    index = [2, ])
# print(df.head)

# insert1 
df.to_sql('test_table', engine, index=True, if_exists='replace')


