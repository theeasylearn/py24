import asyncio
from googletrans import Translator
#user defined function
async def EnglishToHindi():
    translator = Translator()
    english_text = "book"
    translation = await translator.translate(english_text, src='en', dest='hi')
    
    print("Original (English):", english_text)
    print("Translated (Hindi):", translation.text)

# Run the async main function
asyncio.run(EnglishToHindi())
