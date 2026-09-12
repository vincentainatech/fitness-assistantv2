import os
import pandas as pd
from minsearch import Index

def load_fitness_data():
    DATA_PATH = os.getenv("DATA_PATH", "../data/data.csv")
    df = pd.read_csv(DATA_PATH)
    documents = df.to_dict(orient="records")
    return documents

def build_index(documents):
    index = Index(
        text_fields=[
            "exercise_name",
            "type_of_activity",
            "type_of_equipment",
            "body_part",
            "type",
            "muscle_groups_activated",
            "instructions",
        ],
        keyword_fields=["id"],
    )
    index.fit(documents)
    return index

