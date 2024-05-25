import os
from pdf_reader import get_elements_from_pdf
#
import pickle

input_path = "/mnt/usb_mount/books/Calibre Library"
output_path = "/mnt/usb_mount/games/parsee"

os.makedirs(output_path, exist_ok=True)
counterror = 0

logfile = 'main_log.log'

count = -1
with open(os.path.join(input_path,logfile),'w') as mainlogf:

    for root, dirs, files in os.walk(input_path):

            for file in files:
                if '.pdf' in file and '.log' not in file:
                    print(file)
                    newfile = file + '.pkl'

                    try:
                        count += 1
                        elements = get_elements_from_pdf(os.path.join(root,file))
                        with open(os.path.join(output_path,newfile),'wb') as f:
                            pickle.dump(elements, f)
                        mainlogf.writelines(str(count) + " : " + str(file) + " : COMPLETED" + "\n")
                    except Exception as parseE:
                        print(parseE)
                        newfile = file + '.error'
                        print("ERROR:",file)
                        counterror += 1
                        mainlogf.writelines(str(count) + " : " + str(file) + " : ERROR" + str(parseE) + "\n" )

                        with open(os.path.join(output_path,newfile),'wb') as f:
                            pickle.dump('error', f)

                            
                    #print(elements)
                    #break

        #break
print("FINISHED: and there were ",counterror, " failures")    
#If you are processing a PDF that needs OCR but no elements or just very few are being returned, you can force OCR like this (replace the paths):

#elements = get_elements_from_pdf("FILE_PATH", force_ocr=True)
#If you want to visualise the output from the extraction, you can run the following (replace the paths):

#from pdf_reader import visualise_pdf_output
#visualise_pdf_output("FILE_PATH", "OUTPUT_PATH")