# initializing string
test_str = 'Geeksforgeeks is best for geeks and CS'
  
# printing original string
print("The original string is : " + str(test_str))
  
# initializing word list 
word_list = ["best", 'CS', 'for']
  
# initializing replace word 
repl_wrd = 'gfg'
  
# Replace multiple words with K
# Using regex + join()
res = re.sub("|".join(sorted(word_list, key = len, reverse = True)), repl_wrd, test_str)
