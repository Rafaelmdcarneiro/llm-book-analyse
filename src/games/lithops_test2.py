
import os
from lithops import FunctionExecutor
from lithops.storage.cloud_proxy import os as cloudos, open as cloudopen
from lithops import Storage

from pdf_reader import get_elements_from_pdf
import pickle
from multiprocessing import Pool

def process_pdf(file):
    #import cv2
    cwd = os.getcwd()
    print("CURRENTLY:",cwd)
    from pdf_reader import get_elements_from_pdf
    #output_path = "/mnt/usb_mount/games/parsee"
    output_path = "games/parseenumber"
    
    filelist = file.split('(')
    #print("FILELIST:",filelist)
    filenumber = filelist[-1]
    result = filenumber.index(')')
    filenumber = filenumber[0:result]
    #print("FILENUMBER:",filenumber)

    print("FILE PROCESSING:",file, filenumber)

    newfile = file + '_' + filenumber + '.pkl'

    if cloudos.path.exists( cloudos.path.join(output_path,cloudos.path.basename(newfile)) ):
        print("SKIPPING:",file, filenumber)
        return 

    with cloudopen(file,'rb') as f:
        pdffile = f.read()

    # Define the file path
    file_path = file

    # Extract the directory path from the file path
    dir_path = os.path.dirname(file_path)
    #dir_path = dir_path

    # Create the directories if they don't exist
    os.makedirs(dir_path, exist_ok=True)

    # Write to the file
    with open(file_path, 'wb') as localfile:
        localfile.write(pdffile)

    print(f'File has been written to {file_path}')        
    try:
        elements = get_elements_from_pdf(file)
        #print(elements)
        print("NEWFILE OUTPUT:",output_path,os.path.basename(newfile))
        with open(cloudos.path.join(output_path,clouodos.path.basename(newfile)), 'wb') as f:
            pickle.dump(elements, f)
    except Exception as parseE:
        print(parseE)
        newfile = file + '_' + filenumber + '.error'
        print("ERROR:", file)
        with open(cloudos.path.join(output_path,cloudos.path.basename(newfile)), 'wb') as f:
            pickle.dump(str(parseE), f)

if __name__ == "__main__":
    input_path = "books/Calibre Library"
    output_path = "games/parseenumber"
    filetest = 'Anodyne Printware/Mothership - HULL BREACH VOL. 1 (25633)/Mothership - HULL BREACH VOL. 1 - Anodyne Printware.pdf'
    filetest = 'books/Calibre Library/Sean McCoy/Mothership - WOM-v1.1 (26106)/Mothership - WOM-v1.1 - Sean McCoy.pdf'
    #os.makedirs(output_path, exist_ok=True)
    #counterror = 0

    


    with FunctionExecutor(runtime='book-mentat-runtime') as fexec:

        #lith = lithops.FunctionExecutor(runtime='lithops-ndvi-v312:01')
        #lith.call_async(test, data=())
        #res = lith.get_result()
        #print(res)  # Prints 'hello'        
        f = fexec.call_async(process_pdf, filetest)
        print(f.result())