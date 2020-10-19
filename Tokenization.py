# nltk  import
#  os for read mutiple file
import nltk
from nltk.tokenize import sent_tokenize , regexp_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk import ISRIStemmer
from nltk.tag import pos_tag
from nltk.chunk import RegexpChunkParser, RegexpParser

from pathlib import Path

import os

# this class for tokenizaor
class Text_Tokenization:

    #this function to return All files Name from dirctory
    def fetchFiles(self):
        path = '_articles-sports\_articlesSports'
        AllFiles = os.listdir(path)
        return  AllFiles

    #   this function setences tokeniaze
    #   call fetch files name for get all name for files
    #   for loop for read the content of file
    #   call stop words function and write result in new file
    def SentTokenize(self):
        AFiles = self.fetchFiles()
        array = []
        for sentences in AFiles:
            path = "_articles-sports/_articlesSports/" + sentences
            readText = open(path,'r')
            arr = readText.read()
            word = word_tokenize(arr)
            #.......... call function stop words ......
            new_text = self.Stop_words(word)

            #...........call function steamer words....
            steamer_text = self.Word_Steamer(new_text)

            #........... call function that tagging the words
            chungedWords = self.ProcessWoeds(steamer_text)

            #...... call function and check the path if exists or not to save the file
            self.SaveFile(chungedWords,sentences)








    # this function to remove stop words from the text
    # first call the functiion stop words and chose the languages
    # ther is three If statment for check and fliter the string is not number or sample or stop word
    # this function return array
    def Stop_words(self, arr):
        stop_word = set(stopwords.words("arabic"))
        sample_array = ['?','.','"','!',',',':','؟']
        new_value = []
        for i in arr:

            if i not in stop_word:
                if i not in sample_array:
                    if not i.isnumeric():
                        new_value.append(i)
        return new_value

    #.. this function steaner the arabic word
    #.. define the object from ISRIStemmer
    #.. save result in array and return it

    def Word_Steamer(self, arr):
        array = []
        stemmer = ISRIStemmer()
        for words in arr:
            array.append(stemmer.stem(words))
        return array

    #...this function for procwess the word after steamer
    #... give the words tager and show the tree for the world
    def ProcessWoeds(self,arr):
        tagged = pos_tag(arr)
        chunkGram = r"""Chunk:{<RB.?>*<VB.?>*<NNP>}"""
        chunkParser = RegexpParser(chunkGram)
        chunked = chunkParser.parse(tagged)
        return chunked
        print(chunked)


    #.... this function for save the file in the new dir.
    def SaveFile(self,arr,sent):
        #...check if  dir exists or not before the save file
        try:
            print("file not exists")
            file_bulder = open('Result/' + sent, 'w')
            stringValue = str(arr)
            file_bulder.write(stringValue)
        except:
            my_file = Path('Result/' + sent)
            if my_file.exists():
                print('this path exists !')











if __name__ == '__main__':

   obj = Text_Tokenization()
   obj.SentTokenize()
