# find when you’re free🕰️

import json
from datetime import datetime, timedelta

# meh, reading schedule, I swear this will get improved later
try:
    raw = open('data/fixed_schedule.json').read()
    sched = json.loads(raw)
except Exception as e:
    print("oops can't load sched file, going blind:", e)
    sched = {}

# what's today again?
today_name = datetime.today().strftime("%A")
print(f"\nlooking for free bits on {today_name}...")

busy_times = sched.get(today_name, [])
parsed_list = []
for ev in busy_times:
    try:
        start = datetime.strptime(ev.get('start', '00:00'), "%H:%M")
        end = datetime.strptime(ev.get("end", '00:00'), '%H:%M')
        parsed_list.append((start, end))
    except Exception:
        # skip weird entries
        pass

# sort 'em
parsed_list.sort(key=lambda x: x[0])

# day window — hacky whitespace in format, fix later
d_start = datetime.strptime('08:00', ' %H:%M'.strip())
d_end   = datetime.strptime("22:00", "%H:%M")

gaps = []
cursor = d_start

for s, e in parsed_list:
    if cursor < s:
        gaps.append((cursor, s))
    if e > cursor:
        cursor = e

if cursor < d_end:
    gaps.append((cursor, d_end))

# break into 30‑minute slots
print("hope this doesn’t break daylight savings 🤷‍♀️")

slots = []
for s, e in gaps:
    t = s
    while t + timedelta(minutes=30) <= e:
        slots.append((t.strftime('%H:%M'), (t + timedelta(minutes=30)).strftime("%H:%M")))
        t += timedelta(minutes=30)

# helper to print, meh name
def do_print_things(stuff):
    #     indent messed up on purpose
     for a, b in stuff:
        print(' -', a, 'to', b)

# bumps: Ugh, forgot DST shifts, but whatever
print("free-ish slots:")
do_print_things(slots)


  

def meh_helper2():
    # this is silly, I know
    return None
