# Task 2 - T38 - HyperionDev SE Bootcamp

# Imports
from typing import List
import spacy

nlp = spacy.load('en_core_web_md')

# Read in text file to create dictionary of descriptions
movies_dict = dict
with open('./movies.txt', 'r') as movie_text:
    movies_stripped = [line.strip('\n') for line in movie_text.readlines()]
    movies_split: list[list[str]] = [line.split(' :') for line in movies_stripped]
    movies_dict = dict(movies_split)

# Set example description
model_dict = {
    "Planet Hulk": """
Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
the Illuminati trick Hulk into a shuttle and launch him into space to aplanet where the Hulk can live in peace.
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""
}


def view_next(movies: dict, model: dict) -> str:
    # Build description
    description = nlp(model['Planet Hulk'])
    # Build list of similarity values
    similarity_list = []
    for key, value in movies.items():
        similarity = nlp(value).similarity(description)
        similarity_list.append(similarity)
    # Sort list and find highest
    similarity_list_sorted = sorted(similarity_list)
    highest = similarity_list_sorted[-1]
    # Return this movie as a formatted string
    for key, value in movies.items():
        similarity = nlp(value).similarity(description)
        if similarity == highest:
            return f"{key}: {value} - {similarity}"


watch_next = view_next(movies_dict, model_dict)
print(watch_next)
