from read_chunks import create_embedding
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd 
import requests
import numpy as np
import joblib
import json
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()
def inference(prompt):
    r = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
    )
    return r.text

df = joblib.load('embeddings.joblib')
incoming_query = input("Ask a question: ")
question_embedding = create_embedding([incoming_query])
similarities = cosine_similarity(np.vstack(df['embedding'].values), question_embedding).flatten()
top_results = 10
max_indices = similarities.argsort()[::-1][0:top_results]
print(max_indices)
new_df = df.loc[max_indices]

prompt = f''' i am teaching Self Knowledge - One Minute Series by Happy Thoughts Here are video chunks  containing video title ,video number,start time in seconds,end time in seconds,
text at that :{new_df[["title", "number", "start", "end", "text"]].to_json(orient="records")}
---------------------------------------------------
{incoming_query}
The user asked this question related to the video chunks ,you have to answer
where and how much content is taught where (in which video and what timestamp) and guide the user to go to 
that particular video. if user asks unrelated question  tell him you can only answer question related to the coding
'''

with open('prompt.txt', "w", encoding="utf-8") as f:
    f.write(prompt)

response = inference(prompt)
output_text = response

with open('response.txt', "w", encoding='utf-8') as f:
    f.write(output_text)

print(output_text)