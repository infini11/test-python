import pandas as pd
import sys, os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from utils.helpers import (clean_data, link_search_for_drugs)

def clean_all_data_task(drugs_df: pd.DataFrame, pubmed_df: pd.DataFrame, clinical_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """clean all dataframe with non appriate date format

    Args:
        drugs_df (pd.DataFrame): drugs
        pubmet_df (_typd.DataFramepe_): pubmed
        clinical_df (pd.DataFrame): clinical trials

    Returns:
        tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]: return all cleaned dataframe obj
    """
    try :
        drugs_df_cleaned = clean_data(df=drugs_df)
        pubmed_df_cleaned = clean_data(df=pubmed_df)
        clinical_df_cleaned = clean_data(df=clinical_df)
        return (
            drugs_df_cleaned,
            pubmed_df_cleaned,
            clinical_df_cleaned
        )
    except Exception as e:
        print(f"Error when cleaning all file with exception : {e}")
        return
    

def create_graph_task(drugs_df: pd.DataFrame, pubmet_df: pd.DataFrame, clinical_df: pd.DataFrame) -> dict:
    """map liaison between data and generate graph

    Args:
        drugs_df (pd.DataFrame): drugs
        pubmet_df (_typd.DataFramepe_): pubmed
        clinical_df (pd.DataFrame): clinical trials

    Returns:
        dict: graph
    """
    
    drugs_edges_pubmed = link_search_for_drugs(
            drugs_df=drugs_df, 
            target_search_df=pubmet_df,
            traget_column="title",
            source="pubmed"
        )
    drugs_edges_clinical = link_search_for_drugs(
            drugs_df=drugs_df, 
            target_search_df=clinical_df,
            traget_column="scientific_title",
            source="clinical trials"
        )
    
    drugs_edges = drugs_edges_pubmed + drugs_edges_clinical
    
    return drugs_edges