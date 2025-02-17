import pandas as pd
from dateutil import parser


def load_data(filepath: str, type: str) -> pd.DataFrame:
    """read data in dataframe obj

    Args:
        filepath (str): file path

    Returns:
        pd.DataFrame: dataframe that contain data
    """
    try:
        return pd.read_csv(filepath) if type=="csv" else pd.read_json(filepath)
    except Exception as e:
        print(f"Error when reading file : {filepath} with exception : {e}")
        return
    
    
def normalize_date(date: str) -> str:
    """normalize date format

    Args:
        date (str): in put date

    Returns:
        str: _normalize date
    """
    
    try:
        return parser.parse(str(date)).strftime('%Y-%m-%d')
    except Exception as e:
        print(f"Error when normalizing date : {date} with exception : {e}")
        return None
        

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """data cleaning

    Args:
        df (pd.DataFrame): init loaded dataframe

    Returns:
        pd.DataFrame: cleaned dataframe
    """
    if 'date' in df.columns:
        df['date'] = df['date'].apply(normalize_date)
    return df


def link_search_for_drugs(drugs_df: pd.DataFrame, target_search_df: pd.DataFrame, traget_column: str, source: str) -> list[dict]:
    """search link for drugs in pubmed and clinical trials

    Args:
        drugs_df (pd.DataFrame): drugs
        target_search_df (pd.DataFrame): target_search (pubmed or clinical trials)
        traget_column (str) : traget column name
    Returns:
        list[dict]: finded links in dict
    """
    edges = []
    
    for _, drug_row in drugs_df.iterrows():
        drug_name = drug_row["drug"]
        
        matches = target_search_df[target_search_df[traget_column].str.contains(drug_name, case=False)]
        for _, row in matches.iterrows():
            edge = {
                "drug": drug_name,
                "journal": row['journal'],
                "source": source,
                "date": row['date']
            }
            edges.append(edge)
    return edges