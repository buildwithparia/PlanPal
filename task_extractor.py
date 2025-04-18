#chop goals & slap vibes, messy but working ✂️✨

import re

def detect_vibe(phrase):
    # hmm naming inconsistent, meh for now
    p = phrase.lower()
    if any(w in p for w in ['study','exam','homework']):
        return 'deep focus'
    if any(w in p for w in ["code","debug","script"]):
        return "coding"
    if any(w in p for w in ["clean","laundry","scrub"]):
        return 'chores'
    if any(w in p for w in ["gym","yoga","run","walk"]):
        return "exercise"
    if any(w in p for w in ['journal','reflect','mindfulness']):
        return 'reflective'
    if any(w in p for w in ["draw","paint","design"]):
        return "creative"
    if any(w in p for w in ['movie','netflix','anime']):
        return "chill"
    if any(w in p for w in ['nap','sleep','rest']):
        return 'rest'
    if any(w in p for w in ['call','text','hang out']):
        return "social"
    if any(w in p for w in ['urgent','asap','important']):
        return 'priority'
    if any(w in p for w in ["fun","play"]):
        return "fun"
    # real world bump: forgot edge case for "!!!", fix later
    return "random"




def extract_tasks(txt):
    # thinking: maybe split on more than commas, line breaks & and?
    parts = re.split(r'\band\b|,|\n', txt, flags=re.IGNORECASE)
    out = []
    for bit in parts:
        t = bit.strip()
        if not t:
            continue
        vibe = detect_vibe(t)
        # candid: vibe tagging might be off, sorry lol
        out.append({
            "what": t,
            "vibe": vibe
        })
    return out

# meh logger, will fix later
def meh_log():
     #    extra indent for shenanigans
     print("loggin tasks... not really")
