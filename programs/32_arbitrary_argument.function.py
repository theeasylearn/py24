import asyncio
from googletrans import Translator
#concept of arbitrary arguments 
async def translateToHindi(*words):
    line = ' '.join(words)
    print(line)
    translator = Translator()
    translation = await translator.translate(line, src='en', dest='hi')
    print("Original (English):", line)
    print("Translated (Hindi):", translation.text)
    
asyncio.run(translateToHindi('Books','pen','table','room'))
asyncio.run(translateToHindi('animal','bird','pound'))
asyncio.run(translateToHindi('tomato','dish'))
asyncio.run(translateToHindi('bread'))