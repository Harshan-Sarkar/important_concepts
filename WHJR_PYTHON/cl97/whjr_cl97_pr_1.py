# intro = input("Enter your name: ")
# # print(len(intro))
# for words in intro:
#     print(words.count())

introString=input("Enter string:")
letterCount=0
wordCount=1
for i in introString:
      print(i)
      letterCount=letterCount+1
      if(i==' '):
            wordCount=wordCount+1
    
print("Number of word in the string:", wordCount)
print("Number of character in the string:", letterCount)