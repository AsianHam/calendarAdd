from calSetup import get_calendar_service

SCOPES = ['https://www.googleapis.com/auth/calendar']

def add(uni, cal):
    service = get_calendar_service()

    rule = {
        'scope': {
            'type': 'user',
            'value': uni,
        },
        'role': 'writer'
    }

    service.acl().insert(calendarId = cal, body = rule, sendNotifications = False).execute()

def delete(uni, cal):
    service = get_calendar_service()

    user = "user:" + uni

    service.acl().delete(calendarId = cal, ruleId = user).execute()

def listUser(cal):
    service = get_calendar_service()

    acl = service.acl().list(calendarId = cal).execute()

    users = []

    for rule in acl['items']:
        users.append('%s: %s' % (rule['id'], rule['role']))
    
    return(users)

if __name__ == "__main__":
    broadway = 'columbia.edu_3634343538303339393332@resource.calendar.google.com'
    print(listUser(broadway))