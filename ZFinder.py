import os

def search_files(directory, keyword):
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            if os.path.isfile(filepath):
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    for line_num, line in enumerate(f, 1):
                        if keyword in line:
                            print(f"Found '{keyword}' in '{file}' at line {line_num}:")
                            print(line.rstrip())

# Example usage
directory = os.path.dirname(os.path.abspath(__file__))  # Directory where the script is located
keyword = 'Tashri'  # Replace with the word or phrase you want to search for

search_files(directory, keyword)
