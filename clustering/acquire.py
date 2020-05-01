import pandas as pd
import numpy as np
import env

def get_db_url(database):
    from env import host, user, password
    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    return url

def get_zillow_data():
    query = """
    SELECT * FROM properties_2017
    RIGHT JOIN `predictions_2017` USING (`parcelid`)
    LEFT JOIN `architecturalstyletype` USING (`architecturalstyletypeid`) 
    LEFT JOIN `buildingclasstype` USING (`buildingclasstypeid`)
    LEFT JOIN `heatingorsystemtype` USING (`heatingorsystemtypeid`)
    LEFT JOIN `propertylandusetype` USING (`propertylandusetypeid`)
    LEFT JOIN `storytype` USING (`storytypeid`)
    LEFT JOIN `airconditioningtype` USING (`airconditioningtypeid`)
    LEFT JOIN `typeconstructiontype` USING (`typeconstructiontypeid`) 
    WHERE properties_2017.latitude IS NOT NULL OR  properties_2017.longitude IS NOT NULL
    """
    df = pd.read_sql(query, get_db_url('zillow'))
    return df


def get_iris_data():
    query = """
    SELECT * 
    FROM `measurements`
    JOIN species USING (species_id)
    """
    df = pd.read_sql(query, get_db_url("iris_db"))
    return df