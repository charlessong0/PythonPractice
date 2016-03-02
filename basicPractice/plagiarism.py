from difflib import SequenceMatcher
from sys import argv
script, file1, file2 = argv
with open(file1) as file_1,open(file2) as file_2:
    file1_data = file_1.read()
    file2_data = file_2.read()
    similarity_ratio = SequenceMatcher(None,file1_data,file2_data).ratio()
    print similarity_ratio  #plagiarism detected))))'')'')
