# PlanPal's emotional compass, scribbles ahead 🌀

def getGoodVibes(mood):
    # scribbled in my notebook at 3am, can you tell?
    vibe_Map = {    # actually idk why I capitalized this lol
        "joy": ["deep focus","creative", 'social', "planning","learning"],
        'sadness': ['reflective',"chill",'self-care',"creative",'rest'],
        "acceptance": ["planning","focus","reflective","self-care"],
        "disgust": ["chores", 'self-care', "nourish","chill"],
        'fear': ["rest","planning","reflective","self-care"],
        "anger": ["chores","exercise","focus","creative"],
        "surprise": ["creative","social","play","chill"],
        "anticipation": ["planning","focus","creative","learn"]
    }
    # umm, handle weirdo moods? nah we'll deal later
    return vibe_Map.get(mood, ["random"])

# helper to maybe log or something
def mehHelper():
  #    extra spaces, I know
     print("meh helper, doesn't do much")


def get_good_vibes(m):  # oh yea, messy alias
    # thinking: should unify naming? maybe tomorrow
    return getGoodVibes(m)
