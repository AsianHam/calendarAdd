from math import floor
from ratelimit import limits, sleep_and_retry

from calSetup import get_calendar_service

TOTAL_REQUESTS_PER_PERIOD = 100000
NUMBER_OF_METHODS = 3
REQUESTS_PER_METHOD = floor(TOTAL_REQUESTS_PER_PERIOD / NUMBER_OF_METHODS)
PERIOD_IN_SECS = 100


@sleep_and_retry
@limits(calls=REQUESTS_PER_METHOD, period=PERIOD_IN_SECS)
def add(service, uni, cal):

    rule = {
        "scope": {
            "type": "user",
            "value": uni,
        },
        "role": "writer",
    }

    service.acl().insert(
        calendarId=cal, body=rule, sendNotifications=True
    ).execute()


@sleep_and_retry
@limits(calls=REQUESTS_PER_METHOD, period=PERIOD_IN_SECS)
def delete(service, uni, cal):

    user = "user:" + uni

    service.acl().delete(calendarId=cal, ruleId=user).execute()


@sleep_and_retry
@limits(calls=REQUESTS_PER_METHOD, period=PERIOD_IN_SECS)
def listUser(service, cal):

    acl = service.acl().list(calendarId=cal).execute()

    users = []

    for rule in acl["items"]:
        users.append("%s: %s" % (rule["id"], rule["role"]))

    return users


if __name__ == "__main__":
    print(listUser(get_calendar_service(), "id@resource.calendar.google.com"))
