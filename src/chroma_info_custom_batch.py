import sys

model = sys.argv[1]
strq = sys.argv[2]
print("mode:",model,"query:",strq)
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
#from IPython.display import Markdown, display
import chromadb
from llama_index.llms.ollama import Ollama

from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core import QueryBundle
import pandas as pd
#from IPython.display import display, HTML

embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

chroma_path = "/mnt/usb_mount/chroma/Calibre Books"
collection_name = "calibrebooks"

# note on custom embed class to get around signature error
# https://stackoverflow.com/questions/77555461/facing-issue-while-running-chroma-from-documents-function

from chromadb.utils import embedding_functions
from chromadb import Documents, EmbeddingFunction, Embeddings
class MyEmbeddingFunction(EmbeddingFunction[Documents]):
    def __call__(self, input: Documents) -> Embeddings:
        sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="BAAI/bge-small-en-v1.5")
        embeddings = sentence_transformer_ef(input)
        return embeddings

custom = MyEmbeddingFunction()

def get_retrieved_nodes(
    query_str, vector_top_k=10, reranker_top_n=3, with_reranker=False
):
    query_bundle = QueryBundle(query_str)
    # configure retriever
    retriever = VectorIndexRetriever(
        index=index,
        similarity_top_k=vector_top_k,
    )
    retrieved_nodes = retriever.retrieve(query_bundle)

    if with_reranker:
        # configure reranker
        reranker = LLMRerank(
            choice_batch_size=5,
            top_n=reranker_top_n,
        )
        retrieved_nodes = reranker.postprocess_nodes(
            retrieved_nodes, query_bundle
        )

    return retrieved_nodes

def pretty_print(df):
    return display(HTML(df.to_html().replace("\\n", "<br>")))


def visualize_retrieved_nodes(nodes) -> None:
    result_dicts = []
    for node in nodes:
        result_dict = {"Score": node.score, "Text": node.node.get_text()}
        result_dicts.append(result_dict)

    #pretty_print(pd.DataFrame(result_dicts))
    print(pd.DataFrame(result_dicts))

new_nodes = get_retrieved_nodes(
    "What was the main organisation in Pandora's Legions by Christopher Anvil?",
    vector_top_k=3,
    with_reranker=False,
)

visualize_retrieved_nodes(new_nodes)

new_nodes = get_retrieved_nodes(
    "What was the main organisation in Pandora's Legions by Christopher Anvil?",
    vector_top_k=10,
    reranker_top_n=3,
    with_reranker=True,
)
print("LOAD CHROMA INDEX CHECK")

# load from disk
db2 = chromadb.PersistentClient(path=chroma_path)
#client = chromadb.PersistentClient(path="/path/to/save/to")
#collection = db2.get_collection(name=collection_name, embedding_function=embedding_model)
collection = db2.get_collection(name=collection_name, embedding_function=custom)

print(collection.count())


existing_count = collection.count()
batch_size = 400000
file_dict = {}
count = 0
for i in range(0, existing_count, batch_size):
    batch = collection.get(include=["metadatas", "documents", "embeddings"], limit=batch_size, offset=i)

    for b in batch:
        print(b)
    
    for x in range(len(batch["documents"])):
        # print(db.get()["metadatas"][x])
        doc = batch["metadatas"][x]
        #source = doc["source"]
        #print(doc)
        print(doc['file_name'])
        count += 1
        #break
        file_dict[doc['file_name']] = 1

    print(count)    

    print(file_dict)
    print(len(file_dict))
    #break

sorted_dict = dict(sorted(file_dict.items()))
for key in sorted_dict:
    print(key)    

print(len(sorted_dict), existing_count)    

import pickle
with open('book_dict.pkl','wb') as f:
    pickle.dump(sorted_dict, f)

