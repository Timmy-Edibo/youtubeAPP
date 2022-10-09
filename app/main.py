from fastapi import FastAPI, Form, HTTPException, status, Body
from fastapi.middleware.cors import CORSMiddleware
from isodate import parse_duration

import requests
import os
import json

app = FastAPI(prefix="/do_it_yourself", tags=["Do It Yourself"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["set-cookie"],
)


from dotenv import load_dotenv
load_dotenv()
youtube_api_key = os.getenv("YOUTUBE_API_KEY")

@app.post("/youtube")
async def youtube(form: str = Body(...)):

    curse_words =["shit", "bullshit", "bitch", "fuck","sex", "porn", "whore", "ho", "slot", "dick", "pussy", "asshole", "steal", "fucker",
    "zulu", "Yvonne", "xml", "xnxx", "x-rated", "x-japan", "x-bomb", "wuhan", "watch free", "watch online", "virgin", "virginity", "violence", "violently",
    "victim", "victimz", "vibrator", "vibrators", "vape", "vajayjay", "Vaginal thrush", "vagina", "vaginal", "vaffanculo", "vacuum", "Uyghur Muslims", "Uyghur Muslim", "urge",
    "upskirts", "upskirt", "undressing", "undress", "underwear", "Ukraine", "twerk", "twerking", "twat", "twats", "turk", "tumor", "tubes", "troops", "tri-sexual", "treatment",
    "trans gender", "torture", "torrent", "topless", "titty", "titties", "titten", "tittie", "titties", "titfuck", "tit", "tide", "tug", "throating", "throat", "threat", "thong",
    "thc", "testicle", "testicles", "terrorism", "terrorist", "terrorists", "teen", "teens", "Ted Bundy", "technician", "tattoo", "tattoos", "stripper", "strippers", "striped",
    "taking the piss", "dating", "t bag", "syria", "swearing", "suicide", "sucking", "sucks", "sucked", "Succubus", "suitable", "stuff", "strips", "stripping", "kissing", "strip", 
    "strip club", "strap on", "strapon", "stockings", "stoned", "stoner", "stfu", "squirting", "squirt", "spycam", "spy cam", "spy", "spokesman", "sponsors", 
    "sperm", "spanking", "spank", "sonofabitch", "sodomize", "snuff", "snatch", "smut", "smutty", "smoke", "smoking", "sluts", "slut", "sleazy", "slaves", "slayer", "slayers", "slave",
    "slavery", "slaughtering", "skullfuck", "skins", "skin", "skin to skin", "shrooms", "shut","shota", "shoplifter", "shot", "shrek", "sites", "shibari", "shemales", "shemale", 
    "shocking", "shitty", "shitter", "shitted", "shitposting", "shitpost","shithouse", "shithole", "shithead", "shitfuck", "shitfaced", "shitface", "shite", "shitbag", "sheet", "Shane Dawson",
    "shame", "sh!t", "f*ck", "sexy time", "sexy", "Sexually transmitted infections", "sexually", "sexuality", "Sexual Health", "sexual", "sextortion", "sexting", "sexted", "sext", "sexo",
    "sexist", "sexism", "sexcam", "sex worker", "sex work", "sex", "service", "servant","serum", "series", "sensor", "sends", "sending", "semen", "seduce", "seduced", "seduces", "secretly",
    "secrets", "secretary", "scrotum", "scrog", "screw", "screwed", "screenshot", "scissoring", "scientist", "schlong", "scandal", "scanner", "scam", "satisfying", "satisfy", "urge",
    "satan", "salvia", "sake",  "sadly", "sadist", "sadism", "saddam", "sabrina", "sack",  "s3x", "s.h.i.t.", "s-h-i-t", "rwanda", "rule 34", "russian", "rule 34", "rude", "rufies", "romance", 
    "romantic", "roms", "rom", "roblox", "robbery", "roasting", "rob", "robber", "robbed",  "riverside", "rivers", "rip", "riot", "riots", "rioting", "rioters", "rimming", "rimjob", "rigs",
    "rico", "rick", "richardson", "rica", "revolutionary",   "reverse cowgirl", "restriction", "restricted", "restaurants", "restaurant", "requests", "rehab", "rehabilitation", "referral", 
    "remarks", "redneck", "redhead", "reddit", "rectal", "rapist", "raping", "raped", "rape","racist", "racism", "race war", "race", "r kelly", "qwert", "qweef", "queef", "que", "quad-sexual",
    "quackityhq", "qtf", "pussys", "pussylicking", "pussy", "pussies", "pussie", "pussi", "pusse", "puss", "punishment", "puke", "pukes", "pubic", "pubic hair", "pubes", "prude", "prostitute",
    "prostitution", "prostitues", "pro-choice", "prig", "prescription", "prescription drug", "prescription medication", "premium", "pot head", "potty", "powder", 
    "pornos", "pornography", "porno", "pornhub", "porn", "porchmonkey", "porch monkey", "poops", "poopuncher", "poopchute", "poop", "poonany", "poonani", 
    "poo", "poof", "pittsburgh", "pissing", "pissin", "pissflaps", "pissers", "pisser", "pissed off", "pissed", "piss pig", "piss off", "piss", "pingas", "ping", "pills", "phuck", "phucking", "photos",
    "phonesex", "phi", "phallus", "pervert", "perverted", "perverts", "penis", "penial", "penile", "pencils", "peggiing", "peeing", "pee pee", "pedobear", "pedophile", "pedophilia", "pedophiliac",
    "pedo", "pecker", "pee" , "panta", "pantyhouse", "pants", "panties", "pansexual", "pantie", "pansy", "paedophile", "paedo", "p0rn", "p.u.s.s.y." , "oven", "ovary", "orgasim", "orgasims", "organsm"
    "organsmic", "organsms", "orgies", "orgy", "oriental", "oral", "offesnive", "offense", "offend", "obituaries", "nutten", "nutsacks", "nudes", "nude", "nudity", "nudist", "nipple", "nip", "nipples",
    "niggers", "niggerfaggot", "nigger", "niggaz", "niggas", "niggah", "nigg3r", "nevaeh", "netfix", "net", "naughty", "nasty", "naked", "naggers", "murder", "murdered", "murderer", "movies", "film",
    "motherfucking", "motherfuckin", "motherfuckers",  "molest", "molester", "misconduct", "mature", "adult", "adults", "mating", "mattress", "masturbators", "masturbation", "masturbate", "masterbation",
    "masterbating", "masterbate", "masterbat", "master-bate", "massacre", "massage", "master", "marijuana", "lust", "lustful", "LSD", "LGBTQ", "LGBTQIA", "LHR", "LQTM", "lick", "licking", "libs", "lesbos",
    "lesbo", "lesbians", "lesbian", "lesbianism", "labia", "vegas", "kurwa", "kush", "Ku Klux Klan", "kum", "kidnap", "jihad", "jews", "jerkoff", "jerk-off", "jerk0ff", "jerkass", "jacking off", "jackie",
    "islam", "isis", "isil", "religion", "allah", "intercourse", "intimacy", "immoral", "immature", "illegal", "alien", "selina", "idiots", "hymen", "hottest", "hotsex", "hotmail", "hot", "horney", "horny",
    "horrible", "hooker", "homo", "hiv", "hitler", "harass", "hand", "job", "blow", "girl", "top", "kiss", "grab", "genital", "genocide", "gay" 
      ]
    
    for curse_word in curse_words:
        if curse_word in form:
            raise HTTPException(status_code=404, detail="content not allowed on this platform")
    search_url = "https://www.googleapis.com/youtube/v3/search"
    video_url = "https://www.googleapis.com/youtube/v3/videos"

    search_params = {"key": youtube_api_key, "q": form, "part": "snippet", "type": "video", "maxResults": 9}
    search_results = requests.get(search_url, params=search_params)
    
    # results = search_results.json()["items"]
    results = search_results.json()
    print(result_item["items"])
    result_item=results["items"]

    with open("test.json", "a", encoding="utf8") as file:
        json.dump(results, file, indent=4)


    # video_ids = [result["id"]["videoId"] for result in results]

    # video_params = {"key": youtube_api_key, "id": ",".join(video_ids), "part": "snippet, contentDetails", "maxResults": 9}
    # video_results = requests.get(video_url, params=video_params)

    # r = video_results.json()["items"]

    # videos =[]
    # for result in r:
    #     video_data = {
    #         "id": result["id"],
    #         "url": f"https://www.youtube.com/watch?v={result['id']}",
    #         "thumbnail": result["snippet"]["thumbnails"]["high"]["url"],
    #         "duration": parse_duration(result['contentDetails']['duration']).total_seconds() // 60 ,
    #         "title": result["snippet"]["title"]
    #     }
    #     videos.append(video_data)
    

    # return {"data": videos }


from pydantic import BaseModel
class Word(BaseModel):
    search: str



from .cruds import dictionary

@app.post("/dictionary")
def dictionaryy(word: Word):
    """ Post request \n
    Dictionary Endpoint
    """
    return dictionary(word=word.search)


