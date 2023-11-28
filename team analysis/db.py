from sqlalchemy import create_engine
import pandas as pd

# All the database variables are stored here
db_username = "postgres"
db_password = "TitleistSwitch93!"
db_name = "postgres"
db_host = "db.qsptishlntxxmxhriunh.supabase.co"
db_port = "5432"
db_url = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"


def query_to_df(query):
    engine = create_engine(db_url)
    df = pd.read_sql(query, engine)
    return df
