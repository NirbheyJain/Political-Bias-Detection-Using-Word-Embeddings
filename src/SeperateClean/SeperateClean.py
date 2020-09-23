# -*- coding: utf-8 -*-
import re
import string

def lowerCase(str):
    return str.lower()

def removeNumbers(str):
    return re.sub(r'\d+', '', str)

def removePunctuation(input):
    punc = string.punctuation + "’" + "“" + "”"
    translator = string.maketrans(punc, ' '*len(punc))
    output = input.translate(translator)
    return output


def removeCommonWords(sentence):
    commonWords = ['the','in','an','is','that','are','to','of','and','but','at','be','or','so','no']
    splitSentence = str.split(sentence)
    newSentence = ""
    for word in splitSentence:
        if word not in commonWords:
            newSentence = newSentence + " " + word
    return newSentence

def removeOneLetterWords(sentence):
    splitSentence = str.split(sentence)
    newSentence = ""
    for word in splitSentence:
        if len(word) > 1:
            newSentence = newSentence + " " + word
    return newSentence

def main():
    inputfiles = ['articles1.csv', 'articles2.csv','articles3.csv']

    """
    for csv in inputfiles:
        inputfile = open(csv,'r')
        for line in inputfile:
            print(str.strip(line))
            break

    Basis of each type of CSV parse
    """

    publications = ['New York Times', 'CNN', 'Breitbart', 'New York Post', 'Guardian', 'NPR', 'Reuters', 'Vox', 'Washington Post', 'Atlantic', 'Fox News', 'Buzzfeed News', 'National Review']

    for csv in inputfiles:
            x = 0
            inputfile = open(csv,'r')
            currentPublication = ""

            for line in inputfile:

                print(line)
                splitLine = str.split(line,",,")

                if splitLine[0].strip()=='publication' or splitLine[0].strip()=='':
                    continue

                if splitLine[0].strip() != currentPublication and splitLine[0].strip()in publications:
                    currentPublication = splitLine[0].strip()
                    exec("outputfile = open('publications/"+splitLine[0]+".csv','w')")
                if splitLine[0].strip() not in publications:
                    cleanLine = removeOneLetterWords(removePunctuation(removeNumbers(removeCommonWords(lowerCase(line)))))
                else:
                    exec("outputfile.write(\",\")")
                    cleanLine = removeOneLetterWords(removePunctuation(removeNumbers(removeCommonWords(lowerCase(line)))))
                exec("outputfile.write(\""+cleanLine+"\")")
                print("done")


if __name__== "__main__" :
    main()
