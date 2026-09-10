import os
from collections import Counter

print("========================================")
print("        FILE EXTENSION REPORTER")
print("========================================")

folder_path = input("Enter folder path: ").strip()

if not os.path.isdir(folder_path):
    print("\n Invalid folder path.")
else:
    extension_counter = Counter()
    no_extension = 0
    total_files = 0

    for root, folders, files in os.walk(folder_path):
        for file in files:
            total_files += 1

            extension = os.path.splitext(file)[1].lower()

            if extension:
                extension_counter[extension] += 1
            else:
                no_extension += 1

    print("\n========================================")
    print("          EXTENSION REPORT")
    print("========================================")

    if total_files == 0:
        print("No files found in this folder.")

    else:
        for extension, count in extension_counter.most_common():
            print(f"{extension:<10} : {count} files")

        if no_extension > 0:
            print(f"{'No Extension':<10} : {no_extension} files")

        print("----------------------------------------")
        print(f"Total Files : {total_files}")

    print("========================================")