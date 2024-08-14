class WordsFinder:
  def __init__(self, *file_names ):
    self.file_names = file_names
    
  def get_all_words(self): 
 # {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
    words_dict = {}
    for file_name in self.file_names:
      with open(file_name, 'r') as file:
        words = list(file.read().split())
        words_dict[file_name] = words
    return  words_dict 

  def find(self, word):
    words_dict = self.get_all_words()
    result = dict()
    for file_name, words in words_dict.items():
      for index, word_ in enumerate(words):
        if word_ == word:
          result[file_name] = index
        
    return result

  def count(self, word):
    words_dict = self.get_all_words()
    dict1 = {}
    for file_name, words in words_dict.items():
      count = 0
      for index, word_ in enumerate(words):
        if word_.lower() == word.lower():
          count += 1
      dict1[file_name] = count 
    return dict1

finder2 = WordsFinder("test_file.txt")
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

