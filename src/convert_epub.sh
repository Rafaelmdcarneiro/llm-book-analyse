#!/bin/bash

# Input directory containing the eBooks to be processed
INPUT_DIR="/mnt/usb_mount/books/Calibre Books"

# Output directory where converted EPUBs will be saved
OUTPUT_DIR="/mnt/usb_mount/output/Calibre Books"

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR"

# Recursively traverse all directories in the input directory
find "$INPUT_DIR" -type f -exec bash -c '
    # Function to convert or copy EPUB files
    process_file() {
        FILE="$1"
        OUTPUT_DIR="/mnt/usb_mount/output/Calibre Books"

        # Extract the filename without extension
        FILENAME=$(basename "$FILE" | cut -d. -f1)
        EXTENSION="${FILE##*.}"

        # Check if the file has an undesirable extension
        if [[ "$EXTENSION" == "json" || "$EXTENSION" == "db" || "$EXTENSION" == "jpg" || "$EXTENSION" == "opf" || "$EXTENSION" == "rar"  ]]; then
            # If the file has an undesirable extension, skip it
            echo "Skipping $FILE - undesirable extension"
            return
        fi

        # Check if the file is already an EPUB
        if [[ "$EXTENSION" == "epub" ]]; then
            # If the file is already an EPUB, copy it to the output directory
            echo "COPYING epub FILE $FILE"
            cp "$FILE" "$OUTPUT_DIR"
            # Print status message
            echo "Copied $FILE to $OUTPUT_DIR"
        else
            # Convert the non-EPUB eBook to EPUB format and save it to the output directory
            echo "DESTINATION $OUTPUT_DIR/$FILENAME.epub"
            #ebook-convert "$FILE" dummy.epub
            ebook-convert "$FILE" "$OUTPUT_DIR/$FILENAME.epub"
            # Print status message
            echo "Converted $FILE to EPUB"
        fi
    }

    # Process each file found by find command
    process_file "$0"
' {} \;

