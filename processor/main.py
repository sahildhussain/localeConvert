from processor.fileProcess import *
from processor.translateProcess import translateLanguage, translateLanguages
from pathlib import Path
import sys

def Translate():
    print(sys.argv)
    data = GetKeydata()
    
    # print(data["translator"])
    translator=data["translator"]
    if(len(sys.argv)>1):
        filePath = sys.argv[1]
        original_language = sys.argv[2]
        languages = sys.argv[3]
        convert_to = languages.replace(' ','').split(',')

    else:
        filePath = input('Enter file Path(Enter for default.xml): ')
        original_language = input('Select the original Language(Enter for AutoDetect):')

        print('Select the languages you want to convert this document to:')
        convert_to = [x for x in input().split(' ')]

    if filePath == '' or filePath == 'na':
        filePath = Path.cwd()/Path('default.xml')

    directoryPath = str(filePath).split('/')
    directoryPath.pop()
    directoryPath = ('/').join(directoryPath)

    if translator=='microsoft':
        response = translateLanguages(original_language,convert_to,filePath)
        saveFiles(convert_to, response, filePath,directoryPath)
    else:
        for lang in convert_to:
            response = translateLanguage(original_language,lang,filePath)
            # print(response)
            saveFile(lang,response,filePath,directoryPath)
        