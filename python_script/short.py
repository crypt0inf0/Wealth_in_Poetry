# Function to read and process the file
def process_file(file_path):
    word_lists = {}

    with open(file_path, 'r') as file:
        for line in file:
            word, value = line.strip().split("' ")
            value = int(value)
            
            if value not in word_lists:
                word_lists[value] = []
            
            word_lists[value].append(word)

    return word_lists

# Main program
file_path = 'filter.txt'

try:
    word_lists = process_file(file_path)

    for value, words in sorted(word_lists.items()):
        word_list_str = ', '.join(words)
        print(f"{value}st word list is: {word_list_str}")

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
