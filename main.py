import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine, text

load_dotenv()

# SQL Alchemy connecting to Neon
engine = create_engine(
    os.getenv("DATABASE_URL"),
    pool_pre_ping=True
)

# Labor Statistics Annually
w2020a = pd.read_csv("data/raw/DSW2020A.csv",
                     usecols=["Areaname", "Periodyear", "OwnershipDesc", "Avgemp", "Avgwkwage"])
w2021a = pd.read_csv("data/raw/DSW2021A.csv",
                     usecols=["Areaname", "Periodyear", "OwnershipDesc", "Avgemp", "Avgwkwage"])
w2022a = pd.read_csv("data/raw/DSW2022A.csv",
                     usecols=["Areaname", "Periodyear", "OwnershipDesc", "Avgemp", "Avgwkwage"])
w2023a = pd.read_csv("data/raw/DSW2023A.csv",
                     usecols=["Areaname", "Periodyear", "OwnershipDesc", "Avgemp", "Avgwkwage"])
w2024a = pd.read_csv("data/raw/DSW2024A.csv",
                     usecols=["Areaname", "Periodyear", "OwnershipDesc", "Avgemp", "Avgwkwage"])

# Labor Statistics Quarterly
w2019q = pd.read_csv("data/raw/w2019Q.csv",
                     usecols=['year', 'qtr', "industry_title", 'industry_code', 'avg_wkly_wage'])
w2020q = pd.read_csv("data/raw/w2020Q.csv",
                     usecols=['year', 'qtr', "industry_title", 'industry_code', 'avg_wkly_wage'])
w2021q = pd.read_csv("data/raw/w2021Q.csv",
                     usecols=['year', 'qtr', "industry_title", 'industry_code', 'avg_wkly_wage'])
w2022q = pd.read_csv("data/raw/w2022Q.csv",
                     usecols=['year', 'qtr', "industry_title", 'industry_code', 'avg_wkly_wage'])
w2023q = pd.read_csv("data/raw/w2023Q.csv",
                     usecols=['year', 'qtr', "industry_title", 'industry_code', 'avg_wkly_wage'])
w2024q = pd.read_csv("data/raw/w2024Q.csv",
                     usecols=['year', 'qtr', "industry_title", 'industry_code', 'avg_wkly_wage'])

# labor_stats_all = pd.concat([w2020a, w2021a, w2022a, w2023a, w2024a], ignore_index=True)
# labor_stats_all.to_sql("Bernalillo County and ABQ MSA Labor Statistics", engine, if_exists='append', index=False)

# labor_stats_quarterly = pd.concat([w2019q, w2020q, w2021q, w2022q, w2023q, w2024q], ignore_index=True)
# labor_stats_quarterly.to_sql("Quarterly Albuquerque MSA Labor Statistics", engine, if_exists='replace', index=False)

#Ridership data
# riders = pd.read_csv("data/raw/UPTBigSheet.csv")
# riders_all = riders.iloc[1556:1559]

# riders_all.to_sql("City of Albuquerque Bus Ridership", engine, if_exists='append', index=False)




