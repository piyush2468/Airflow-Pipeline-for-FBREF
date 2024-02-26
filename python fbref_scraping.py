import pandas as pd
import psycopg2
import csv

df = pd.read_html('https://fbref.com/en/comps/9/Premier-League-Stats')

print(df[0].head())


# conn = psycopg2.connect("host=localhost dbname=fbref_pl user=postgres password=!ITCpwps1")
# cur = conn.cursor()
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:!ITCpwps1@localhost:5432/fbref_pl')
df[0].to_sql('premierleague', engine, if_exists='replace')