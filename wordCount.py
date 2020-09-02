#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:42:00 2020

@author: joaquin
"""
import sys        # command line arguments 

# set input and output files
if len(sys.argv) is not 3:  #(set to 3 b/c including the cmmnd line args + 2 .txt files)
    print("Correct usage: wordcount.py <input text file> <output file> ")
    exit()

def Split(txtWord):
    for char in ".,/\':;-+\n\"":
        txtWord = txtWord.replace(char, ' ')
    word = txtWord.lower() 
    word = word.split()  
    return word
        
def InsertToDict(wList):
    d1 = {}
    for word in wList:
        if word in d1:
            d1[word] = d1[word] + 1
        else:
            d1[word] = 1
    return d1
    

def main():
    textFname = sys.argv[1]   # read from (paragrapghs)
    outputFname = sys.argv[2]  #write to (format of solution key)

    with open(textFname, 'r') as txtWordsF:
        txtFile1 = txtWordsF.read() 
    wordList = Split(txtFile1)
    dictWord = InsertToDict(wordList)
    outputFile = open(outputFname, 'w') #must close file
    for k,v in sorted(dictWord.items() ):
        outputFile.write(k + ' ' + str(v) + '\n')
    outputFile.close()


if __name__ == '__main__':
    main()
    
    