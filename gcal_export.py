# gcal_export.py  –  Google Calendar sync (very rough, human style) 📆
import pickle, os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.events']

# load or get credentials
def get_creds():
    creds = None
    if os.path.exists('token.pkl'):
        creds = pickle.load(open('token.pkl','rb'))
    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        pickle.dump(creds, open('token.pkl','wb'))
    return creds

# slap events into calendar
def export_to_gcal(plan):
    creds = get_creds()
    service = build('calendar', 'v3', credentials=creds)
    for item in plan:
        start, end = item['when']
        event = {
            'summary': item['what'],
            'start': {'dateTime': f"2025-04-20T{start}:00", 'timeZone': 'Asia/Tehran'},
            'end':   {'dateTime': f"2025-04-20T{end}:00", 'timeZone': 'Asia/Tehran'}
        }
        try:
            service.events().insert(calendarId='primary', body=event).execute()
            print(f"added: {item['what']}")
        except Exception as e:
            print("whoops, failed to add event:", e)

# usage (in CLI or app)
if __name__=='__main__':
    from schedule_planner import match_tasks_to_slots, load_tasks, get_today_vibes
    from free_time_finder import slots
    tasks = load_tasks()
    vibes = get_today_vibes()
    plan = match_tasks_to_slots(tasks, slots, vibes)
    export_to_gcal(plan)
    print("done-ish, check your calendar?")
