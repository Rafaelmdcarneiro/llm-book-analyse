
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
from llama_index.core import SimpleDirectoryReader

loader = SimpleDirectoryReader(
    input_dir="test",
    required_exts=[".epub"],
    recursive=True,
    exclude_hidden=False,


)

documents = loader.load_data()

from llama_index.llms.ollama import Ollama
#note you need to pull this cmd ollama pull llama2
#systemctl if you need to stop ollama - on initial install might already be running?
llama = Ollama(
    model="llama2",
    request_timeout=4000.0,
)

from llama_index.core import VectorStoreIndex

index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embedding_model,
)

query_engine = index.as_query_engine(llm=llama)

print(
    query_engine.query(
        "What are the titles of all the books available? Show me the context used to derive your answer."
    )
)

print(
    query_engine.query(
        "What is the name of the main organisation in the Christopher Anvil novel?"
    )
)


