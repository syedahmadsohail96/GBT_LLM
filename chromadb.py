import chromadb

chroma_client = chromadb.Client()

collection = croma_client.create_collection(name = "my_collection")

collection.add(
    document = ["my name is ahmad","my name is not ahmad"],
    metadatas = [{"source":"name is true"},{"source":"my name is not true"}],
    ids= ["id1","id2"]
)

results = collection.query(
    query_texts= ['what is my name'],
    n_results = 1
)

print(results)



