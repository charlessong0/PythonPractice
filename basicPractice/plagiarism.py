from difflib import SequenceMatcher
with open('ex25.py') as file_1,open('ex25.1.py') as file_2:
    file1_data = file_1.read()
    file2_data = file_2.read()
    similarity_ratio = SequenceMatcher(None,file1_data,file2_data).ratio()
    print similarity_ratio  #plagiarism detected))))'')'')
