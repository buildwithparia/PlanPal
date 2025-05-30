
# PlanPal 💖  
A mood-aware daily planner that helps you get things done without pushing yourself too hard.

---

## 🧠 What is PlanPal?

**PlanPal** is a smart, mood-driven daily planning assistant built in Python.  
Unlike traditional schedulers, PlanPal tailors your tasks to match your current emotional and energy state — helping you plan more intuitively, not just efficiently.

Whether you're feeling joyful, tired, or stressed, PlanPal adjusts your day with empathy.

---

## ✨ Features

- 🌀 **Mood-based task matching** using a personal mood journal (`mood.json`)
- ✅ **Automatic task vibe detection** (e.g., “study” = deep focus, “paint” = creative)
- 🕒 **Time slot detection** from your daily schedule (`fixed_schedule.json`)
- 📆 **Google Calendar sync** using OAuth (exports your plan directly)
- 💻 **Streamlit UI** — mobile-friendly, pastel-themed, and simple to use
- 💾 Offline-friendly — no external database or backend required

---

## 🛠️ Technologies Used

- Python 3.10  
- Streamlit (UI)  
- Google Calendar API (with `google-auth-oauthlib`)  
- Regex + custom logic for task classification  
- JSON files for lightweight, editable data

---

## 📦 Folder Structure (Core Files)

```
PlanPal/
│
├── PlanPal_app.py             ← Streamlit UI
├── PlanPal_brain.py           ← Reads today's mood + energy
├── schedule_planner.py        ← Core logic for matching tasks to time slots
├── task_extractor.py          ← Tags each task with a "vibe"
├── mood_rules.py              ← Maps moods → suitable task vibes
├── free_time_finder.py        ← Parses free blocks from fixed schedule
├── gcal_export.py             ← Sends final plan to Google Calendar
├── data/
│   ├── mood.json              ← Personal mood log
│   ├── fixed_schedule.json    ← Daily commitments
│   └── goals.txt              ← Raw list of tasks
```

---

## 🌍 Real-World Impact

This project tackles a widespread issue:  
> Many people plan tasks logically, but not emotionally — leading to burnout, avoidance, or guilt.

PlanPal aims to bridge that gap.  
It helps users:
- Work **with** their moods, not against them
- Build **realistic** schedules during low-energy days
- Boost consistency by respecting emotional rhythms

This tool can benefit:
- Students managing burnout or exam stress  
- Professionals balancing deep work with recovery  
- Users with ADHD who struggle with rigid planners

---

## 🚧 Challenges

- **Mapping moods to task vibes** was deeply subjective — required testing with multiple emotional states
- Designing a lightweight planner with **no database** while preserving flexibility
- Handling **timezone quirks** with Google Calendar export
- Wanting a more dynamic UI — but Streamlit had limitations I hope to improve later

---

## 🌀 Inspired by Plutchik's Wheel of Emotions

I based the mood system loosely on **Dr. Robert Plutchik’s Feelings Wheel**.  
I didn’t use it strictly, but it helped me decide how moods like "joy" or "sadness" might affect what types of tasks feel right.

This helped in designing PlanPal’s vibe categories and mood-response rules.

---

## ✅ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/buildwithparia/PlanPal.git
   cd PlanPal
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your:
   - `mood.json`, `fixed_schedule.json`, and `goals.txt` to `data/`
   - `credentials.json` in root (get from Google Cloud Console)

4. Run locally:
   ```bash
   streamlit run PlanPal_app.py
   ```

---

## 📌 To-Do & Future Plans

- 🔄 Improve UI layout and navigation (current version is functional but limited)
- 🗂️ Support for multiple days and weekly planning
- 📊 Add optional analytics for mood trends and focus tracking
- 🔒 Secure handling for OAuth and secret keys
- 🖼️ Add animated transitions or visual feedback for better UX

---

## ❤️ Final Notes

This project is not about perfect productivity.  
It's about designing tech that listens to *how you feel*.  
PlanPal reflects my growing belief:  
> “Productivity should feel kind, not cold.”

---

## ✍️ Built By

Made with empathy
by [Paria](https://github.com/buildwithparia) —  
Developer, designer, and aspiring AI researcher.

---

## 🔐 About .gitignore

I added a `.gitignore` file to make sure `credentials.json` and `token.pkl` (Google auth stuff) don’t get uploaded by accident.  
If you're using this project yourself, make sure you protect your own keys too.

---

## 📘 License

Released under the [MIT License](./LICENSE).  
Because good ideas deserve to be shared — kindly, openly, and with just a little bit of magic ✨
