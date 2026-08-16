import requests 
import json
import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib
def create_embedding(text_list):
    
        r = requests.post("http://localhost:11434/api/embed",json={
            "model":"bge-m3",
            "input":text_list
        })
        embedding = r.json()["embeddings"]
        return embedding
if "__name__"=="__main__":
    jsons = os.listdir("all_json")
    my_dicts =[]
    chunk_id = 0
    for jsin in jsons:
        input_path = os.path.join("all_json",jsin)
        with open(input_path,"r",encoding="utf-8") as f:
            content = json.load(f)
        print(f"creating embedding for {jsin}")
        embeddings =create_embedding( [c['text'] for c in content['chunks'] ])
        for i,chunk in enumerate(content["chunks"]):
                
                chunk['chunk_id'] = chunk_id
                chunk_id += 1
                chunk['embedding'] = embeddings[i]
                my_dicts.append(chunk)
                
        
                
    # print(my_dicts)
    df = pd.DataFrame.from_records(my_dicts)
    # save this dataframe
    joblib.dump(df,'embeddings.joblib')
