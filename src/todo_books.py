import pickle
import shutil
import os
with open('book_dict.pkl','rb') as f:
    book_dict = pickle.load(f)

input_path = "/mnt/usb_mount/output/Calibre Books"
output_path = "/mnt/usb_mount/todo/Calibre Books"

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

os.makedirs(output_path, exist_ok=True)

for n in need_list:
    print("copying:",n)
    shutil.copy(os.path.join(input_path,n),os.path.join(output_path,n))
