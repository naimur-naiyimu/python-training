import zipfile

def count_word_occurrences(file_path, word):
    with zipfile.ZipFile(file_path, 'r') as docx:
        content = docx.read('word/document.xml').decode('utf-8')

    occurrences = content.count(word)
    return occurrences


word_to_search = input("Enter a word or puncution mark: ")
file_path = "C:/Users/sr/Desktop/B Onika/golpo.docx"  # Change this to the path of your Word document

occurrences = count_word_occurrences(file_path, word_to_search)
print(f"The word '{word_to_search}' appears {occurrences} times in the document.")
