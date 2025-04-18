# brain of the planner, but kind of sleep-deprived 🧠

import json
from datetime import datetime

# reading mood journal, ugh messy file ops
try:
    raw = open('data/mood.json').read()
    entries = json.loads(raw)
except Exception as err:
    print("ugh mood load error:", err)
    entries = []

# what day is it? stun gun me if this breaks
today_name = datetime.today().strftime('%A')
# what if timezone is off? oh, forgot timezone support

# search for today's entry
found = None
for entry in entries:
    if entry.get('day') == today_name:
        found = entry  # aha
        break

if found:
    mood = found.get("mood", "no idea")
    energy = found.get('energy', 'meh')
    print(f"🌀 Mood for {today_name}: {mood} mood with {energy} energy")
else:
    print('🤷 no mood set for today... guessing 🙃')

# oh, maybe I'll add an alarm later, but meh
def alarm_me_sometime():
    # imaginary function to nag you
    pass

your_mood = found



  

def mehAlarm():  
   
     print("this will nag you ¯\\_(ツ)_/¯")
