import os
import pandas as pd
input_path = "/mnt/usb_mount/books/Calibre Library"
output_path = "/mnt/usb_mount/games/parsee"

counterror = 0

count = 0
count_complete = 0
count_incomplete = 0
count_problem = 0
count_log = 0

with open(os.path.join(input_path,'logs.log'),'w') as fl:
        
    with open(os.path.join(input_path,'complete.log'),'w') as f:
        for root, dirs, files in os.walk(input_path):
            for file in files:
                if '.pdf' not in file or '.log' in file:
                    if '.log' in file:
                        fl.writelines("LOG: " + os.path.join(root,file) + "\n")    
                    continue
                count += 1
                if os.path.exists(os.path.join(output_path,file + '.pkl')):
                    print("COMPLETE:", os.path.join(root,file))
                    f.writelines("COMPLETE: " + os.path.join(root,file) + "\n")
                    count_complete += 1
                else:
                    print("NEED TO CHECK:", os.path.join(root,file))
                    f.writelines("NEED TO CHECK: " + os.path.join(root,file) + "\n")
                    count_incomplete += 1

                if os.path.exists(os.path.join(output_path,file + '.error')):
                    print("ERROR:", os.path.join(root,file))
                    f.writelines("COMPLETE: " + os.path.join(root,file) + "\n")
                    count_problem += 1


print("TOTAL PDF:",count, "COMPLETE:", count_complete, "NOT:", count_incomplete, "ERROR:", count_problem)                


