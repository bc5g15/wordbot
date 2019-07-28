import requests
import random

URL = "https://api.noopschallenge.com/wordbot"
PARAMS = {"count": 1000, "set":"moods"}

r = requests.get(url = URL, params = PARAMS)

data = r.json()

END = "END"
START = "START"

#print(data)
wrds = data["words"]

def get_sets():
    turl = "https://api.noopschallenge.com/wordbot/sets"
    r = requests.get(url=turl)
    data = r.json()
    return data

def build_chain(words):
    # Build a markov chain using the word list provided
    chain = {}
    for word in words:
        c = word[0]
        if START not in chain: chain[START] = {}
        chain[START][c] = chain[START].get(c, 0) + 1
        for i in range(len(word)-1):
            c = word[i]
            if c not in chain:
                chain[c] = {}
            ca = word[i+1]
            chain[c][ca] = chain[c].get(ca, 0) + 1
        c = word[len(word)-1]
        if c not in chain: chain[c] = {}
        chain[c][END] = chain[c].get(END, 0) + 1
    return chain

def choose_letter(chain, start):
    probs = chain[start]
    total = sum([probs[x] for x in probs])
    i = random.randint(1, total)
    for w in probs:
        i -= probs[w]
        if i <= 0:
            return w

def make_word(chain):
    l = START
    output = []
    while l != END:
        l = choose_letter(chain, l)
        output.append(l)
    output.pop()
    return "".join(output)

def word_length(chain, min_length):
    w = ""
    while len(w) < min_length:
        w = make_word(chain)
    return w

#c = build_chain(["test", "trial", "length"])
c = build_chain(wrds)
i = 0
while i < 100:
    w = word_length(c, 4)
    if w not in wrds:
        i+= 1
        print(w)
