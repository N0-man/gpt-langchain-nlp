# Support for dataset retrieval with Hugging Face
from datasets import load_dataset
from constants import *

print('Loading Dataset from Hugging Face')
myDataset = load_dataset("leonweber/teaching_motivational_quotes", split="train")
phrases = myDataset["text"][:4000]

print('\n Generating Embeddings and storign into Astra DB')
myCassandraVStore.add_texts(phrases)
# Adding a delay to overcome the rate limie
# "Rate limit reached for default-text-embedding-ada-002"
# for detail in Details:
#     print("\n Writing dratils... ", detail[:10])
#     myCassandraVStore.add_texts([detail])
#     time.sleep(1)

print("Inserted %i Phrases.\n" % len(phrases))

