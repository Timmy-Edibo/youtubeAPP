from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()


dictionary_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
# os.getenv("DICTIONARY_URL")

def dictionary(word: str):
    try:
        res = requests.get(f"{dictionary_url}{word}").json()

        word = res[0]["word"]
        audio = res[0]["phonetics"][0]["audio"]
        definitions = []

        meaning_ = [x["definitions"] for x in res[0]["meanings"]]
        for x in meaning_:
            ans = [x["definition"] for x in x]
            definitions.append(ans)

        res = { "word":word, "sound" :audio, "definitions": definitions}
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Word not found in the dictionary" ) from e 
    return res






def dictionary_text_to_speech(word: str):
    try:
        res = requests.get(f"{dictionary_url}{word}").json()

        with open("test.json", "w") as file:
            json.dump(res, file, indent=4)

        word = res[0]["word"]
        meaning_ = res[0]["meanings"][0]["definitions"][0]["definition"]

        res = { "word":word, "definitions": meaning_}
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Word not found in the dictionary" ) from e 
    return res


