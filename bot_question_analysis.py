import cohere
import numpy as np
co = cohere.Client('rGKXRRqPj11SPhISUvJTsaEdOheEvZwEcqsocDWs')

# get the embeddings
phrases = ["i love soup", "soup is my favorite", "london is far away"]
(soup1, soup2, london) = co.embed(phrases).embeddings

# compare them
def calculate_similarity(a, b):
  return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print(calculate_similarity(soup1, soup2)) # 0.9 - very similar!
print(calculate_similarity(soup1, london)) # 0.3 - not similar!