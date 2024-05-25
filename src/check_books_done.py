import pickle
import os
with open('book_dict.pkl','rb') as f:
    book_dict = pickle.load(f)

input_path = "/mnt/usb_mount/output/Calibre Books"
file_list = []
for root, dirs, files in os.walk(input_path):
    for file in files:
        file_list.append(file)

need_list = []
for b in file_list:
    if b in book_dict:
        pass
    else:
        print("STILL NEED:",b)
        need_list.append(b)

print("BOOK DICT SIZE:",len(book_dict), "FILE LIST SIZE:",len(file_list), "NEED LIST SIZE:",len(need_list))        
