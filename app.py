import json, sys, os
import pandas as pd

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from tasks.hostpital_process import create_graph_task, clean_all_data_task
from utils.helpers import load_data


if __name__ == "__main__":
    
    drugs_df = load_data("data/drugs.csv", type="csv")
    pubmed_df = load_data("data/pubmed.csv", type="csv")
    pubmed_df_json = load_data("data/pubmed.json", type="json")
    clinical_df = load_data("data/clinical_trials.csv", type="csv")
    
    pubmed_df = pd.concat([pubmed_df, pubmed_df_json], ignore_index=True)
    
    cleaned_drugs_df, cleaned_pubmed_df, cleaned_clinical_df = clean_all_data_task(
            drugs_df=drugs_df,
            pubmed_df=pubmed_df,
            clinical_df=clinical_df
        )
    
    graph = create_graph_task(
            drugs_df=cleaned_drugs_df,
            pubmet_df=cleaned_pubmed_df,
            clinical_df=cleaned_clinical_df
        )
    
    with open('outputs/graph.json', 'w') as file:
        json.dump(graph, file, ensure_ascii=False, indent=4)
    
    
    

    
    