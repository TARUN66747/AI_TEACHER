# How to use this RAG AI Teaching assistent on your own data

## Step-1 - Collect your videos
Move all your video files to the videos folder

## step-2 - convert to mp3
Convert all the video files to mp3 by running process_ideos.py

## step-3 -mp3 to json
Convert all the mp3 file to json by running spt2

## step-4 - convert the json files to vector
Use the file read_chunks to convert the json files to embeddings and save it to joblib pickle

## step - 5 
read the joblib file and load the memory.then create a relevent prompt as per the user query and feed to the llm