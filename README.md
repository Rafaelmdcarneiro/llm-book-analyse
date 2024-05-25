# book-mentat
Considering how to analyse book collections, Large Language Model style

# Motivation
- Get all the good spaceship names
- Finding old stories you have forgotten
- References found
- State of the art models for a current mineral exploration problem

# Problem
## Library
- Consider an extensive ebook library that is decades old
### Formats
    - text
    - html
    - rtf
    - prc
    - mobipocket
    - epub
    - pdf
    - cbz / cbr

### Origin
    - Not all digital native
        - Failure OCR - what is open source state of the art
        - If on windows - robocopy multithreaded is useful robocopy "C:\Users\bananasplits\OneDrive\Calibre Books" "D:\books\Calibre Books" /MIR /MT:16

### Type
- Fiction
- Non-fiction
- Games
- Academic
    - Papers etc    
- Code
    - Many languages

### Modality
- Do you want covers?
- Diagrams from non-fiction
- Pictures [or comic strips] from games
- Actual comics
    - 2000 AD, Image, Humble Bundles have CBR/CBZ possibilities

### Current State
- Calibre https://calibre-ebook.com/

### Prior Art
#### epub
- https://huggingface.co/learn/cookbook/en/rag_llamaindex_librarian
- https://github.com/huggingface/cookbook/blob/main/notebooks/en/rag_llamaindex_librarian.ipynb
- https://www.bitsgalore.org/2023/03/09/extracting-text-from-epub-files-in-python
    - https://github.com/RichardScottOZ/textExtractDemo
#### comics
- https://linnk.ai/insight/comics-analysis/multimodal-transformer-for-comics-text-cloze-enhancing-narrative-understanding-in-comics-analysis-f7rPlZEc/
    - paper https://arxiv.org/pdf/2403.03719

# Approach
- Clearly will need some sort of Retrieval Augmented Generation

## Data
### Calibre Libraries
- Currently a folder with metadata, db and a folder per 'author' - which is not important, but is the structure

## Technology
### Storage
- Is in memory ok if run on a decent server
- A books library example
```bash
.azw: 12
.azw3: 234
.azw4: 2
.db: 2
.doc: 1
.docx: 1
.epub: 1567
.htmlz: 6
.jpg: 9829
.json: 1
.lit: 2
.lrf: 2
.mobi: 10054
.opf: 10891
.original_epub: 20
.pdb: 9
.pdf: 102
.prc: 315
.rar: 18
.rtf: 9
.txt: 28
.zip: 17
```
### Calibre
- use this for conversion 
    - ubuntu has an apt package

### ollama
- install https://ollama.com/download/linux
    - curl -fsSL https://ollama.com/install.sh | sh
- models: https://ollama.com/library    
- operation https://github.com/ollama/ollama/issues/707
```bash
>>> Creating ollama user...
>>> Adding ollama user to render group...
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
>>> Enabling and starting ollama service...
Created symlink /etc/systemd/system/default.target.wants/ollama.service → /etc/systemd/system/ollama.service.
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
WARNING: No NVIDIA/AMD GPU detected. Ollama will run in CPU-only mode.
```

### Llamaindex
#### Simple Directory Reader
- https://docs.llamaindex.ai/en/v0.9.48/examples/data_connectors/simple_directory_reader.html
- Readers https://github.com/run-llama/llama_index/tree/main/llama-index-integrations/readers/llama-index-readers-file
- Vector Stores https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/

#### Reranker
- https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LLMReranker-Gatsby/

### Chroma
- https://docs.trychroma.com/
    - is multimodal
- installation https://docs.trychroma.com/getting-started
- vector store installation pip install llama-index-vector-stores-chroma
- embedding speed https://www.youtube.com/watch?v=7FvdwwvqrD4&ab_channel=JohnnyCode
- examples -
    - https://thenewstack.io/exploring-chroma-the-open-source-vector-database-for-llms/

### Tokenisers
- ?

### Models
- Text
- Multimodal - Llava?
- Model Storage https://github.com/ollama/ollama/issues/1737

- https://ollama.com/library
- ollama pull llama2
- ollama run llama3
- etc
## Ollama



# Errors
## bind address already in use
- https://github.com/ollama/ollama/issues/707
- Hey all, not seeing ollama in the output of lsof could be a permissions issue. When you install ollama on linux via the install script it creates a service user for the background process. You may need to stop the process via systemctl in that case.

Here is some troubleshooting steps that will hopefully help:

Stop the background service: 
```bash
sudo systemctl stop ollama
```

Run lsof as sudo to rule out permissions issues: 
```bash
sudo lsof -i :11434
```

# Embeddings
- multi GPU approach
- https://github.com/UKPLab/sentence-transformers/blob/master/examples/applications/computing-embeddings/computing_embeddings_multi_gpu.py
- Chroma will do multimodal

# Tips
- https://thenewstack.io/exploring-chroma-the-open-source-vector-database-for-llms/
- sqlite3 linux package can be used to check pragma basics etc.

# Layout
- discussion https://www.reddit.com/r/LocalLLaMA/comments/1brk3qo/pdf_to_json_for_rag_through_multimodal_models/
- Llava?
- layoutlm https://huggingface.co/docs/transformers/en/model_doc/layoutlm
- grobid https://grobid.readthedocs.io/en/latest/Introduction/
- LlamaParse https://medium.com/@salujav4/parsing-pdfs-text-image-and-tables-for-rag-based-applications-using-llamaparse-llamaindex-0f4c5ed50fb7
    - https://colab.research.google.com/drive/1aUPywCH92XLNpdjkmXz3ff8H-QnT2JHZ?usp=sharing
