# planpal_app.py  –  Streamlit UI, super Paria pastel kawaii 💖
import streamlit as st
import json
from datetime import datetime, timedelta
from task_extractor import extract_tasks
from mood_rules import get_good_vibes

# helper to compute free slots (from free_time_finder, adapted)
def get_slots(day):
    fmt = '%H:%M'
    try:
        data = json.loads(open('data/fixed_schedule.json').read())
    except:
        data = {}
    blocks = data.get(day, [])
    events = []
    for ev in blocks:
        try:
            s = datetime.strptime(ev['start'], fmt)
            e = datetime.strptime(ev['end'], fmt)
            events.append((s, e))
        except:
            pass
    events.sort(key=lambda x: x[0])
    start_w = datetime.strptime('08:00', fmt)
    end_w   = datetime.strptime('22:00', fmt)
    ptr = start_w
    gaps = []
    for s, e in events:
        if ptr < s:
            gaps.append((ptr, s))
        ptr = max(ptr, e)
    if ptr < end_w:
        gaps.append((ptr, end_w))
    slots = []
    t = None
    for gstart, gend in gaps:
        t = gstart
        while t + timedelta(minutes=30) <= gend:
            slots.append((t.strftime(fmt), (t + timedelta(minutes=30)).strftime(fmt)))
            t += timedelta(minutes=30)
    return slots

# CSS for pastel themes and cute fonts
theme_css = '''
<style>
@import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@300;700&display=swap');
body, .stApp, .block-container {
    background-color: #eef5d9 !important;
    color: #553149 !important;
    font-family: 'Comic Neue', cursive;
}
h1 {
    color: #f72c5b !important;
    font-size: 2.2rem !important;
    white-space: nowrap;
    text-align: center;
    margin-top: 0.5rem;
}
h3 {
    color: #a63368 !important;
    font-size: 1.1rem !important;
    margin-bottom: 0.5rem;
}
.stButton>button {
    background-color: #ff748b !important;
    color: #fff !important;
    border-radius: 12px;
    padding: 10px 24px;
    font-size: 1rem;
    font-family: 'Comic Neue', cursive;
}
.stTextArea>textarea, .stTextInput>div>input {
    background-color: #fff5f8 !important;
    border: 2px solid #f72c5b !important;
    border-radius: 12px !important;
    padding: 8px !important;
    color: #553149 !important;
    font-family: 'Comic Neue', cursive;
}
.stSelectbox>div>div, .stSelectbox>label {
    background-color: #fff5f8 !important;
    border: 2px solid #ffb6c1 !important;
    border-radius: 12px !important;
    padding: 6px 8px !important;
    font-family: 'Comic Neue', cursive;
    color: #553149 !important;
}
::-webkit-scrollbar {
    width: 10px;
}
::-webkit-scrollbar-track {
    background: #eef5d9;
}
::-webkit-scrollbar-thumb {
    background-color: #d91656;
    border-radius: 5px;
}
</style>
'''
st.set_page_config(page_title="PlanPal 💖", page_icon="⭐", layout="centered")
st.markdown(theme_css, unsafe_allow_html=True)

# Header
st.title("✨ PlanPal — Your Kawaii Day Scheduler ✨")
st.markdown("<h3 style='font-family:Comic Neue; color:#a63368; margin-top:0.4rem;'>Built at 3AM, excuse the glitter ✨</h3>", unsafe_allow_html=True)

# Select day label
st.markdown("<p style='font-family:Comic Neue; color:#3e1f47; font-size:1rem; margin-top:1rem;'>Which day is it?</p>", unsafe_allow_html=True)
# single dropdown with collapsed label
day = st.selectbox(
    "",
    ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
    label_visibility='collapsed'
)

# Load mood
try:
    moods = json.loads(open('data/mood.json').read())
    today_mood = next(m for m in moods if m['day']==day)
except:
    today_mood = {'mood':'random','energy':'meh'}
st.markdown(
    "<p style='font-family:Comic Neue; color:#3e1f47; font-size:1rem;'>🌀 <strong>Mood:</strong> "
    f"{today_mood['mood']} | <strong>Energy:</strong> {today_mood['energy']}</p>",
    unsafe_allow_html=True
)

# Goals input area label
st.markdown(
    "<p style='font-family:Comic Neue; color:#3e1f47; font-size:1rem;'>Your goals (comma or newline separated):</p>",
    unsafe_allow_html=True
)
# text area for goals
goals_input = st.text_area("", height=120, placeholder="e.g. Study math, clean desk, journal...")

# Generate Plan
if st.button("Generate Plan ❤️"):
    text = goals_input if goals_input.strip() else open('data/goals.txt').read()
    tasks = extract_tasks(text)
    vibes = get_good_vibes(today_mood['mood'])
    slots = get_slots(day)
    plan = []
    for t in tasks:
        if slots and t['vibe'] in vibes:
            when = slots.pop(0)
            plan.append({'when':when,'what':t['what'],'vibe':t['vibe']})
    # display
    if plan:
        st.markdown(
            "<div style='background:#ffdce0; padding:12px; border-radius:10px; margin-top:1rem;'>"
            "<h3 style='font-family:Comic Neue; color:#d6336c;'>Here's your plan ✨</h3>"
            + ''.join([
                f"<p style='font-family:Comic Neue; color:#553149;'>🕒 <strong>{e['when'][0]}</strong> - <strong>{e['when'][1]}</strong>: {e['what']} "
                f"<em>({e['vibe']})</em></p>" for e in plan])
            + "</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<p style='font-family:Comic Neue; color:#a63368;'>…nothing matches today. Maybe snack time? 🍪</p>",
            unsafe_allow_html=True
        )
    st.markdown(
        "<h3 style='font-family:Comic Neue; color:#d6336c;'>✨ PlanPal says: Go slay your day! ✨</h3>",
        unsafe_allow_html=True
    )
