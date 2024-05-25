from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
#from IPython.display import Markdown, display
import chromadb
from llama_index.llms.ollama import Ollama

embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
from llama_index.core import SimpleDirectoryReader

input_path = "/mnt/usb_mount/output/Calibre Books"
#input_path="test"

print("LOADING CALIBRE BOOKS in epub")

loader = SimpleDirectoryReader(
    input_dir=input_path,
    required_exts=[".epub"],
    recursive=True,
    exclude_hidden=False,

)

documents = loader.load_data()
#Extending the previous example, if you want to save to disk, simply initialize the Chroma client and pass the directory where you want the data to be saved to.
#Caution: Chroma makes a best-effort to automatically save data to disk, however multiple in-memory clients can stomp each other's work. As a best practice, only have one client per path running at any given time.

print("CHROMA DB CREATION")

# save to disk
chroma_path = "/mnt/usb_mount/chroma/Calibre Books"
collection = "calibrebooks"

db = chromadb.PersistentClient(path=chroma_path)
chroma_collection = db.get_or_create_collection(collection)
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

print("CHROMA VECTOR INDEX CREATION")

index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embedding_model
)

print("LOAD CHROMA INDEX")

# load from disk
db2 = chromadb.PersistentClient(path=chroma_path)
chroma_collection = db2.get_or_create_collection(collection)
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
index = VectorStoreIndex.from_vector_store(
    vector_store,
    embed_model=embedding_model,
)

if 1 == 2:
    # Query Data from the persisted index
    query_engine = index.as_query_engine()
    response = query_engine.query("What did the author do growing up?")
    display(Markdown(f"<b>{response}</b>"))

print("SAMPLE QUERIES")

llama = Ollama(
    model="llama2",
    request_timeout=4000.0,
)

if 1 == 2:
    index = VectorStoreIndex.from_documents(
        documents,
        embed_model=embedding_model,
    )

query_engine = index.as_query_engine(llm=llama)

print(
    query_engine.query(
        "Please summarise the Christopher Anvil novel Pandora's Legions"
    )
)

print(
    query_engine.query(
        "What is the name of the main organisation in the Christopher Anvil novel?"
    )
)


