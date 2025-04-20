# let's rock this PlanPal 🚀

import free_time_finder
from task_extractor import extract_tasks
from PlanPal_brain import your_mood  # grab today's vibes
from mood_rules import get_good_vibes


def load_tasks(src='data/goals.txt'):
    # omg reading tasks, hold tight! maybe switch to DB someday
    try:
        with open(src, 'r') as f:
            text = f.read()
    except Exception as e:
        print("whoops, can't read tasks:", e)
        text = ''
    # raw text → parse into tasks
    return extract_tasks(text)


def get_today_vibes():
    # woo! pick today's vibe filter
    if your_mood:
        mood = your_mood.get('mood', 'random')  # fallback if missing
    else:
        mood = 'random'
    vibes = get_good_vibes(mood)
    print(f"✨ Today's mood: {mood}, vibes: {vibes}")  # shout it out
    return vibes


def match_tasks_to_slots(tasks, slots, vibes):
    plan = []
    #this will eat from slots list directly
    for task in tasks:
        if not slots:
            print("😮 out of slots! consider rescheduling")
            break
        if task['vibe'] in vibes:
            current = slots.pop(0)
            plan.append({ 'when': current, 'what': task['what'], 'vibe': task['vibe'] })
        else:
            # not matching? maybe later 🤷‍♀️
            pass
    return plan


def print_schedule(schedule):
    print("\n🔥 Here's your PlanPal schedule:")
    for entry in schedule:
        start, end = entry['when']
        print(f"{start} → {end}: {entry['what']} ({entry['vibe']})")
    if not schedule:
        print("…hmm, nothing matched today. Time for a break? 😌")



def cheer():
      # extra indent cause excitemeeent!
      print('Yay, done! Go slay your day! 💪')


# entry point
if __name__ == "__main__":
    tasks = load_tasks()  # evolving name alert
    vibes = get_today_vibes()
    slots = free_time_finder.slots  # precomputed free slots
    # schedule matching (basic greedy)
    daily_plan = match_tasks_to_slots(tasks, slots, vibes)
    print_schedule(daily_plan)
    cheer()  # hype you up


def future_ideas():
    # maybe visualize with matplotlib? lol
    pass