- Unstructured https://github.com/Unstructured-IO
## Tables
- https://github.com/parsee-ai/parsee-pdf-reader
- TableTransformer

## PDF
- PyMuPDF
- PDFMiner.six
- Camelot
- PyPDF2
- pikepdf https://github.com/RichardScottOZ/pikepdf

## OCR
- tesseract https://tesseract-ocr.github.io/tessdoc/Installation.html

## Parsee pdf
- https://github.com/parsee-ai/parsee-pdf-reader
- pdf reader conflicts
- Installing collected packages: pytesseract, pypdf, pycparser, pdf2image, opencv-python, cffi, cryptography, pdfminer-six, parsee-pdf-reader
  Attempting uninstall: pypdf
    Found existing installation: pypdf 4.2.0
    Uninstalling pypdf-4.2.0:
      Successfully uninstalled pypdf-4.2.0
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
llama-index-readers-file 0.1.20 requires pypdf<5.0.0,>=4.0.1, but you have pypdf 3.17.4 which is incompatible.
Successfully installed cffi-1.16.0 cryptography-42.0.7 opencv-python-4.9.0.80 parsee-pdf-reader-0.1.5.8 pdf2image-1.17.0 pdfminer-six-20221105 pycparser-2.22 pypdf-3.17.4 pytesseract-0.3.10


# Metadata
- could use isfdb database dumps
- or rpggeek similarly

# Logging
- needs logging added to track things in main program

# Speed
- Game collection with lots of images - some things being old scans will be slow
- Consider parallelising
    - All at once embarassingly parallel job
    - Perhaps Lithops to abstract some configuration [supposedly]?
        - https://github.com/lithops-cloud/lithops

# Lithops
## Configure
- Config File
- Compute Backend [policy, role] https://github.com/lithops-cloud/lithops/blob/master/docs/source/compute_config/aws_lambda.md
- Storage Backend [bucket] - https://github.com/lithops-cloud/lithops/blob/master/docs/source/storage_config/aws_s3.md

## Cloud test
```bash
/book-mentat/src/games$ lithops hello
2024-05-25 12:37:06,919 [INFO] config.py:139 -- Lithops v3.3.0 - Python3.10
2024-05-25 12:37:07,708 [INFO] aws_s3.py:59 -- S3 client created - Region: us-west-2
2024-05-25 12:37:09,791 [INFO] aws_lambda.py:97 -- AWS Lambda client created - Region: us-west-2
2024-05-25 12:37:09,793 [INFO] invokers.py:107 -- ExecutorID 8xc5f5-0 | JobID A000 - Selected Runtime: default-runtime-v310 - 256MB
2024-05-25 12:37:10,010 [INFO] invokers.py:115 -- Runtime default-runtime-v310 with 256MB is not yet deployed
2024-05-25 12:37:10,010 [INFO] aws_lambda.py:388 -- Deploying runtime: default-runtime-v310 - Memory: 256 - Timeout: 180
2024-05-25 12:37:10,838 [INFO] aws_lambda.py:187 -- Creating lambda layer for runtime default-runtime-v310
2024-05-25 12:38:53,088 [INFO] invokers.py:174 -- ExecutorID 8xc5f5-0 | JobID A000 - Starting function invocation: hello() - Total: 1 activations
2024-05-25 12:38:53,166 [INFO] invokers.py:213 -- ExecutorID 8xc5f5-0 | JobID A000 - View execution logs at /tmp/lithops-richard/logs/8dc5f5-0-A000.log
2024-05-25 12:38:53,191 [INFO] executors.py:491 -- ExecutorID 8xc5f5-0 - Getting results from 1 function activations
2024-05-25 12:38:53,191 [INFO] wait.py:101 -- ExecutorID 8xc5f5-0 - Waiting for 1 function activations to complete
```

## Runtimes
- Need to build a Docker image for anything bespoke of interest
- Follow examples
    - https://github.com/lithops-cloud/lithops/tree/master/runtime/aws_lambda

- Needs Docker Desktop https://docs.docker.com/desktop/install/ubuntu/
```bash
At the end of the installation process, apt displays an error due to installing a downloaded package. You can ignore this error message.

N: Download is performed unsandboxed as root, as file '/home/user/Downloads/doc
```

### Build
- lithops runtime build -f MyDockerfile -b aws_lambda my-container-runtime-name
- runtime memory –memory, -m Memory size in MBs to assign to the runtime.
- permissions issues:
    - https://stackoverflow.com/questions/51342810/how-to-fix-dial-unix-var-run-docker-sock-connect-permission-denied-when-gro
- list runtimes lithops runtime list -b aws_lambda

- libgl error
    - libgl1 library
    - suggestions https://stackoverflow.com/questions/55313610/importerror-libgl-so-1-cannot-open-shared-object-file-no-such-file-or-directo
- so good questions?
- other solutions
- pip install opencv-contrib-python
- install opencv-contrib-python rather than opencv-python.
- https://stackoverflow.com/questions/55313610/importerror-libgl-so-1-cannot-open-shared-object-file-no-such-file-or-directo
- At one point, I used opencv-python-headless which worked for my case with FastAPI when I deployed on Heroku once. What's the 
- pip install -U opencv-python
- apt update && apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libg

# possibly
-  Set the LD_LIBRARY_PATH environment variable
 ENV LD_LIBRARY_PATH="/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH"

### Docker
- docker system prune --all --force  
