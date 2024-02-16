from transformers import pipeline
pipe = pipeline(model="roberta-large-mnli")
pipe("This restaurant is awesome")