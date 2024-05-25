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
# work out where we are up to
for d in documents:
    print(d)

print(len(documents))    