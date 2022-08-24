import googletrans
from googletrans import Translator
import pandas as pd
import numpy as np
import os


if __name__ == "__main__":
    fileList = []
    files = os.listdir()
    # init
    for file in files:
        if file[file.rindex('.')+1:] == "xlsx" :
            fileList.append(file)
    
    for file in fileList:           
        data = pd.read_excel(
         file,
         engine='openpyxl'
        )
        df = pd.DataFrame(data, columns=['English']).fillna(0)
        hindi = []
        telagu = []
        for i  in range (len(df['English'])):
            if df['English'][i] is not None and df['English'][i] != 0:
                print(df['English'][i])
                
                translator = Translator()

                from_lang = 'en'

                to_lang = 'hi'
                
                get_sentence = df['English'][i]
                text_to_translate = translator.translate(get_sentence,src= from_lang,dest= to_lang)
                
                hindi.append(text_to_translate.text)
                to_lang = 'te'
                text_to_translate = translator.translate(get_sentence,src= from_lang,dest= to_lang)
                telagu.append(text_to_translate.text)
            else:
                hindi.append(" ")
                telagu.append(" ")
        df2 = pd.DataFrame(data)
        df2["Hindi"] = hindi
        df2["Telagu"] = telagu
        print(df2)
        fileName = file[0 : file.rindex('.')]
        df2.to_excel(f"{fileName} translated.xlsx", index=False)
