import os

def count_filetypes(root_dir):
    file_count = {}
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext.lower() not in file_count:
                file_count[ext.lower()] = 1
            else:
                file_count[ext.lower()] += 1
    return file_count

root_dir = '/mnt/usb_mount/books/Calibre Books'
file_count = count_filetypes(root_dir)
for ext, count in sorted(file_count.items()):
    print(f"{ext}: {count}")