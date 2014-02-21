''' html2markdown is a utility which converts an HTML file to markdown format

Usage:

python3 html2markdown.py <yourfile.html>

This utility strips the head, and all block tags except <h1> ...<h6> <p> <img><strong>
<em> list tags, and table tags.  Then converts these into the Markdown format.

'''
import os
import io
import sys
import re

filename = sys.argv[1]

class mdFile():
    '''This class creates the resulting markdown file'''
    text = ""
    file = None
    def __init__(self, filename):
        fileOutName = filename.rstrip('html')+"md"
        self.text = hfile.intText()

    def convertHeadings(self):
        pass

    def close(self):
        self.file = open (fileOutName, mode= 'wt')
        self.file.write(self.text)
        self.file.close()
    

class htmlFile():
    '''This class object handles the HTML file input'''
    intText = ""
    inFile = None
    def __init__(self, filename):
        self.fileInName = open (filename)
        self.intText = self.fileInName.read()

    def stripTags(self):
        intText.replace('\n','')
        '''remove line endings'''
        head = re.compile('<head>*</head>')
        print ('removing header')
        intText = head.sub(' ')
        

    
filename = sys.argv[1]
hFile = htmlFile(filename)
mFile = mdFile(filename)

